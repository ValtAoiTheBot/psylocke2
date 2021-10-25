from SophiaBot import System
from telethon.sync import events
from telethon import Button
await event.client.bot.send_message(event.chat_id, f'**➢ Hᴇʏ {(event.sender.first_name)}**\n\n**➢ I Aᴍ [Yᴜᴋɪɴᴀ](t.me/YuukiKonnoRobot)**\n**➢ I Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ [Sᴀɪ](t.me/Me_Iz_Mad_Boi)**', file='cute.jpg', buttons=[Button.inline('**Iɴғᴏ**', data="psylocke"), Button.url('**Sᴜᴘᴘᴏʀᴛ**', 'https://t.me/YuukiSupportChat')])
@System.bot.on(events.CallbackQuery(pattern=r"psylocke"))
async def ok(event):
     await event.answer(f'➢ Fɪʀsᴛ Nᴀᴍᴇ : {(event.sender.first_name)}\n➢ Lᴀsᴛ Nᴀᴍᴇ : {(event.sender.last_name)}\n➢ Usᴇʀɴᴀᴍᴇ : {(event.sender.username)}\n➢ Usᴇʀ Iᴅ : {(event.sender.id)}', alert=True)
