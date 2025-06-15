from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum! Men ishlayapman!")

app = ApplicationBuilder().token("8078911806:AAHxbUbazJVRF67M_OmZcm9WOlVAllfvB7k").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()