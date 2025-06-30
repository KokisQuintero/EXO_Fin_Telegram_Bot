# modules/autocritic.py – MVP de Autocrítica Inteligente

import json
import os

HISTORIAL_PATH = "logs/historial_operaciones.json"

def cargar_historial():
    if not os.path.exists(HISTORIAL_PATH):
        return []
    with open(HISTORIAL_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def evaluar_resultados(historial):
    errores = []
    aciertos = []

    for operacion in historial:
        roi = operacion.get("roi", 0)
        razon = operacion.get("razon", "")
        simbolo = operacion.get("symbol", "?")

        if roi < 0:
            errores.append((simbolo, roi, razon))
        else:
            aciertos.append((simbolo, roi, razon))

    return aciertos, errores

def sugerencias_mejora(errores):
    insights = []
    for simbolo, roi, razon in errores:
        if "volumen" in razon.lower():
            insights.append(f"🔍 Evitar operar {simbolo} sin validación de volumen claro.")
        if "timing" in razon.lower() or roi < -15:
            insights.append(f"⏱ Revisar timing de entrada en {simbolo}. Quizás fue apresurada.")
        if "sin catalizador" in razon.lower():
            insights.append(f"🚫 No operar {simbolo} sin catalizador fundamental verificable.")

    return insights if insights else ["✅ No se detectaron errores críticos en operaciones pasadas."]

def ejecutar_autocritica():
    historial = cargar_historial()
    if not historial:
        return "ℹ️ No hay historial de operaciones para analizar aún."

    aciertos, errores = evaluar_resultados(historial)
    insights = sugerencias_mejora(errores)

    resumen = f"📈 Aciertos: {len(aciertos)} | 📉 Errores: {len(errores)}\n\n"
    resumen += "\n".join(insights)
    return resumen
