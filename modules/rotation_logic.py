def suggest_rotation_logic(current_symbol, current_roi):
    ideas_disponibles = [
        {"symbol": "NVDA", "roi_proyectado": 150, "razon": "Breakout post earnings con alto volumen"},
        {"symbol": "MARA", "roi_proyectado": 120, "razon": "Correlación con BTC + impulso técnico"},
        {"symbol": "TSLA", "roi_proyectado": 80, "razon": "Catalizador macro + rebote técnico"},
        {"symbol": "META", "roi_proyectado": 60, "razon": "Buyback y mejora en márgenes"},
    ]

    mejores = [idea for idea in ideas_disponibles if idea["roi_proyectado"] > current_roi + 20 and idea["symbol"] != current_symbol]
    return mejores[0] if mejores else None
