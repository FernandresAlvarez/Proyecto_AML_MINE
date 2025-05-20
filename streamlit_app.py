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

with st.form("form_inicial"):
    Unnamed0 = st.number_input("Valor numérico", min_value=0.0, value=1.0)
    Código_Estatal  = st.selectbox("Estado", ["CA", "NY", "MA", "WA", "TX", "CO", "IL", "PA", "VA", "GA", "NC", "OR", "NJ", "MD", "FL", "OH", "MN", "CT", "DC", "UT", "TN", "RI", "MI", "KY", "ME", "NH", "MO", "IN", "NV", "AZ", "WV", "NM", "ID", "AR", "WI"])
    
    relationships          = st.number_input("Número de relaciones/inversionistas", min_value=0.0, value=1.0)
    funding_rounds         = st.number_input("Número de rondas de financiación", min_value=0,   value=1)
    funding_total_usd      = st.number_input("Total financiado (USD)", min_value=0.0, value=10000.0)
    milestones             = st.number_input("Número de hitos alcanzados", min_value=0,   value=1)
    age_first_milestone_year = st.number_input("Años hasta primer hito", min_value=0.0, value=1.0)
    age_last_milestone_year  = st.number_input("Años desde último hito", min_value=0.0, value=0.0)
    state                    = st.selectbox("Estado", ["activo", "inactivo", "pivot"])
    industry_type            = st.selectbox("Sector / Industria", ["tech", "finanzas", "salud", "otro"])
    has_VC                   = st.selectbox("¿Cuenta con VC?", ["sí", "no"])
    has_angel                = st.selectbox("¿Cuenta con ángeles?", ["sí", "no"])
    has_roundA               = st.selectbox("¿Ronda A?", ["sí", "no"])
    has_roundB               = st.selectbox("¿Ronda B?", ["sí", "no"])
    has_roundC               = st.selectbox("¿Ronda C?", ["sí", "no"])
    has_roundD               = st.selectbox("¿Ronda D?", ["sí", "no"])
    avg_participants         = st.number_input("Participantes promedio en rondas", min_value=0.0, value=5.0)
    is_top500                = st.selectbox("¿Está en Top500 startups?", ["sí", "no"])
    submit_init              = st.form_submit_button("Evaluar inicio")

if submit_init:
    df_init = pd.DataFrame([{
        "age_first_funding_year":    age_first_funding_year,
        "age_last_funding_year":     age_last_funding_year,
        "relationships":             relationships,
        "funding_rounds":            funding_rounds,
        "funding_total_usd":         funding_total_usd,
        "milestones":                milestones,
        "age_first_milestone_year":  age_first_milestone_year,
        "age_last_milestone_year":   age_last_milestone_year,
        "state":                     state,
        "industry_type":             industry_type,
        "has_VC":                    has_VC,
        "has_angel":                 has_angel,
        "has_roundA":                has_roundA,
        "has_roundB":                has_roundB,
        "has_roundC":                has_roundC,
        "has_roundD":                has_roundD,
        "avg_participants":          avg_participants,
        "is_top500":                 is_top500
    }])

elif st.form_submit_button("Evaluar inicio") is None:
    st.error("You must choose a csv file", icon="🚨")


    with st.spinner("Processing your information...."):

        if st.form_submit_button("Evaluar inicio") is not None:
            try:

                # Presentamos la inforamción de forma tabulada o pestañas
                tab1, tab2, tab3, tab4, tab5 = st.tabs(["Random Forest", "MeanShift", "Decision Tree", "OneClassSVM", "MLPRegressor", "Start-Up State", "Stats"])

                RF_df, MS_df, DT_df, OCSVM_df, MLPR_df = ctrl.predict()
                RF_EvalMets, MS_EvalMets, DT_EvalMets, OCSVM_EvalMets, MLPR_EvalMets = ctrl.evaluation_metrics()
                FinalPred = ctrl.final_pred() #Tupla para incluir mensaje, imagen y valorización de start up, si fue exitosa

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



                with tab2:
                    svc_styled_df = svc_df.style.apply(highlight_diff, axis=1)
                    st.subheader("🏿 Original data and predictions")
                    # st.dataframe(svc_df)
                    st.dataframe(svc_styled_df) # Presentar el df

                with tab3:
                    rf_styled_df = rf_df.style.apply(highlight_diff, axis=1)
                    st.subheader("🏿 Original data and predictions")
                    # st.dataframe(svc_df)
                    st.dataframe(rf_styled_df)

                with tab4:
                    full_styled_df = full_df.style.apply(highlight_full_diff, axis=1)
                    st.subheader("🏿 Original data and predictions")
                    # st.dataframe(full_df)
                    st.dataframe(full_styled_df)
                
                with tab5:
                    df_long = full_df.melt(id_vars=["Real"], value_vars=["Predicción RF", "Predicción SVM"],
                                            var_name="Modelo", value_name="Predicción")

                    df_counts = df_long.groupby(["Modelo", "Predicción"]).size().reset_index(name="Cantidad")

                    fig = px.bar(df_counts, x="Modelo", y="Cantidad", color="Predicción",
                                    title="",
                                    barmode="stack",  # "group" para barras separadas
                                    text="Cantidad")

                    # Mostrar en Streamlit
                    st.subheader("📊 Model Predictions for class 'YES'")
                    # st.plotly_chart(fig, use_container_width=True)
                    st.plotly_chart(fig)
                    
                if is_valid:
                    st.success("✅ Done!")

            except:
                st.error("Something happened", icon="🚨")
    
