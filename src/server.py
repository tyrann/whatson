#!/usr/bin/env python3

import telegram
from credential import TELEGRAM_TOKEN
from test import get_tone_for_user

def main():
    updater = telegram.Updater(token=TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.addTelegramCommandHandler('start', start)
    dispatcher.addTelegramCommandHandler('username_tone', username_tone)

    dispatcher.addUnknownTelegramCommandHandler(unknown)

    updater.start_polling()

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hey, I'm WhatSon bot! How can I help?")

def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

def username_tone(bot, update, args):
    chat_id = update.message.chat_id

    if len(args) != 1:
        bot.sendMessage(
            chat_id=chat_id,
            text='You need to provide a reddit username, like so: /username_tone <username>')
    else:
        # Display "typing" chat action to show that something is happening
        bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)

        tones = get_tone_for_user(args[0])
        for tone in tones:
            bot.sendMessage(chat_id=chat_id, text=str(tone.etone))


if __name__ == "__main__":
    main()
