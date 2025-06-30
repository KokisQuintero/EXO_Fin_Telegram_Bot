from external_apis import get_current_price
from modules.rotation_logic import suggest_rotation_logic

def recomendar_rotacion(portafolio):
    recomendaciones = []

    for posicion in portafolio:
        symbol = posicion["symbol"]
        quantity = posicion["quantity"]
        buy_price = posicion["price"]

        current_price = get_current_price(symbol)
        roi_actual = ((current_price - buy_price) / buy_price) * 100

        idea_mejor = suggest_rotation_logic(symbol, roi_actual)

        if idea_mejor and idea_mejor["roi_proyectado"] > roi_actual + 20:
            recomendaciones.append({
                "vender": symbol,
                "comprar": idea_mejor["symbol"],
                "roi_actual": round(roi_actual, 2),
                "roi_nuevo": idea_mejor["roi_proyectado"],
                "logica": idea_mejor["razon"]
            })

    return recomendaciones if recomendaciones else "No se detectaron rotaciones óptimas por ahora."
