from modules.rotator import recomendar_rotacion
from modules.risk import evaluar_riesgo
from modules.moonshot import buscar_moonshot
from modules.autocritic import ejecutar_autocritica
from modules.utils import obtener_portafolio_actual

def ejecutar_comando(comando: str, argumentos: dict = None):
    if comando == "/rotar":
        portafolio = obtener_portafolio_actual()
        return recomendar_rotacion(portafolio)

    elif comando == "/riesgo":
        symbol = argumentos.get("symbol")
        quantity = argumentos.get("quantity")
        price = argumentos.get("price")
        return evaluar_riesgo(symbol, quantity, price)

    elif comando == "/moonshot":
        return buscar_moonshot()

    elif comando == "/autocritica":
        return ejecutar_autocritica()

    else:
        return "Comando no reconocido. Intenta con /rotar, /riesgo, /moonshot o /autocritica."

if __name__ == "__main__":
    resultado = ejecutar_comando("/rotar")
    print(resultado)
