import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    update.message.reply_text("Hola, Geeks!")
    return "Hola, Geeks!"

def help(update, context):
    """Envia un mensaje cuando se emita el comando /help."""
    update.message.reply_text("Ayudame!")
    return "Ayudame!"

def mayus(update, context):
    mensaje = context.args[0].upper()
    update.message.reply_text(mensaje)
    return mensaje
def alreves(update, context):
    """Repite el mensaje del usuario."""
    mensaje = update.message.text
    msj = ""
    for i in range (len(mensaje)-1,0,-1):
        msj += mensaje[i] 
    msj += mensaje[0]
    update.message.reply_text(msj)
    return msj

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Inicio del Bot"""
    #Colocamos el Token creado por FatherBot
    updater = Updater("1150186932:AAFM14CFYJ-6zA_Yhx2m1pNttAu9DftOQzo", use_context=True)



    # Es el Registro de Comandos a través del dispartcher
    dp = updater.dispatcher

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",help))
    dp.add_handler(CommandHandler("mayus",mayus))


    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    echo_handler = MessageHandler(Filters.text & (~Filters.command), alreves)
    dp.add_handler(echo_handler)
    
    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
