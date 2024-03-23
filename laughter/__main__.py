from os import environ
from .bot import bot


def run():
    bot.run(environ["BOT_TOKEN"], log_handler=None)
