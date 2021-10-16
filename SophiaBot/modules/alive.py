from telethon import events, Button, custom
import re, os
from SophiaBot.events import register
from SophiaBot import telethn as tbot
from SophiaBot import telethn as tgbot
PHOTO = "https://telegra.ph/file/3ad9b32cd366aab77f1ae.jpg"
@register(pattern=("/alive"))
async def awake(event):
  PIKACHU = event.sender.first_name
  PIKACHU = "**♡ I,m ᴘꜱʏʟᴏᴄᴋᴇ 💝** \n\n"
  PIKACHU += "**♡ I'm Working Properly 💕**\n\n"
  PIKACHU += "**♡ ᴘꜱʏʟᴏᴄᴋᴇ : 2.0 LATEST 💞**\n\n"
  PIKACHU += "**♡ My Master :** [ᴋᴡᴀɴɴᴏɴ](t.me/Kwannon) 💓\n\n"
  PIKACHU += "**♡ Telethon Version : 1.23.0 💗**\n\n"
  BUTTON = [[Button.url("𝙎𝙐𝙋𝙋𝙊𝙍𝙏 ❣️", "https://t.me/PigasusSupport"), Button.url("𝙐𝙋𝘿𝘼𝙏𝙀 💓", "https://t.me/PigasusUpdates")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=PIKACHU,  buttons=BUTTON)
