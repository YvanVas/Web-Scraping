import logging
# Importar libreria de precios de la yerba
from yerba import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

# Iniciar Loggin
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# funcion para enviar el primer mensaje luego del /start


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        'Hola! envíe \"/buscar\" para elegir el tamaño y saber su precio')


# funcion para explicar los comandos
def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        '- Envíe /menu para acceder al menu de eleccion de la yerba por su tamaño /n - Envíe /links para acceder a las páginas')


def echo(update, context):
    # Busca una palabra clave, y responde con un mensaje
    if(update.message.text.upper().find("YERBA CAMPESINO") > 0):
        update.message.reply_text("Prefiero la yerba kurupi")
    elif(update.message.text.upper().find("") > 0):
        update.message.reply_text("Envíe /menu para saber que hacer")
    else:
        update.message.reply_text("Envíe /menu para saber que hacer")


# Menu de opciones  para distintos datos
def menuPrecio(update, context):
    kurupi250 = precioK250
    kurupi500 = precioK500
    keyboard = [
        [
            InlineKeyboardButton("250 Gr", callback_data=kurupi250),
            InlineKeyboardButton("500 Gr", callback_data=kurupi500)
        ]
    ]
    # escuchando la eleccion
    reply_markup = InlineKeyboardMarkup(keyboard)
    # titulo del menu
    update.message.reply_text(
        'Seleccione el tamaño de la yerba:', reply_markup=reply_markup)


def buttonPrecio(update, context):
    query = update.callback_query
    # CallbackQueries necesita una respuesta para seguir
    query.answer()
    query.edit_message_text(
        text="El precio es de la yerba es de: {}".format(query.data)
    )


def main():
    """Inicia el bot con un TOKEN"""
    updater = Updater(
        " ", use_context=True)

    dp = updater.dispatcher

    # los diferentes comandos para bot
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ayuda", help_command))
    dp.add_handler(CommandHandler("buscar", menuPrecio))

    updater.dispatcher.add_handler(CallbackQueryHandler(buttonPrecio))

    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
