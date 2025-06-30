from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from main_dispatcher import ejecutar_comando

import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise Exception("❌ BOT_TOKEN no encontrado. Revisa tus variables de entorno en Railway.")
CHAT_ID = os.getenv("CHAT_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 EXO-FIN está listo. Usa /rotar, /riesgo, /moonshot o /autocritica")

async def rotar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resultado = ejecutar_comando("/rotar")
    await update.message.reply_text(str(resultado))

async def moonshot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resultado = ejecutar_comando("/moonshot")
    await update.message.reply_text(str(resultado))

async def autocritica(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resultado = ejecutar_comando("/autocritica")
    await update.message.reply_text(str(resultado))

async def riesgo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        args = context.args
        symbol = args[0].upper()
        quantity = int(args[1])
        price = float(args[2])
        resultado = ejecutar_comando("/riesgo", {"symbol": symbol, "quantity": quantity, "price": price})
        await update.message.reply_text(str(resultado))
    except (IndexError, ValueError):
        await update.message.reply_text("Uso: /riesgo SYMBOL CANTIDAD PRECIO\nEjemplo: /riesgo RIOT 35 8.80")

if __name__ == '__main__':
    import os
    from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise Exception("❌ BOT_TOKEN no encontrado. Revisa tus variables de entorno en Railway.")
    print("🤖 Bot activo...")

def main():
    from telegram.ext import ApplicationBuilder
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("rotar", rotar))
    app.add_handler(CommandHandler("moonshot", moonshot))
    app.add_handler(CommandHandler("autocritica", autocritica))
    app.add_handler(CommandHandler("riesgo", riesgo))

    app.run_polling()
