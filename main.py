from telegram.ext import Application, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

TOKEN = "8655114606:AAGB0NJCi1edimgo1KDEN5URYrWnrUU4N6o"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("БОТ ЖИВ ✅")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("BOT STARTED")

app.run_polling()
