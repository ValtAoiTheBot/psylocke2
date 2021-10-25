import System
from SophiaBot import events
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
await event.client.bot.send_message(event.chat_id, f'**➢ Hᴇʏ {(event.sender.first_name)}**\n\n**➢ I Aᴍ [Yᴜᴋɪɴᴀ](t.me/YuukiKonnoRobot)**\n**➢ I Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ [Sᴀɪ](t.me/Me_Iz_Mad_Boi)**', file='https://telegra.ph/file/a340604e274705673b96a.jpg', 

[
        InlineKeyboardButton(text="➕ Aᴅᴅ Mᴇ", data="psylocke"),   
    ],
],Button@System.bot.on(events.CallbackQuery(pattern=r"psylocke"))
async def ok(event):
     await event.answer(f'➢ Fɪʀsᴛ Nᴀᴍᴇ : {(event.sender.first_name)}\n➢ Lᴀsᴛ Nᴀᴍᴇ : {(event.sender.last_name)}\n➢ Usᴇʀɴᴀᴍᴇ : {(event.sender.username)}\n➢ Usᴇʀ Iᴅ : {(event.sender.id)}', alert=True)
