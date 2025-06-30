import os
from telegram import Bot
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
bot = Bot(token=BOT_TOKEN)

app = FastAPI()

class ComandoInput(BaseModel):
    comando: str
    parametros: str = ""

@app.post("/enviar_comando")
def enviar_comando(data: ComandoInput):
    mensaje = f"{data.comando} {data.parametros}".strip()
    bot.send_message(chat_id=CHAT_ID, text=mensaje)
    return {"status": "OK", "mensaje_enviado": mensaje}
