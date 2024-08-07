import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Read bot token from environment variable
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the Hamster Kombat Key Generator Bot! Use /getcode <game_number> <key_count> to generate a key. example if you want two keys for 'riding extreme 3d' use /getcode 1 2")

async def get_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Your existing code to generate and return the key

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    start_handler = CommandHandler('start', start)
    get_code_handler = CommandHandler('getcode', get_code)

    application.add_handler(start_handler)
    application.add_handler(get_code_handler)

    application.run_polling()
