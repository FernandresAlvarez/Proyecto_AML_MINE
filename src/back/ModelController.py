# src/back/ModelController.py

import Definitions
import os.path as osp
import joblib
import pandas as pd

from src.model.DataPreprocessingRF import DataPreprocessingRF
from src.model.DataPreprocessingMS import DataPreprocessingMS
from src.model.DataPreprocessingMLPRegressor import DataPreprocessingMLPRegressor

class ModelController:

    def __init__(self):
        print("ModelController.__init__ ->")
        # Ruta base donde están los .joblib
        base = osp.join(Definitions.ROOT_DIR, "resources/models")

        # Paths a tus modelos serializados
        self.RandomForest_model_path         = osp.join(base, "df1RandomForest.joblib")
        self.MeanShift_model_path            = osp.join(base, "df4MeanShift.joblib")
        self.DecisionTreeClusters_model_path = osp.join(base, "dfClustersDecisionTree.joblib")
        self.OneClassSVM_model_path          = osp.join(base, "df5OneClassSVM.joblib")
        self.MLPRegressor_model_path         = osp.join(base, "df6MLPRegressor.joblib")

        # Carga de los modelos
        self.RandomForest_model = joblib.load(self.RandomForest_model_path)
        self.MeanShift_model    = joblib.load(self.MeanShift_model_path)
        self.DT_model           = joblib.load(self.DecisionTreeClusters_model_path)
        self.OCSVM_model        = joblib.load(self.OneClassSVM_model_path)
        self.MLPRegressor_model = joblib.load(self.MLPRegressor_model_path)

        # Extraer categorías de Industry para el UI de SVM
        # Asume que tu pipeline OCSVM tiene un step 'preprocessing' con un transformer 'cat'
        try:
            ct = (self.OCSVM_model
                  .named_steps['preprocessing']
                  .named_transformers_['cat'])
            self.svm_industries = list(ct.categories_[0])
        except Exception:
            self.svm_industries = []

        # Instanciar tus preprocesadores
        self.d_processing_RF         = DataPreprocessingRF()
        self.d_processing_MS         = DataPreprocessingMS()
        self.d_processing_MLPRegressor = DataPreprocessingMLPRegressor()


    # --- Tab 1: RandomForestClassifier ----------------
    def predict_RF(self, input_data):
        print("ModelController.predict_RF ->")
        X = self.d_processing_RF.transform(input_data)
        y = self.RandomForest_model.predict(X)

        df = X.copy()
        df["Predicción"] = y
        df["Predicción"] = df["Predicción"].replace({
            0: self.d_processing_RF.get_cat_name(0),
            1: self.d_processing_RF.get_cat_name(1)
        })
        return df, y


    # --- Tab 2 Part A: MeanShift Clustering ----------
    def predict_ms(self, input_data):
        print("ModelController.predict_ms ->")
        # Extraer el objeto MeanShift (si está dentro de un Pipeline)
        clustering = (
            self.MeanShift_model.named_steps['clustering']
            if hasattr(self.MeanShift_model, 'named_steps')
            else self.MeanShift_model
        )
        feature_names = clustering.feature_names_in_
        # Reindexar tu input para que tenga EXACTAMENTE esas columnas
        X = input_data.reindex(columns=feature_names, fill_value=0)
        labels = self.MeanShift_model.predict(X)

        df = X.copy()
        df["Cluster_MS"] = labels
        return df, labels


    # --- Tab 2 Part B: DecisionTree on Clusters -----
    def predict_dt(self, input_data):
        print("ModelController.predict_dt ->")
        clustering = (
            self.MeanShift_model.named_steps['clustering']
            if hasattr(self.MeanShift_model, 'named_steps')
            else self.MeanShift_model
        )
        feature_names = clustering.feature_names_in_
        X = input_data.reindex(columns=feature_names, fill_value=0)
        labels = self.DT_model.predict(X)

        df = X.copy()
        df["Cluster_DT"] = labels
        return df, labels


    # --- Tab 3: OneClassSVM --------------------------
    def get_svm_industries(self):
        """Lista de categorías de Industry que entrenó el SVM."""
        return self.svm_industries

    def predict_ocsvm(self, input_data):
        print("ModelController.predict_ocsvm ->")
        # Estas son las columnas que tu pipeline espera
        feature_cols = [
            'Industry',
            'Startup_Age',
            'Funding_Amount',
            'Revenue',
            'Customer_Retention_Rate',
            'Revenue_to_Burn_Ratio',
            'Employees_Count',
            'High_Retention'
        ]
        X = input_data.reindex(columns=feature_cols, fill_value=0)
        preds = self.OCSVM_model.predict(X)

        df = X.copy()
        df["Anomaly"] = preds
        df["Anomaly"] = df["Anomaly"].replace({1: "Normal", -1: "Anomalía"})
        return df, preds


    # --- Tab 4: MLPRegressor -------------------------
    def predict_MLPRegressor(self, input_data):
        print("ModelController.predict_MLPRegressor ->")
        X = self.d_processing_MLPRegressor.transform(input_data)
        y = self.MLPRegressor_model.predict(X)

        df = X.copy()
        df["Predicción"] = y
        return df, y
