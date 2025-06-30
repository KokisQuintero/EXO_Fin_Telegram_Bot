def buscar_moonshot():
    oportunidades = [
        {
            "symbol": "SMCI",
            "roi_estimado": 350,
            "catalizador": "Adquisición estratégica + demanda IA",
            "validacion_tecnica": "EMA crossover + volumen x3",
            "TP": 180,
            "SL": 85,
            "riesgo_beneficio": 4.6
        },
        {
            "symbol": "IOT",
            "roi_estimado": 290,
            "catalizador": "Resultados explosivos + upgrade de analistas",
            "validacion_tecnica": "Breakout con vela Marubozu",
            "TP": 78,
            "SL": 34,
            "riesgo_beneficio": 3.9
        },
    ]
    moonshots_validas = [o for o in oportunidades if o["roi_estimado"] >= 300 and o["riesgo_beneficio"] >= 4]
    return moonshots_validas[0] if moonshots_validas else "No hay oportunidades Moonshot sólidas hoy."
