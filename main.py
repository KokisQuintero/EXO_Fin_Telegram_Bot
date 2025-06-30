import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from telegram_bot import main as start_telegram_bot

if __name__ == "__main__":
    print("🚀 Iniciando EXO_Fin_Telegram_Bot...")
    start_telegram_bot()
