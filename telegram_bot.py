from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual token
TOKEN = ''

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        'Welcome to the bot! To choose a game number, type /game followed by the number.\n'
        'Example: /game 1\n\n'
        'This bot is created for you by Akako.'
    )

def game(update: Update, context: CallbackContext) -> None:
    if context.args:
        number = context.args[0]
        update.message.reply_text(f'You chose game number {number}.')
    else:
        update.message.reply_text('Please provide a game number after the command.')

def main() -> None:
    # Create Updater object and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('game', game))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
