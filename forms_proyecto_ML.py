with st.form("form_inicial"):

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
        submit_init              = st.form_submit_button("Evaluar inicio")

if submit_init:
    df_init = pd.DataFrame([{
        'is_enterprise' : is_enterprise,
        'has_roundA': has_roundA,
        'is_ecommerce': is_ecommerce, 
        'is_advertising': is_advertising, 
        'is_CA':    is_CA,
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


### STARTUPS FRACASADAS

with st.form("form_inicial"):
    giants = st.checkbox("¿Enfrenta competencia con los gigantes de tecnología?", value=False)
    no_budget = st.checkbox("¿Tiene suficiente presupuesto para continuar funcionando?", value=False)
    competition = st.checkbox("¿Enfrenta competencia directa intensa?", value=False)
    poor_market_fit = st.checkbox("¿Hay suficiente inetrés o demanda por su producto o servicio?", value=False)
    acquisition_stagnation = st.checkbox("¿Su empresa fue adquirida?¿Si lo fue, se estancó tras la adquisición?", value=False)
    platform_dependency = st.checkbox("¿Su empresa depende de una plataforma no propia?", value=False)
    monetization_failure = st.checkbox("¿Su empresa está logrando convertir los usuarios en ingresos?", value=False)
    niche_limits = st.checkbox("¿Su empresa está en un nicho muy limitado?", value=False)
    execution_flaws = st.checkbox("¿Su empresa tiene problemas de dirección, o técnicos?", value=False)
    trend_shifts = st.checkbox("¿Sus usuarios o clientes presentan una tendencia que los está alejando de su compañía?", value=False)
    toxicity = st.checkbox("¿Sus usuarios confían en sus productos/servicios y lo respaldan?", value=False)
    regulatory_issues = st.checkbox("¿Su empresa enfrenta problemas regulatorios?", value=False)
    overhyped = st.checkbox("¿Se tienen expectativas demasido altas sobre su compañia que son difíciles de cumplir?", value=False)

    # Transformar los checkboxes a 1 y 0
    giants = 1 if giants else 0
    no_budget = 1 if no_budget else 0
    competition = 1 if competition else 0
    poor_market_fit = 1 if poor_market_fit else 0
    acquisition_stagnation = 1 if acquisition_stagnation else 0
    platform_dependency = 1 if platform_dependency else 0
    monetization_failure = 1 if monetization_failure else 0
    niche_limits = 1 if niche_limits else 0
    execution_flaws = 1 if execution_flaws else 0
    trend_shifts = 1 if trend_shifts else 0
    toxicity = 1 if toxicity else 0
    regulatory_issues = 1 if regulatory_issues else 0
    overhyped = 1 if overhyped else 0

if submit_init:
    df_init = pd.DataFrame([{
        'giants' : giants,
        'no_budget': no_budget,
        'competition': competition, 
        'poor_market_fit': poor_market_fit, 
        'acquisition_stagnation': acquisition_stagnation,
        'platform_dependency': platform_dependency,
        'monetization_failure': monetization_failure,
        'niche_limits': niche_limits,
        'execution_flaws': execution_flaws,
        'trend_shifts': trend_shifts,
        'toxicity': toxicity,
        'regulatory_issues': regulatory_issues,
        'overhyped': overhyped
}])
      



### STARTUPS EXITOSAS

with st.form("form_inicial"):
	startup_age = st.number_input("¿Hace cuántos años fundó su empresa?", min_value=0, value=0)
	funding_amount = st.number_input("¿Cuál fue la inversión inicial en dólares?", min_value=1, value=1.0) # hay que aplicarle np.log1p antes de pasarlo por el modelo
	revenue = st.number_input("¿Cuántos ingresos genera en un mes en dólares?", min_value=1, value=1.0) # hay que aplicarle np.log1p antes de pasarlo por el modelo
	customer_retention_rate = st.number_input("¿Cuál es su porcentaje de retención de cliente de 0 a 100?", min_value=0, max_value=100)
	burn_amount = st.number_input("¿Cuánto dinero gasta por mes en dólares?", min_value=1, value=1.0) # No se usa en el modelo, pero se usa para el calculo de revenue_to_burn_ratio
	employees_count = st.number_input("¿Cuántos empleados tiene?", min_value=1, value=1) # hay que aplicarle np.log1p antes de pasarlo por el modelo
	industria = st.selectbox("¿A cuál industria pertence?", ['Manufacturing & Logistics', 'Education', 'Healthcare', 'Finance', 'Information & Tech'])
	
	# Transformaciones antes de pasar al pipeline
	funding = np.log1p(funding_amount)
	revenue = np.log1p(revenue)
	customer_retention_rate = customer_retention_rate / 100
	revenue_to_burn_ratio = np.log1p(revenue / (burn_amount+1))
	employees_count = np.log1p(employees_count)
	high_retention = 1 if customer_retention_rate > 0.8 else 0

if submit_init:
    df_init = pd.DataFrame([{
        'startup_age' : startup_age,
        'funding_amount': funding_amount,
        'revenue': revenue,
        'customer_retention_rate': customer_retention_rate,
        'revenue_to_burn_ratio': revenue_to_burn_ratio,
        'high_retention': high_retention,
        'employees_count': employees_count,
        'industry': industria
}])