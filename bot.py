from telegram import Update, ParseMode
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Function to handle /start command
async def start(update: Update, context) -> None:
    await update.message.reply_text("Send me a sticker, and I'll provide the file ID!")

# Function to handle stickers and extract file ID
async def get_sticker_id(update: Update, context) -> None:
    sticker = update.message.sticker
    if sticker:
        await update.message.reply_text(f"Sticker File ID: <code>{sticker.file_id}</code>", parse_mode=ParseMode.HTML)
    else:
        await update.message.reply_text("Please send a sticker!")

# Main function to start the bot
async def main():
    # Add your bot token here
    TOKEN = ""
    
    # Create the Application instance
    application = Application.builder().token(TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.Sticker.ALL, get_sticker_id))

    # Start the bot
    await application.start_polling()
    await application.idle()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
