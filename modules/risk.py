def evaluar_riesgo(symbol: str, quantity: int, price: float) -> dict:
    exposicion = round(quantity * price, 2)
    riesgo_base = "Alto" if symbol.upper() in ["RIOT", "APLD", "MARA"] else "Moderado"

    if exposicion > 5000:
        riesgo_base = "Crítico"
    elif exposicion < 1000:
        riesgo_base = "Bajo"

    return {
        "activo": symbol,
        "cantidad": quantity,
        "precio_compra": price,
        "exposicion_total": exposicion,
        "riesgo_estimado": riesgo_base,
        "logica": "Basado en exposición y tipo de activo"
    }
