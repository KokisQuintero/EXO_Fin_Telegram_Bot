import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
import asyncio
from telegram_bot import main as start_telegram_bot

if __name__ == "__main__":
    asyncio.run(start_telegram_bot())
