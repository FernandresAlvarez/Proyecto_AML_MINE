import Definitions

import numpy as np
import os.path as osp
import pandas as pd
from io import StringIO

import joblib
from src.model.DataPreprocessingRF import DataPreprocessingRF
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
        # Almacena la ruta de cada modelo en una variable
        #self.rf_model_path = osp.join(self.model_path, "rf_model.joblib")
        #self.svc_model_path = osp.join(self.model_path, "svc_model.joblib")

        self.RandomForest_model_path = osp.join(self.model_path, "df1RandomForest.joblib")
        #self.MeanShift_model_path = osp.join(self.model_path, "df4MeanShift.joblib")
        #self.OneClassSVM_model_path = osp.join(self.model_path, "df5OneClassSVM.joblib")
        #self.LinearRegression_model_path = osp.join(self.model_path, "dfRegresion.joblib")
        #TODO

        #Cargar los modelos
        self.RandomForest_model = joblib.load(self.RandomForest_model_path)
        #self.MeanShift_model = joblib.load(self.MeanShift_model_path)
        #self.OneClassSVM_model = joblib.load(self.OneClassSVM_model_path)
        #self.LinearRegression_model = joblib.load(self.LinearRegression_model_path)
        #TODO

        # Inicializar variables
        self.input_df = ""

        self.X_test_RF = ""
        self.Y_test_RF = ""
        self. y_pred_RF = ""
        #TODO

        # Clase de preprocesamiento de la información
        self.d_processing_RF = DataPreprocessingRF()
        #self.d_processing_MS = DataPreprocessingMS()
        #TODO


    def validate_data_RF(self, df):
        return self.d_processing_RF.get_columns().issubset(df.columns)
        #TODO

    def load_input_data(self, input_data):
        print("ModelController.load_input_data ->")
        try:
            input_data_str = StringIO(input_data.decode("utf-8"))
            self.input_df = pd.read_csv(input_data_str)
            is_valid = self.validate_data(self.input_df)
            return self.input_df, is_valid

        except:
            raise("Ocurrió un error al leer la información de entrada")

    def predict(self):
        print("ModelController.predict ->")

        # Generamos la partición de la información
        #X_test, Y_test = self.input_df.drop([self.target_feature], axis=1), self.input_df[self.target_feature]
        self.X_test_RF, self.Y_test_RF = self.d_processing_RF.transform(self.input_df)
        #TODO

        # Predicciones Isolation Forest, One Class SVM y Regresión Lineal
        self.y_pred_RF = self.RandomForest_model.predict(self.X_test_RF)
        #TODO


        # Preparamos un dataframe para presentar al usuario final
        RF_result_df = self.X_test_RF.copy()
        RF_result_df["Real"] = self.Y_test_RF.values
        RF_result_df["Real"] = RF_result_df["Real"].replace(
            {0: self.d_processing_RF.get_cat_name(0), 1: self.d_processing_RF.get_cat_name(1)})

        RF_result_df["Predicción"] = self.y_pred_RF
        RF_result_df["Predicción"] = RF_result_df["Predicción"].replace(
            {0: self.d_processing_RF.get_cat_name(0), 1: self.d_processing_RF.get_cat_name(1)})
        #TODO

        

        #RF_result_df[f"Probabilidad Clase {self.d_processing_RF.get_cat_name(0)} (%)"] = y_pred_proba_svc[:, 0]
        #RF_result_df[f"Probabilidad Clase {self.d_processing_RF.get_cat_name(1)} (%)"] = y_pred_proba_svc[:, 1]

        # Predicciones RF y probabilidad (con redondeo)
        #y_pred_rf = self.rf_model.predict(X_test)
        #y_pred_proba_rf = self.svc_model.predict_proba(X_test)
        #y_pred_proba_rf = np.round(y_pred_proba_rf * 100, 2)

        # Dataframe de los resultados para RandomForest
        #rf_result_df = X_test.copy()
        #rf_result_df["Real"] = Y_test.values
        #rf_result_df["Real"] = rf_result_df["Real"].replace(
        #    {0: self.d_processing_RF.get_cat_name(0), 1: self.d_processing_RF.get_cat_name(1)})
        #rf_result_df["Predicción"] = y_pred_rf
        #rf_result_df["Predicción"] = rf_result_df["Predicción"].replace(
        #    {0: self.d_processing_RF.get_cat_name(0), 1: self.d_processing_RF.get_cat_name(1)})
        #rf_result_df[f"Probabilidad Clase {self.d_processing_RF.get_cat_name(0)} (%)"] = y_pred_proba_rf[:, 0]
        #rf_result_df[f"Probabilidad Clase {self.d_processing_RF.get_cat_name(1)} (%)"] = y_pred_proba_rf[:, 1]
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
        return RF_result_df
    
    #TODO

def evaluation_metrics(self):
    
    RF_evalmets = classification_report(self.Y_test_RF, self.y_pred_RF)
    # Generar el reporte como un diccionario
    report_dict = classification_report(self.Y_test_RF, self.y_pred_RF, output_dict=True)
    # Convertir el diccionario a DataFrame
    report_df = pd.DataFrame(report_dict).transpose()

    #TODO

    return report_df



#def final_pred(self):
#    if self.y_pred_RF == 1:
#        if #TODO

#    return (mensaje, valorizacion, imagen)

    #Probar RF y luego con los demás de a pocos. De streamlit falta formulario y habría que ingresar un conjunto de datos test
    # Actualizar modelo RF actualizado de Manuel


