#!/usr/bin/env python3


from telegram import Updater
from credential import TELEGRAM_TOKEN

def main():
    updater = Updater(token=TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.addTelegramCommandHandler('start', start)
    updater.start_polling()



def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")




if __name__ == "__main__":
    main()
