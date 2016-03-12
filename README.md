# What's On?

## Information
`What's On?` is an Telegram bot that provides an interface to IBM Watson for analysing the mood of posts and comments on reddit.

## Commands

* `/help` Send help message
* `/rs <string>` : Evaluate the mood of a raw message sent to the bot
* `/ut <username>` : Evaluate the mood of the last comment made by `<username>` on reddit


## Install your own bot

To install the bot on your server, clone the repo, rename the [credentials.py.example](credentials.py.example) file to `credentials.py`. Create a telegram bot with [Botfather](https://telegram.me/botfather), and fill in the `BOT_TOKEN` in `credentials.py`. Finally, add your own credentials from IBM Bluemix to access the Watson API.   

You also need to install the [dependencies](requirements.txt): 

Your bot is ready! Launch it with `./server.py` or `python3 server.py`.

