# update_portfolio.py – Editor rápido del portafolio actual

import json
import os

PORTAFOLIO_PATH = "modules/utils.py"

def actualizar_portafolio():
    portafolio = []
    print("🧾 Ingrese los datos de cada posición (ENTER para finalizar):")

    while True:
        symbol = input("Símbolo (ej: RIOT): ").strip().upper()
        if not symbol:
            break
        quantity = int(input("Cantidad: "))
        price = float(input("Precio de compra: "))
        portafolio.append({"symbol": symbol, "quantity": quantity, "price": price})

    with open(PORTAFOLIO_PATH, "w", encoding="utf-8") as f:
        f.write("# modules/utils.py – Herramientas de soporte para el sistema EXO-FIN\n\n")
        f.write("def obtener_portafolio_actual():\n")
        f.write("    return " + json.dumps(portafolio, indent=4).replace("true", "True").replace("false", "False"))

    print("✅ Portafolio actualizado correctamente en utils.py")

if __name__ == "__main__":
    actualizar_portafolio()
