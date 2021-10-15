import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, version
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME, Lastupdate
from . import dcdef
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "TSF USERBOT"

global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/5a7945894898e8cee4a26.jpg"
file2 = "https://telegra.ph/file/562e49da0f074c4b8e18f.jpg"
file3 = "https://telegra.ph/file/5a7945894898e8cee4a26.jpg"
file4 = "https://telegra.ph/file/562e49da0f074c4b8e18f.jpg"
""" =======================CONSTANTS====================== """


@borg.on(admin_cmd(pattern=r"/alive"))
@borg.on(sudo_cmd(pattern=r"/alive", allow_sudo=True))

async def hmm(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    await yes.delete()
    uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
    pm_caption = "** ᴘꜱʏʟᴏᴄᴋᴇ ɪꜱ ᴏɴʟɪɴᴇ **\n\n"
    pm_caption += "**Your Psylocke Alive And Systems Are Working Perfectly As It Should Be...**\n\n"
    pm_caption += "✘ 𝙰𝚋𝚘𝚞𝚝 𝚖𝚎 ✘\n\n"
    pm_caption += f"➾ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ** ☞ {version.__version__}\n"
    pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ** ☞ [ᴊᴏɪɴ](https://t.me/Pigasusupdates)\n"
    pm_caption += "➾ **ᴀᴅᴅ ᴍᴇ**  ☞ [ᴄʟɪᴄᴋ ʜᴇʀᴇ](http://t.me/Psylocke_robot?startgroup=true)\n"
    pm_caption += "➾ **ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ** ☞ [ᴊᴏɪɴ](https://t.me/PigasusSupport)\n\n"
    pm_caption += f"➾ **ᴜᴘᴛɪᴍᴇ** ☞ {uptime}\n\n"
    pm_caption += f"➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{Kwannon}](tg://user?id={Kwanon})\n"
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

    
