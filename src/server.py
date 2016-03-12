#!/usr/bin/env python3

import logging
import telegram
from credentials import TELEGRAM_TOKEN
from test import get_tone_for_user
from test import get_raw_tone
from plots import plot_emotions
from plots import plot_writing
from plots import plot_social

def main():
    # Activate logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    updater = telegram.Updater(token=TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.addTelegramCommandHandler('start', start)
    dispatcher.addTelegramCommandHandler('help', start)
    dispatcher.addTelegramCommandHandler('ut', username_tone)
    dispatcher.addTelegramCommandHandler('rs', raw_text)

    dispatcher.addUnknownTelegramCommandHandler(unknown)

    # Add error handler that prints error to stdin
    dispatcher.addErrorHandler(lambda _, error: print(error))

    updater.start_polling()

def start(bot, update):
    help_message = "\
    Oi, I'm the What's On bot, I can help you understand emotions behind subreddit comments.\n\
    You can control me by sending these commands:\n\
    \n\
    /rs <string> : Evaluate the mood of a raw message sent to the bot\n\
    /ut <username> : Evaluate the mood of the last comment made by <username>\n\
    "
    bot.sendMessage(chat_id=update.message.chat_id, text=help_message)

def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Sorry, I didn't understand that command.")

def raw_text(bot, update, args):
    chat_id = update.message.chat_id
    bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    tone = get_raw_tone(" ".join(args))

    plot_emotions(tone.etone)
    send_figure(bot, chat_id)
    plot_writing(tone.wtone)
    send_figure(bot, chat_id)
    plot_social(tone.stone)
    send_figure(bot, chat_id)




def username_tone(bot, update, args):
    chat_id = update.message.chat_id

    if len(args) != 1:
        bot.sendMessage(
            chat_id=chat_id,
            text='You need to provide a reddit username, like so: /ut <username>')
    else:
        # Display "typing" chat action to show that something is happening
        bot.sendChatAction(chat_id=chat_id, action=telegram.ChatAction.TYPING)

        comment_to_tones = get_tone_for_user(args[0])

        for comment, tone in comment_to_tones:
            bot.sendMessage(
                chat_id=chat_id,
                text="Your last comment: {}".format(comment))

            # Plot emotions, writings and social and send it through telegram
            plot_emotions(tone.etone)
            send_figure(bot, chat_id)
            plot_writing(tone.wtone)
            send_figure(bot, chat_id)
            plot_social(tone.stone)
            send_figure(bot, chat_id)

def send_figure(bot, chat_id):
    # Send the image file
    photo = open('../out/figure.png', 'rb')
    bot.sendPhoto(chat_id=chat_id, photo=photo)
    photo.close()


if __name__ == "__main__":
    main()
