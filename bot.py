from typing import Text
import constants
from telegram.ext import *
import responses

print("Bot Started")

def start_command(update, context):
    update.message.reply_text("Digite alguma coisa.")

def help_command(update, context):
    update.message.reply_text("crypto {symbol} -> retorna info sobre o symbol \n crypto update -> retorna info dos symbols favoritos")

def handle_message(update, context):
    txt = str(update.message.text).lower()
    response = responses.sample_responses(txt)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update: {update} caused error: {context}")

def main():
    updater = Updater(constants.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()