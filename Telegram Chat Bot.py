from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your chatbot. How can I help you?")

# Define a function to handle incoming messages
def echo(update, context):
    user_message = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"You said: {user_message}")

# Define a function to handle unknown commands
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(token='YOUR_TELEGRAM_BOT_TOKEN', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register handler for the /start command
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Register handler for incoming messages
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # Register handler for unknown commands
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
