import random

def get_current_price(symbol):
    precios_mock = {
        "RIOT": 9.25,
        "APLD": 11.10,
        "CMM": 6.10,
        "ZIP": 2.90,
    }
    return precios_mock.get(symbol.upper(), round(random.uniform(5, 20), 2))
