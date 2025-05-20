import streamlit as st
import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer

def prepare_input(df, pipeline):
    ct = next(step for step in pipeline.named_steps.values() if isinstance(step, ColumnTransformer))
    return df.reindex(columns=ct.feature_names_in_)

model_success = joblib.load("dfRegresion.joblib")
model_anom     = joblib.load("df4IsolationForest.joblib")
model_fail     = joblib.load("df5OneClassSVM.joblib")




st.set_page_config(page_title="Evaluación de tu Startup", layout="centered")
st.title("🚀 Evaluación Interactiva de Startups")

with st.form("form_inicial"):
    age_first_funding_year = st.number_input("Años desde primera ronda de financiación", min_value=0.0, value=1.0)
    age_last_funding_year  = st.number_input("Años desde última ronda de financiación", min_value=0.0, value=0.0)
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
    
    df_init_pre = prepare_input(df_init, model_success)
    label_success = model_success.predict(df_init_pre)[0]
    if label_success == 1:
        st.success("✅ Tu startup va por buen camino")



    
        with st.form("form_anom"):
            Startup_Name             = st.text_input("Nombre de la startup", value="MiStartup")
            Industry                 = st.text_input("Industria (texto libre)", value="tech")
            Funding_Amount           = st.number_input("Monto de última ronda (USD)", min_value=0.0, value=50000.0)
            Number_of_Founders       = st.number_input("Número de fundadores", min_value=1, value=2)
            Founder_Experience       = st.number_input("Años de experiencia promedio de fundadores", min_value=0.0, value=5.0)
            Employees_Count          = st.number_input("Número de empleados", min_value=1, value=10)
            Revenue                  = st.number_input("Ingresos anuales (USD)", min_value=0.0, value=100000.0)
            Burn_Rate                = st.number_input("Tasa de quema mensual (USD)", min_value=0.0, value=10000.0)
            Market_Size              = st.number_input("Tamaño de mercado estimado (USD)", min_value=0.0, value=1000000.0)
            Business_Model           = st.text_input("Modelo de negocio", value="B2B")
            Product_Uniqueness_Score = st.number_input("Puntaje de unicidad de producto (0-10)", min_value=0, max_value=10, value=7)
            Customer_Retention_Rate  = st.number_input("Tasa de retención de clientes (%)", min_value=0.0, max_value=100.0, value=80.0)
            Marketing_Expense        = st.number_input("Gasto en marketing anual (USD)", min_value=0.0, value=20000.0)
            Startup_Status           = st.selectbox("Estado actual", ["operando", "crecimiento", "pivot"])
            submit_anom              = st.form_submit_button("Analizar anomalías")
        if submit_anom:
            df_anom      = pd.DataFrame([{
                "Startup_Name":             Startup_Name,
                "Industry":                 Industry,
                "Funding_Amount":           Funding_Amount,
                "Number_of_Founders":       Number_of_Founders,
                "Founder_Experience":       Founder_Experience,
                "Employees_Count":          Employees_Count,
                "Revenue":                  Revenue,
                "Burn_Rate":                Burn_Rate,
                "Market_Size":              Market_Size,
                "Business_Model":           Business_Model,
                "Product_Uniqueness_Score": Product_Uniqueness_Score,
                "Customer_Retention_Rate":  Customer_Retention_Rate,
                "Marketing_Expense":        Marketing_Expense,
                "Startup_Status":           Startup_Status
            }])
            df_anom_pre = prepare_input(df_anom, model_anom)
            label_anom  = model_anom.predict(df_anom_pre)[0]
            if label_anom == 1:
                st.success("🎉 No es anomalía.")
            else:
                st.warning("⚠️ Es anomalía.")
    else:
        st.error("🚨 Tu startup podría estar en riesgo")
        with st.form("form_fail"):
            plat        = st.checkbox("Dependencia de Plataforma")
            pres        = st.checkbox("Sin Presupuesto")
            market      = st.checkbox("Mala Adecuación al Mercado")
            regul       = st.checkbox("Presión Regulatoria")
            comp        = st.checkbox("Competencia")
            monet       = st.checkbox("Fallo en Monetización")
            trend       = st.checkbox("Cambios de Tendencias")
            submit_fail = st.form_submit_button("Analizar riesgo")
        if submit_fail:
            df_fail      = pd.DataFrame([{
                "dependency_platform":   int(plat),
                "no_budget":             int(pres),
                "poor_market_fit":       int(market),
                "regulatory_pressure":   int(regul),
                "competition":           int(comp),
                "monetization_failure":  int(monet),
                "trend_changes":         int(trend)
            }])
            df_fail_pre  = prepare_input(df_fail, model_fail)
            label_fail   = model_fail.predict(df_fail_pre)[0]
            if label_fail == 1:
                st.error("🚨 Alta probabilidad de fracaso.")
            else:
                st.info("⚠️ Riesgo moderado.")
