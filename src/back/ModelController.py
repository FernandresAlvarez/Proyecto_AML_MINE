import Definitions

import numpy as np
import os.path as osp
import pandas as pd
from io import StringIO

import joblib
from src.model.DataPreprocessingRF import DataPreprocessingRF
from src.model.DataPreprocessingMLPRegressor import DataPreprocessingMLPRegressor
#from src.model.DataPreprocessingMS import DataPreprocessingMS
#from src.model.DataPreprocessing3 import DataPreprocessing3
#from src.model.DataPreprocessing4 import DataPreprocessing4
#from src.model.DataPreprocessing5 import DataPreprocessing5
#TODO

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report



class ModelController:

    def __init__(self):
        print("ModelController.__init__ ->")
        # Asegura en una variable la ruta de los modelos
        self.model_path = osp.join(Definitions.ROOT_DIR, "resources/models")
        #TODO

        self.RandomForest_model_path = osp.join(self.model_path, "df1RandomForest.joblib")
        self.MLPRegressor_model_path = osp.join(self.model_path, "df6MLPRegressor.joblib")
        #self.MeanShift_model_path = osp.join(self.model_path, "df4MeanShift.joblib")
        #self.OneClassSVM_model_path = osp.join(self.model_path, "df5OneClassSVM.joblib")
        #self.LinearRegression_model_path = osp.join(self.model_path, "dfRegresion.joblib")
        #TODO

        #Cargar los modelos
        self.RandomForest_model = joblib.load(self.RandomForest_model_path)
        self.MLPRegressor_model = joblib.load(self.MLPRegressor_model_path)
        #self.MeanShift_model = joblib.load(self.MeanShift_model_path)
        #self.OneClassSVM_model = joblib.load(self.OneClassSVM_model_path)
        #self.LinearRegression_model = joblib.load(self.LinearRegression_model_path)
        #TODO

        # Inicializar variables
        self.X_test_RF = ""
        self.Y_test_RF = ""
        self.y_pred_RF = ""
        
        self.X_test_MLPRegressor = ""
        self.Y_test_MLPRegressor = ""
        self.y_pred_MLPRegressor = ""




        # Clase de preprocesamiento de la información
        self.d_processing_RF = DataPreprocessingRF()
        self.d_processing_MLPRegressor = DataPreprocessingMLPRegressor()
        #self.d_processing_MS = DataPreprocessingMS()
        #TODO


    def predict_RF(self, input_data):
        print("ModelController.predict ->")

        # Generamos la partición de la información
        self.X_test_RF = self.d_processing_RF.transform(input_data)
        #print(self.X_test_RF)
        #TODO

        # Predicciones Isolation Forest, One Class SVM y Regresión Lineal
        self.y_pred_RF = self.RandomForest_model.predict(self.X_test_RF)
        #print("La predicción es:", self.y_pred_RF)
        #TODO

        # Preparamos un dataframe para presentar al usuario final
        RF_result_df = self.X_test_RF.copy()

        RF_result_df["Predicción"] = self.y_pred_RF
        RF_result_df["Predicción"] = RF_result_df["Predicción"].replace(
            {0: self.d_processing_RF.get_cat_name(0), 1: self.d_processing_RF.get_cat_name(1)})
        #print(RF_result_df)
        #TODO
        
        #RF_result_df[f"Probabilidad Clase {self.d_processing_RF.get_cat_name(0)} (%)"] = y_pred_proba_svc[:, 0]
        #RF_result_df[f"Probabilidad Clase {self.d_processing_RF.get_cat_name(1)} (%)"] = y_pred_proba_svc[:, 1]

        # Predicciones RF y probabilidad (con redondeo)
        #y_pred_rf = self.rf_model.predict(X_test)
        #y_pred_proba_rf = self.svc_model.predict_proba(X_test)
        #y_pred_proba_rf = np.round(y_pred_proba_rf * 100, 2)
        #TODO

        # Dataframe compilado
        #full_result_df = X_test.copy()
        #full_result_df["Real"] = svc_result_df["Real"]
        #full_result_df["Predicción SVM"] = svc_result_df["Predicción"]
        #full_result_df[f"Probabilidad Clase {self.d_processing.get_cat_name(0)} (%) SVM"] = svc_result_df[f"Probabilidad Clase {self.d_processing.get_cat_name(0)} (%)"]
        #full_result_df[f"Probabilidad Clase {self.d_processing.get_cat_name(1)} (%) SVM"] = svc_result_df[f"Probabilidad Clase {self.d_processing.get_cat_name(1)} (%)"]
        #full_result_df["Predicción RF"] = rf_result_df["Predicción"]
        #full_result_df[f"Probabilidad Clase {self.d_processing.get_cat_name(0)} (%) RF"] = rf_result_df[f"Probabilidad Clase {self.d_processing.get_cat_name(0)} (%)"]
        #full_result_df[f"Probabilidad Clase {self.d_processing.get_cat_name(1)} (%) RF"] = rf_result_df[f"Probabilidad Clase {self.d_processing.get_cat_name(1)} (%)"]
        #TODO
        return RF_result_df, self.y_pred_RF
    


    def predict_MLPRegressor(self, input_data):
        print("ModelController.predict ->")

        # Generamos la partición de la información
        self.X_test_MLPRegressor = self.d_processing_MLPRegressor.transform(input_data)
        #print(self.X_test_MLPRegressor)
        
        # Predicciones Isolation Forest, One Class SVM y Regresión Lineal
        self.y_pred_MLPRegressor = self.MLPRegressor_model.predict(self.X_test_MLPRegressor)
        #print("La predicción es:", self.y_pred_MLPRegressor)
        
        # Preparamos un dataframe para presentar al usuario final
        MLPRegressor_result_df = self.X_test_MLPRegressor.copy()

        MLPRegressor_result_df["Predicción"] = self.y_pred_MLPRegressor
        #print(MLPRegressor_result_df)
        
        return MLPRegressor_result_df, self.y_pred_MLPRegressor



#def final_pred(self):
#    if self.y_pred_RF == 1:
#        if #TODO

#    return (mensaje, valorizacion, imagen)

