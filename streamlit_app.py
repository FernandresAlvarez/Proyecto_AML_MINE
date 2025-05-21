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
tab1, tab2, tab3, tab4 = st.tabs(["Random Forest", "Clusterización", "OneClassSVM", "MLPRegressor"])
#tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Random Forest", "Clusterización", "OneClassSVM", "MLPRegressor", "Start-Up State", "Stats"])



### My UI starting here
with tab1:
    
    with st.form("form_ModeloA"):

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

                df_init_RF = pd.DataFrame([{
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

                RF_df = ctrl.predict_RF(df_init_RF)
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


with tab2:
    with st.form("form_Cluster"):
        st.markdown("#### Selecciona las razones de fallo que aplican a tu startup:")

        giants                  = st.checkbox("¿Enfrenta competencia con los gigantes de tecnología?", value=False)
        acquisition_stagnation  = st.checkbox("¿Su empresa fue adquirida y se estancó tras la adquisición?", value=False)
        platform_dependency     = st.checkbox("¿Su empresa depende de una plataforma no propia?", value=False)
        execution_flaws         = st.checkbox("¿Su empresa tiene problemas de dirección o técnicos?", value=False)
        monetization_failure    = st.checkbox("¿Logra convertir suficientes usuarios en ingresos?", value=False)
        niche_limits            = st.checkbox("¿Está en un nicho muy limitado?", value=False)
        overhyped               = st.checkbox("¿Se tienen expectativas demasiado altas sobre su compañía?", value=False)
        regulatory_issues       = st.checkbox("¿Enfrenta problemas regulatorios?", value=False)
        poor_market_fit         = st.checkbox("¿Hay suficiente demanda por su producto o servicio?", value=False)
        no_budget               = st.checkbox("¿Cuenta con presupuesto suficiente para continuar?", value=False)
        trend_shifts            = st.checkbox("¿Sus usuarios presentan tendencias que los alejan de la compañía?", value=False)
        competition             = st.checkbox("¿Enfrenta competencia directa intensa?", value=False)
        toxicity                = st.checkbox("¿Sus usuarios confían en sus productos y lo respaldan?", value=False)

        submit_cluster = st.form_submit_button("Ejecutar clustering")

        if submit_cluster:
            # Construimos el DataFrame 1/0
            df_init = pd.DataFrame([{
                'Giants':                   int(giants),
                'Acquisition Stagnation':   int(acquisition_stagnation),
                'Platform Dependency':      int(platform_dependency),
                'Execution Flaws':          int(execution_flaws),
                'Monetization Failure':     int(monetization_failure),
                'Niche Limits':             int(niche_limits),
                'Overhype':                 int(overhyped),
                'Regulatory Pressure':      int(regulatory_issues),
                'Poor Market Fit':          int(poor_market_fit),
                'No Budget':                int(no_budget),
                'Trend Shifts':             int(trend_shifts),
                'Competition':              int(competition),
                'Toxicity/Trust Issues':    int(toxicity)
            }])

            # Predicción MeanShift y Decision Tree
            ms_df, ms_labels = ctrl.predict_ms(df_init)
            dt_df, dt_labels = ctrl.predict_dt(df_init)

            # Mostrar resultados
            st.subheader("🔍 Resultados de Clusterización")
            st.dataframe(ms_df.assign(Cluster_DT=dt_labels))

            # Mensajes
            st.info(f"📌 Fue asignado al cluster {ms_labels[0]} según MeanShift.")
            if dt_labels[0] == 1:
                st.error("🚨 Según el árbol de decisión, la probabilidad de fracaso es ALTA.")
            else:
                st.warning("⚠️ Según el árbol de decisión, la probabilidad de fracaso es MODERADA.")






with tab3:
    with st.form("form_SVM"):
        st.markdown("#### Ingresa los datos para OneClassSVM:")

        industry                = st.selectbox("Industry", ctrl.get_svm_industries())
        startup_age             = st.number_input("Startup Age", min_value=0.0, value=8.0)
        funding_amount          = st.number_input("Funding Amount", min_value=0.0, value=1e7)
        revenue                 = st.number_input("Revenue", min_value=0.0, value=5e6)
        cust_ret_rate           = st.number_input("Customer Retention Rate", min_value=0.0, max_value=1.0, value=0.8)
        rev_to_burn_ratio       = st.number_input("Revenue to Burn Ratio", min_value=0.0, value=5.0)
        employees_count         = st.number_input("Employees Count", min_value=0.0, value=50.0)
        high_retention          = st.selectbox("High Retention (1=Sí, 0=No)", [1, 0])

        submit_svm = st.form_submit_button("Evaluar SVM")

        if submit_svm:
            df_svm = pd.DataFrame([{
                'Industry':                    industry,
                'Startup_Age':                 startup_age,
                'Funding_Amount':              funding_amount,
                'Revenue':                     revenue,
                'Customer_Retention_Rate':     cust_ret_rate,
                'Revenue_to_Burn_Ratio':       rev_to_burn_ratio,
                'Employees_Count':             employees_count,
                'High_Retention':              high_retention
            }])

            svm_df, svm_labels = ctrl.predict_ocsvm(df_svm)

            st.subheader("🔍 Resultados OneClassSVM")
            st.dataframe(svm_df)

            # Interpretación de 1 / -1
            if svm_labels[0] == 1:
                st.success("✅ Alta probabilidad de éxito")
            else:
                st.info("ℹ️ Probabilidad moderada de éxito")


with tab4:

    with st.form("form MLPRegressor"):

        ranking = st.number_input("Ranking de la empresa", min_value = 0, value=0)
        temp_ranking = st.number_input("Ranking temporal de la empresa", min_value = 0, value=0)
        previous_ranking = st.number_input("Ranking anterior de la empresa", min_value = 0, value=0)
        city = st.selectbox("¿En cuál ciudad se encuentra la empresa?", ['San Francisco', 'New York', 'London', 'Palo Alto', 'Toronto', 'Los Angeles', 'Boston', 'Austin', 'Miami', 'Mountain View', 'Cambridge', 'San Diego', 'Dallas', 'Atlanta', 'Washington', 'Seattle', 'Brooklyn', 'Oakland', 'Houston', 'San Jose', 'Chicago', 'Tel Aviv', 'Cleveland', 'Boulder', 'Minneapolis', 'Berkeley', 'Santa Monica', 'Santa Clara', 'Vancouver', 'Bellevue', 'Bangalore', 'Menlo Park', 'Jacksonville', 'Los Altos', 'McLean', 'Stockholm', 'Fremont', 'Berlin', 'Denver', 'Sunnyvale', 'Paris', 'Nashville', 'Calgary', 'Singapore', 'Ventura', 'Phoenix', 'Ann Arbor', 'Durham', 'Arlington', 'Louisville', 'Pasadena', 'Columbia', 'Orlando', 'Salt Lake City', 'Raleigh', 'Redwood City', 'Wilmington', 'Detroit', 'Somerville', 'Saratoga', 'San Mateo', 'Incline Village', 'Baltimore', 'Boca Raton', 'Torrance', 'Waltham', 'Kirkland', 'Concord', 'Pittsburgh', 'Herndon', 'Montreal', 'San Antonio', 'Carmel', 'Sao Paulo', 'Amsterdam', 'Omaha', 'Las Vegas', 'Melbourne', 'Portland', 'Conshohocken', 'Newport Beach', 'Hayward', 'Warren', 'Oslo', 'Lincoln', 'Victoria', 'Tampa', 'Charlottesville', 'Bethesda', 'Netanya', 'Richmond', 'Woburn', 'Ellicott City', 'Scottsdale', 'Chertsey', 'Easton', 'Ridgeland', 'Great Neck', 'Milan', 'Bloomington', 'Ottawa', 'Teaneck', 'Florham Park', 'George Town', 'Hamburg', 'Mortsel', 'Seal Beach', 'Jacksonville Beach', 'Gurgaon', 'Cincinnati', 'Belgrade', 'Linthicum', 'Novato', 'Longmont', 'Little Rock', 'Midland', 'St Louis', 'Cupertino', 'Costa Mesa', 'Las Cruces', 'Broomfield', 'Indore', 'New Philadelphia', 'Thornton', 'Orem', 'Markham', 'Tempe', 'Allentown', 'Merritt Island', 'Evanston', 'Arcadia', "Coeur d'Alene", 'Saint-Ouen', 'Sahibganj', 'Hunt Valley', 'Everett', 'Cheyenne', 'Brisbane City', 'Venice', 'Palm Beach Gardens', 'Sioux Falls', 'Gilbert', 'Farmington Hills', 'Port Townsend', 'NYC', 'Walnut', 'Maitland', 'USA', 'Stratford', 'Overland Park', 'Culver City', 'Zelienople', 'Kent', 'Helsinki', 'Rugby', 'Roxboro', 'State College', 'Iowa City', 'Remote First', 'Silicon Beach', 'Buffalo', 'Solana Beach', 'Collierville', 'Ithaca', 'Carrollton', 'lewisville', 'Remote', 'Hutchinson', 'Fairport', 'Texas', 'Winter Park', 'Stanton', 'Warwick', 'Lakeland North', 'Tysons', 'Ashby de la Zouch', 'Shelton', 'Ferndale', 'Valencia', 'Warszawa', 'Thomaston', 'Mill Valley', 'Grapevine', 'Doswell', 'Seguin', 'Utica', 'Brentwood', 'Albuquerque', 'North Kansas City', 'Newton', 'Rock Hill', 'Pune', 'Emeryville', 'Southfield', 'Carterville', 'Fort Myers', 'Harwell', 'Sacramento', 'Elysburg', 'Newark', 'Indianapolis', 'Santiago', 'Greater Boston', 'Hollywood', 'Englewood', 'Connaught Place', 'Beijing', 'Milton Keynes', 'Noida', 'Stanford', 'Lehi', 'Berkeley Heights', 'Rancho Cordova', 'Mumbai ', 'Campbell', 'Stafford', 'Wekiwa Springs', 'Jupiter', 'Burlington', 'Grand Rapids', 'Cumming', 'Indio', 'Reno', 'Columbus', 'Milpitas', 'Santa Ana', 'Vienna', 'Seocho', 'Munich', 'Santa Barbara', 'Winchester', 'Skokie', 'Lander', 'Harrisonburg', 'Albany', 'Hawthorne', 'Abu Dhabi', 'Pawtucket', 'Provo', 'Camana Bay', 'Auburn', 'Johannesburg', 'Foster City', 'FLORHAM PARK', 'Miami ', 'Huger', 'Edmonton', 'Natick', 'Howell', 'Manhasset', 'Walnut Creek', 'Woodinville', 'Tashkent', 'West Hollywood', 'Lyon', 'Croix', 'Distributed', 'Westerville', 'Washington D.C.', 'West End', 'Flemington', 'Wolf Trap', 'Castlebar', 'Hollister', 'Limassol', 'Seoul', 'Schenectady', 'Brea', 'Tunbridge Wells ', 'Jefferson', 'West Jordan', 'Hauppauge', 'Aliso Viejo', 'Ghaziabad', 'Stamford', 'Irvine', 'Beverly', 'Lowell', 'Immokalee', 'NEW YORK', 'Fort Washington', 'Battle Creek', 'Hamilton', 'Espoo', 'Delhi', 'London W1W 5PE.', 'Groton', 'Chennai', 'Jersey City', 'San Marcos', 'Milton', 'Greenville', 'Canton', 'Fort Lauderdale', 'Burnaby', 'Norfolk', 'West Mifflin', 'Lansing', 'Carlsbad', 'Donnelly', 'Cabazon', 'Coral Gables', 'Oakdale', 'Gainesville', 'Dayton', 'Falls Church', 'South Burlington', 'Irving', 'Lafayette', 'Grand Cayman', 'Hillsborough', 'Dublin City', 'Milford', 'Philadelphia', 'Tampere', 'Giza', 'Manchester', 'Birmingham', 'San Clemente', 'San Franscisco', 'Brookline', 'Doral', 'Madrid', 'Carson City', 'Reading', 'Penryn', 'Beaverton', 'Vaduz', 'Lagos'])        
        country = st.selectbox("¿En cuál país se encuentra la empresa?", ['United States', 'UK', 'USA', 'CAN', 'Israel', 'IND', 'Germany', 'France', 'SWE', 'SGP', 'ind', 'aus', 'Cayman Islands', 'South Korea', 'Norway', 'Brazil', 'Netherlands', 'Ger', 'United Arab Emirates', 'Egypt', 'China', 'Hong Kong', 'Fra', 'Cyprus', 'Uzbekistan', 'Nigeria', 'Ireland', 'FI', 'Liechtenstein', 'Denmark', 'New Zealand', 'Spain', 'Ind', 'fin', 'Aus', 'FRA', 'Canada', 'bel', 'Chile', 'POL', 'uk', 'net', 'Grenada', 'South Africa'])
        state = st.selectbox("¿En cuál estado se encuentra la empresa?", ['CA', 'NY', 'TX', 'MA', 'FL', 'WA', 'VA', 'ON', 'CO', 'OH', 'MI', 'IL', 'GA', 'MD', 'PA', 'DC', 'MN', 'NC', 'NJ', 'TN', 'NV', 'UT', 'BC', 'AZ', 'AB', 'IN', 'OR', 'SC', 'NM', 'London', 'CT', 'NE', 'MO', 'ID', 'UK', 'LA', 'QC', 'MT', 'DE', 'WY', 'Maharashtra', 'AR', 'KY', 'VT', 'Ile de France', 'Ca', 'Surrey', 'Great Neck', 'Greater London', 'Woj. Mazowieckie', 'SD', 'MS', 'SP', 'England', 'RI', 'KS', 'Camana Bay', 'AL', 'Washington D.C.', 'IA'])
        current_employees = st.number_input("Número actual de empleados", min_value = 0, value=1)
        employee_growth = st.number_input("Crecimiento de empleados", min_value = 0, value=1)
        total_funding = st.number_input("Fondos totales", min_value = 0, value=2)
        Industry = st.selectbox("¿En cuál industria se encuentra la empresa?", ['Tech Services', 'Fintech', 'AI', 'Environmental', 'Finance', 'IT Security', 'Software', 'Analytics', 'Hospital/Healthcare', 'Digital Health', 'Biotech', 'Insurance', 'Electronics', 'Food', 'Medical Equip', 'Automotive', 'Aviation', 'HRTech', 'Energy', 'Real Estate', 'Investments', 'Entertainment', 'Mining', 'DevOps', 'Telecom', '3D', 'Health', 'Utilities', 'Hospitality', 'Construction', 'Industrial', 'Consumer', 'Martech', 'Transportation', 'NonProfit', 'Engineering', 'EdTech', 'Hardware', 'Research', 'Energy/Oil', 'Media', 'Retail', 'Edtech', 'Casinos', 'Marketing', 'Consulting', 'Defense', 'Logistics', 'SaaS', 'Security', 'Education', 'Wireless', 'Recruiting', 'eCommerceTech', 'Technology, Information and Internet', 'Advertising', 'Pharma', 'Babytech', 'Farming', 'Computer and Network Security', 'Restaurants', 'Technology', 'Maritime', 'Accounting', 'Robotics', 'Adtech', 'Semiconductors', 'Sports', 'Aviatioon', 'Veterinary', 'Chemicals', 'Manufacturing', 'Medical', 'Business Intelligence', 'Chemical Manufacturing', 'Gaming', 'Apparel', 'HR', 'VR', 'eCommerce', 'Facilities', 'Information Technology', 'Social Services', 'Medical Offices', 'Materials', 'Health, Wellness & Fitness', 'Machinery', 'Support/CRM Tech', 'Banking', 'Leisure', 'Leasing Real Estate', 'Cosmetics', 'Hospital/Health', 'Research Services', 'Cloud', 'Blockchain', 'Healthcare', 'Real Estate Tech', 'E-Learning Providers', 'Legaltech', 'Foodtech', 'Information Technology & Services', 'DeliveryTech', 'Retail Health and Personal Care Products', 'Events', 'Computers and Electronics Manufacturing', 'AdTech', 'LegalTech', 'Networking', 'BabyTech', 'Services for Renewable Energy', 'Outsourcing and Offshoring Consulting', 'Design', 'Think Tanks', 'Investment Banks', 'Furniture and Home Furnishings Manufacturing', 'IoT', 'Executive', 'Supplies', 'Oil and Gas', 'Wholesale Building Materials', 'Outsource', 'Travel Arrangements', 'Cannabis', 'ProductivityTech', 'Clean Tech', 'Legal', 'Recreation', 'Nonprofit', 'Professional Training and Coaching', 'Printing Services', 'HRtech', 'Gambling Facilities and Casinos', 'Publishing', 'Airlines and Aviation', 'Plastics', 'Fitness', 'Venture Capital and Private Equity Principals', 'Spectator Sports', 'Cryptocurrency', 'Music', 'Computer Networking Products', 'Trucking', 'Retail Luxury Goods and Jewelry', 'Event Tech'])
        Points = st.number_input("Número de puntos de la empresa", min_value = 0, value=5)
        valuation = st.number_input("Ingresos en USD de la empresa", min_value =0.0, value=1000.0)
        best_score = st.number_input("Mejor puntuación de la empresa", min_value = 0, value=0)
        #match_score = st.number_input("Puntuación de partida de la empresa", min_value = 0, value=0)
        score_category = st.selectbox("¿En cuál categoría se encuentra la empresa?", ['Dudosa (70-84)', 'Buena (85-94)', 'Excelente (95-100)', 'No Match (<70)'])



        submit_init_MLPR = st.form_submit_button("Evaluar inicio")

        try: 
            if submit_init_MLPR:

                df_init_MLPR = pd.DataFrame([{
                    'ranking': ranking,
                    'temp_ranking':temp_ranking,
                    'previous_ranking':previous_ranking,
                    'city':city,
                    'country':country,
                    'state':state,
                    'current_employees':current_employees,
                    'employee_growth':employee_growth,
                    'total_funding':total_funding,
                    'Industry':Industry,
                    'Points':Points,
                    'valuation':valuation,
                    'best_score':best_score,
                    'score_category':score_category,
                }])

                MLPR_df = ctrl.predict_MLPRegressor(df_init_MLPR)
                
                st.subheader("🔍 Predicciones realizadas")
                st.dataframe(MLPR_df[0])

                st.success(f"✅ Start Up con una valoración de: {MLPR_df[1][0]} USD")
            
        except:
            st.error("Something happened", icon="🚨")

    # Tener presentes predicts de cada modelo para presentar resultado final

