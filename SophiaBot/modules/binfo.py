# If You Kanged This Module Plz Give Credits It Was Made By @AASFCYBERKING
# I Really Hardworked For This Module
import asyncio
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from SophiaBot.events import register
from SophiaBot import telethn as borg
from SophiaBot import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins

edit_time = 10
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/6f440b6c52be0cf1c0d29.jpg"
file2 = "https://telegra.ph/file/65c3a5f74c2d5e169bcc5.jpg"
file3 = "https://telegra.ph/file/b9b13f9bd1bf66acad9c9.jpg"
file4 = "https://telegra.ph/file/c18e9f242750f738787a7.jpg"
""" =======================CONSTANTS====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("/binfo"))
async def hmm(yes):
    chat = await yes.get_chat()
    await yes.delete()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    pm_caption = "** Psylocke 𝑖𝑠 𝑜𝑛𝑙𝑖𝑛𝑒  **\n\n"
    pm_caption += "**I Am Alive Till You Supporting...**\n\n"
    pm_caption += "✘ 𝙰𝚋𝚘𝚞𝚝 𝚖𝚎 ✘\n\n"
    pm_caption += f"➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ `{version.__version__}`\n"
    pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ** ☞ [ᴊᴏɪɴ](https://t.me/PigasusSupport)\n"
    pm_caption += "➾ **ᴜᴘᴅᴀᴛᴇꜱ**  ☞ [𝚃𝙴𝙰𝙼 𝙿𝙸𝙶𝙰𝚂𝚄𝚂](https://t.me/PigasusUpdates)\n"
    pm_caption += "➾ **ᴄʀᴇᴅɪᴛꜱ** ☞ [𝙰𝙰𝚂𝙵](https://github.com/AASFCYBERKING)\n\n"
    pm_caption += f"➾ **ᴜᴘᴛɪᴍᴇ** ☞ `{uptime}`\n\n"
    pm_caption += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [ᴋᴡᴀɴɴᴏɴ](tg://user?id=2069031161)\n"
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    
