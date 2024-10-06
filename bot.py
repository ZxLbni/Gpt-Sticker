from telegram import Update, InputFile
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define your bot token
BOT_TOKEN = '8018057302:AAEgq6gIUDsPyc9BBVgssDUkPmYewtTH2FM'

# Start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Welcome! Send me a sticker, and I'll get its ID and allow you to download it.")

# Function to handle sticker messages
def sticker_handler(update: Update, context: CallbackContext) -> None:
    sticker = update.message.sticker

    # Sticker File ID
    sticker_id = sticker.file_id
    update.message.reply_text(f"Sticker ID: `{sticker_id}`", parse_mode='Markdown')

    # Sticker File Download
    file = context.bot.get_file(sticker_id)
    file.download(f'{sticker_id}.webp')
    with open(f'{sticker_id}.webp', 'rb') as sticker_file:
        update.message.reply_document(document=sticker_file, filename=f'{sticker_id}.webp')

# Help command
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Send me a sticker to get its ID and download it!")

# Main function to run the bot
def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Sticker handler
    dispatcher.add_handler(MessageHandler(Filters.sticker, sticker_handler))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM, or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
    
