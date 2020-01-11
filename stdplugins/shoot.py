""" .kill """
import sys
from telethon import events, functions, __version__
from uniborg.util import admin_cmd
import asyncio

KILLSTR = [
    "AWM",
    "M24",
    "Kar98",
    "AKM",
    "M416",
    "UZI",
    "UMP9",
    "Knife",
    "Diamond Sword",
]    
KILL = random.choice(KILLSTR)

@borg.on(admin_cmd(pattern="kill$ ?(.*)", allow_sudo=True))  # pylint:disable=E0602
async def killing (killed):
    """ Dont Kill Too much -_-"""
    if not killed.text[0].isalpha() and killed.text[0] not in ("/", "#", "@", "!"):
        if await killed.get_reply_message():
            await killed.edit(
                f"Targeted user killed with {KILL} 😈......\n"
  "#Sad_Reacts_Onli\n"
            )
