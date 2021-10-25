from telethn.sync import events
from telethn import Button
await event.client.bot.send_message(event.chat_id, f'**➢ Hᴇʏ {(event.sender.first_name)}**\n\n**➢ I Aᴍ [Psylocke](t.me/Psylocke_robot)**\n**➢ I Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ [Kwannon](t.me/kwannon)**', file='https://telegra.ph/file/a340604e274705673b96a.jpg', Buttons=[Button.inline('**Check**', data="psylocke")]
@System.bot.on(events.CallbackQuery(pattern=r"psylocke"))
async def ok(event):
     await event.answer(f'➢ Fɪʀsᴛ Nᴀᴍᴇ : {(event.sender.first_name)}\n➢ Lᴀsᴛ Nᴀᴍᴇ : {(event.sender.last_name)}\n➢ Usᴇʀɴᴀᴍᴇ : {(event.sender.username)}\n➢ Usᴇʀ Iᴅ : {(event.sender.id)}', alert=True)
