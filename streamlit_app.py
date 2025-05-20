#Aseguramos el control de rutas en python
import Definitions
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import streamlit as st
#from io import StringIO

from src.back.ModelController import ModelController

### Setup and configuration

st.set_page_config(page_title="Evaluación de tu Startup", layout="centered")
st.title("🚀 Evaluación Interactiva de Startups")


### Support functions
def highlight_diff(row):
    if row["Real"] != row["Predicción"]:
        # return ["background-color: blue"] * len(row)
        return ["background-color: #F5F5F5; color: black; font-weight: bold"] * len(row)
    return [""] * len(row)


### My vars
ctrl = ModelController()


### My UI starting here

with st.expander("Tip"):
    f"""
    Please upload your file, click on submit. We will provide you the results. 
    """

with st.form(key="my_form"):

    uploaded_file = st.file_uploader(
        "Choose a CSV file", accept_multiple_files=False, type="csv"
    )

    submit_button = st.form_submit_button(label="Submit")

    with st.spinner("Processing your information...."):

        if submit_button and uploaded_file is not None:

            try:

                # Cargar la información del archivo csv
                bytes_data = uploaded_file.getvalue()
                st.write("Filename:", uploaded_file.name)

                 #Asegurar la información de entrada como pandas dataframe
                input_df, is_valid = ctrl.load_input_data(bytes_data)

                if not is_valid:
                    st.warning("File structure not valid", icon="⚠️")
    
                # Presentamos la inforamción de forma tabulada o pestañas
                tab1 = st.tabs(["Random Forest"])
                #TODO: tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Random Forest", "MeanShift", "Decision Tree", "OneClassSVM", "MLPRegressor", "Start-Up State", "Stats"])


                RF_df = ctrl.predict()
                RF_EvalMets = ctrl.evaluation_metrics()

                #RF_df, MS_df, DT_df, OCSVM_df, MLPR_df = ctrl.predict()
                #RF_EvalMets, MS_EvalMets, DT_EvalMets, OCSVM_EvalMets, MLPR_EvalMets = ctrl.evaluation_metrics()
                #FinalPred = ctrl.final_pred() #Tupla para incluir mensaje, imagen y valorización de start up, si fue exitosa
                #TODO

                # Tabla con predicciones, métricas de evaluación y gráficas
                # Estado final de recomendación de la start up: Fallido: Mensaje e imagen, Exitoso: Mensaje, valorización e imagen
                # Stats: Demás gráficas

                with tab1:
                    RF_styled_df = RF_df.style.apply(highlight_diff, axis=1)
                    st.subheader("🏿 Original data and predictions")
                    # st.dataframe(RF_df)
                    st.dataframe(RF_styled_df) # Presentar el df 

                    st.subheader("🔎 Evaluation Metrics")
                    st.dataframe(RF_EvalMets.style)


                    
                if is_valid:
                    st.success("✅ Done!")
            except:
                st.error("Something happened", icon="🚨")

        elif submit_button and uploaded_file is None:
            st.error("You must choose a csv file", icon="🚨")


                

            
    
