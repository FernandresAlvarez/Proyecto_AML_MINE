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


### My vars
ctrl = ModelController()


# Presentamos la inforamción de forma tabulada o pestañas
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Random Forest", "MeanShift", "Decision Tree", "OneClassSVM", "MLPRegressor", "Start-Up State", "Stats"])



### My UI starting here

with tab1:
        
    st.form("form_ModeloA")

    is_enterprise= st.selectbox("¿Es empresa?", [1, 0])
    has_roundA= st.selectbox("¿Tiene ronda A?", [1, 0])
    is_ecommerce= st.selectbox("¿Es E-commerce?", [1, 0])
    is_advertising= st.selectbox("¿Es publicidad?", [1, 0])
    is_CA= st.selectbox("¿Es CA?", [1, 0])
    is_MA= st.selectbox("¿Es MA?", [1, 0])
    has_roundD= st.selectbox("¿Tiene ronda D?", [1, 0])
    is_mobile= st.selectbox("¿Es mobile?", [1, 0])
    is_top500= st.selectbox("¿Top 500?", [1, 0])
    is_TX= st.selectbox("¿Es TX?", [1, 0])
    avg_participants= st.number_input("Participantes promedio", min_value = 0, value=1)
    milestones= st.number_input("Número de rondas de fondos", min_value = 0, value=2)
    is_software= st.selectbox("¿Es de software?", [1, 0])
    is_web= st.selectbox("¿Es web?", [1, 0])
    category_code= st.selectbox("Categoría", ['software', 'web', 'mobile', 'enterprise', 'advertising', 'games_video', 'semiconductor', 'biotech', 'network_hosting', 'hardware', 'public_relations', 'ecommerce', 'cleantech', 'analytics', 'security', 'social', 'search', 'messaging', 'other', 'news', 'travel', 'fashion', 'photo_video', 'medical', 'music', 'finance', 'education', 'real_estate', 'consulting', 'health', 'automotive', 'transportation', 'manufacturing', 'hospitality', 'sports'])
    is_consulting= st.selectbox("¿Consulta?", [1, 0])
    is_otherstate= st.selectbox("¿Es de otro estado?", [1, 0])
    is_gamesvideo= st.selectbox("¿Es de videojuegos?", [1, 0])
    relationships= st.number_input("Número de relaciones", min_value=0, value=1)
    funding_total_usd= st.number_input("Fondos Totales en USD", min_value=0.0, value=1000.0)
    has_angel= st.selectbox("¿Tiene angel?", [1, 0])
    has_roundB= st.selectbox("¿Tiene ronda B?", [1, 0])
    has_VC= st.selectbox("¿Tiene VC?", [1, 0])
    is_biotech= st.selectbox("¿Es de biotecnología?", [1, 0])
    #labels= st.selectbox("¿Adquirida o cerrada?", [1, 0])
    has_roundC= st.selectbox("¿Tiene ronda C?", [1, 0])
    is_othercategory= st.selectbox("¿Es de otra categoría?", [1, 0])
    funding_rounds= st.number_input("Número de rondas de fondos", min_value=0, value=1)
    is_NY = st.selectbox("¿Es de NY?", [1, 0])
    submit_init_RF = st.form_submit_button("Evaluar inicio")

    try: 
        if submit_init_RF:

            df_init = pd.DataFrame([{
                'is_enterprise' : is_enterprise,
                'has_roundA': has_roundA,
                'is_ecommerce': is_ecommerce, 
                'is_advertising': is_advertising, 
                'is_CA': is_CA,
                'is_MA': is_MA,
                'has_roundD': has_roundD,
                'is_mobile': is_mobile,
                'is_top500': is_top500,
                'is_TX': is_TX,
                'avg_participants': avg_participants,
                'milestones': milestones,
                'is_software': is_software,
                'is_web': is_web,
                'category_code': category_code,
                'is_consulting': is_consulting,
                'is_otherstate': is_otherstate,
                'is_gamesvideo': is_gamesvideo,
                'relationships': relationships,
                'funding_total_usd': funding_total_usd,
                'has_angel': has_angel,
                'has_roundB': has_roundB,
                'has_VC': has_VC,
                'is_biotech': is_biotech,
                'has_roundC': has_roundC,
                'is_othercategory': is_othercategory,
                'funding_rounds': funding_rounds,
                'is_NY': is_NY        
            }])

            RF_df = ctrl.predict(df_init)
            #print(RF_df)
            #RF_df, MS_df, DT_df, OCSVM_df, MLPR_df = ctrl.predict()
            #FinalPred = ctrl.final_pred() #Tupla para incluir mensaje, imagen y valorización de start up, si fue exitosa
            #TODO

            
            #print(RF_df)
            st.subheader("🔍 Predicciones realizadas")
            #print(RF_df)
            st.dataframe(RF_df[0])

            if RF_df[1] == 1:
                st.success("✅ Start Up probablemente exitosa")
            else:
                st.warning("🚨 Start Up probablemente en riesgo")
    except:
        st.error("Something happened", icon="🚨")





    





