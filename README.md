![EXO-FIN Banner](README_banner.png.png)

# EXO-FIN Telegram Bot – Sistema de Inversión Algorítmico

**EXO-FIN GPT** es un asistente de inversión algorítmico conectado a Telegram que te ayuda a rotar tu capital, analizar riesgos y detectar oportunidades con ROI explosivo, todo basado en datos reales y lógica adaptativa.

---

## 🧠 Funcionalidades Principales

- `/rotar` – Evalúa tu portafolio y sugiere rotación hacia activos con mejor ROI proyectado.
- `/riesgo SYMBOL CANTIDAD PRECIO` – Analiza el riesgo de una posición específica.
- `/moonshot` – Escanea el mercado global por una acción con ROI ≥ 300%.
- `/autocritica` – Analiza decisiones pasadas, identifica errores y sugiere ajustes futuros.

---

## 🚀 Instrucciones de Uso

1. **Instalá dependencias**
   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecutá el bot**
   ```bash
   python telegram_bot.py
   ```

3. **Interacción desde Telegram**
   - Enviá `/start` y luego cualquiera de los comandos disponibles.

---

## 🛠 Edición del Portafolio

Podés actualizar tu portafolio ejecutando:

```bash
python update_portfolio.py
```

Esto modificará automáticamente el archivo `utils.py` con tus nuevas posiciones.

---

## 🗃 Archivos Incluidos

- `telegram_bot.py` – Bot Telegram principal.
- `main_dispatcher.py` – Orquestador de lógica.
- `modules/` – Análisis de riesgo, rotación, moonshots y mejora continua.
- `external_apis.py` – Mock de datos de mercado.
- `logs/historial_operaciones.json` – Registro de decisiones pasadas.
- `update_portfolio.py` – Editor del portafolio.
- `run.bat` – Script de ejecución rápida en Windows.
- `requirements.txt` – Librerías necesarias.

---

## 📌 Requisitos

- Python 3.10+
- Cuenta de Telegram con bot creado
- Token y Chat ID configurados en `telegram_bot.py`

---

## 📈 Visión

Construido para lograr una **rentabilidad de 1000% anual** con disciplina, automatización y lógica evolutiva. Ideal para traders con perfil técnico y objetivos exponenciales.

---

Desarrollado por Carlos Andrés Quintero Ocampo – Australia 🇦🇺 | Operando desde CommSec
