#!/usr/bin/env python3

import telegram
from credential import TELEGRAM_TOKEN
from test import get_tone_for_user
from plots import plot_emotions

def main():
    updater = telegram.Updater(token=TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.addTelegramCommandHandler('start', start)
    dispatcher.addTelegramCommandHandler('username_tone', username_tone)

    dispatcher.addUnknownTelegramCommandHandler(unknown)

    updater.start_polling()

def start(bot, update):
    help_message = """
            Oi, I'm the What's On bot, I can help you understand emotions behind subreddit comments.
        
            You can control me by sending these commands:
            
            /ut <username> -n <#count> : Evaluate the mood of the <n> last comment made by <username>
           """
    bot.sendMessage(chat_id=update.message.chat_id, text=help_message)

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
        #tones = FAKE_TONES
        for tone in tones:
            # Plot emotions and save it to an image file
            plot_emotions(tone.etone)

            # Send the image file
            photo = open('../out/figure.png', 'rb')
            bot.sendPhoto(chat_id=chat_id, photo=photo)
            photo.close()

            bot.sendMessage(chat_id=chat_id, text=str(tone.etone))
            bot.sendMessage(chat_id=chat_id, text=str(tone.wtone))
            bot.sendMessage(chat_id=chat_id, text=str(tone.stone))


if __name__ == "__main__":
    main()
