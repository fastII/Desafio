from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Função para responder às mensagens do usuário
def respond_message(update, context):
    update.message.reply_text('Olá! Sou um bot simples.')

def main():
    # Substitua 'TOKEN' pelo token do seu bot
    updater = Updater('6700804714:AAGcFASisZ0rInJqSzc_2jI0vOuXrzQuAhI', use_context=True)
    dispatcher = updater.dispatcher

    # Define um handler para responder a mensagens do usuário
    message_handler = MessageHandler(Filters.text & (~Filters.command), respond_message)
    dispatcher.add_handler(message_handler)

    # Inicia o bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
