from telegram.ext import *
import constants,responses

def start_command(update,context):
    update.message.reply_text(f"Olá {update.message.from_user['first_name']} Seja bem vindo ao bot do Canal Refatorando, digite /help para ver os comandos disponíveis")

def help_command(update,context):
    update.message.reply_text("oi ou olá -> retorna uma saudação\ncanal -> retorna informações sobre o Canal do Youtube\ncrypto {symbol} -> retorna info sobre o symbol \ncrypto update -> retorna info dos symbols favoritos")

def handle_message(update,context):
    txt = str(update.message.text).lower()
    response = responses.sample_responses(txt)

    update.message.reply_text(response)

def error(update, context):
    print(f"Update: {update} caused error: {context.error}")

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