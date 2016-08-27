from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

location_command = "/give_me_book_locations - will send you locations where you can go hunt books\n"
facebook_command = "/facebook - our facebook group\n"
intro_command = "/introduction - will give you the game rules\n"
about_command = "/about - who we are and why we're doing this\n"
clue_command = "/give_me_a_clue - will give you a clue about a location\n"
help_command = "/help - see all commands\n"

# Methods handling commands
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="I'm a bot, please talk to me!")

def hello(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Hello {}'.format(update.message.from_user.first_name))

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text=intro_command + location_command + clue_command + facebook_command + about_command + help_command)


def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)


# Helpers

echo_handler = MessageHandler([Filters.text], echo)
caps_handler = CommandHandler('caps', caps, pass_args=True)

updater = Updater('247492263:AAFf0QZ0kYJH7hSCBK3Tquo9_CvOZuhiP6g')

# For quicker access to the Dispatcher used by your Updater
dispatcher = updater.dispatcher

# Register the methods handling commands
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('hello', hello))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)

updater.start_polling()
updater.idle()
