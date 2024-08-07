import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from keygen import generate_keys  # Import the function from keygen.py

# Read bot token from environment variable
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        'Welcome to the Hamster Kombat Key Generator Bot! '
        'Use /getcode <game_number> <key_count> to generate a key. '
        'Example: if you want two keys for "riding extreme 3d", use /getcode 1 2'
    )

async def get_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 2:
        await update.message.reply_text(
            'Usage: /getcode <game_number> <key_count>. '
            'Example: /getcode 1 2'
        )
        return

    try:
        game_number = int(context.args[0])
        key_count = int(context.args[1])
    except ValueError:
        await update.message.reply_text(
            'Invalid arguments. Please provide numeric values for <game_number> and <key_count>.'
        )
        return

    try:
        keys, game_name = await generate_keys(game_number, key_count)
        if not keys:
            await update.message.reply_text(f'No keys generated for {game_name}.')
        else:
            response = '\n'.join(keys)
            await update.message.reply_text(f'Generated keys for {game_name}:\n{response}')
    except Exception as e:
        await update.message.reply_text(f'An error occurred: {str(e)}')

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    start_handler = CommandHandler('start', start)
    get_code_handler = CommandHandler('getcode', get_code)

    application.add_handler(start_handler)
    application.add_handler(get_code_handler)

    application.run_polling()
