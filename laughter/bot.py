from random import choice, randint

from discord import Intents, Message, Permissions
from discord.ext.commands import Bot
from laughter.log import setup_logging

setup_logging()

EMOJIS = ["\N{ROLLING ON THE FLOOR LAUGHING}", "\N{FACE WITH TEARS OF JOY}"]
PERMS_NEEDED = Permissions(add_reactions=True, read_message_history=True)

bot = Bot(
    command_prefix=lambda *_: [],
    intents=Intents(guilds=True, guild_messages=True, dm_messages=True),
)


def should_react(message: Message) -> bool:
    if message.guild is not None:
        curr_perms = message.channel.permissions_for(message.guild.me)
        if not curr_perms.is_superset(PERMS_NEEDED):
            return False
    skip_it = randint(0, 3)
    return not skip_it


@bot.event
async def on_message(message: Message) -> None:
    if not should_react(message):
        return
    await message.add_reaction(choice(EMOJIS))
