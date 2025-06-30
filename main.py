import os
import sys
import asyncio

# Añadir carpeta 'modules' al path para imports personalizados
MODULES_PATH = os.path.join(os.path.dirname(__file__), 'modules')
if MODULES_PATH not in sys.path:
    sys.path.append(MODULES_PATH)

try:
    from telegram_bot import main as start_telegram_bot
except ImportError as e:
    print("❌ Error al importar el bot de Telegram:", e)
    sys.exit(1)

async def launch_bot():
    print("🚀 Iniciando EXO_Fin_Telegram_Bot...")
    try:
        await start_telegram_bot()
        print("✅ Bot ejecutado correctamente.")
    except Exception as e:
        print("❌ Ocurrió un error al ejecutar el bot:", e)

if __name__ == "__main__":
    asyncio.run(launch_bot())