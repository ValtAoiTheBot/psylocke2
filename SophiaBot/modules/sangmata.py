from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions, types

from SophiaBot import telethn
from SophiaBot.events import register as lilly

@lilly(
    pattern="sg(u)?(?:\s|$)([\s\S]*)",
    command=("sg"),
    info={
        "header": "To get name history of the user.",
        "flags": {
            "u": "That is sgu to get username history.",
        },
        "usage": [
            "{tr}sg <username/userid/reply>",
            "{tr}sgu <username/userid/reply>",
        ],
        "examples": "{tr}sg @missrose_bot",
    },
)
async def _(event):  # sourcery no-metrics
    "To get name/username history."
    input_str = "".join(event.text.split(maxsplit=1)[1:])
    reply_message = await event.get_reply_message()
    if not input_str and not reply_message:
        await edit_delete(
            event,
            "reply to  user's text message to get name/username history or give userid/username",
        )
    user, rank = await get_user_from_event(event, secondgroup=True)
    if not user:
        return
    uid = user.id
    chat = "@SangMataInfo_bot"
    misty = await edit_or_reply(event, "Processing...")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"/search_id {uid}")
        except YouBlockedUserError:
            await edit_delete(misty, "unblock @Sangmatainfo_bot and then try")
        responses = []
        while True:
            try:
                response = await conv.get_response(timeout=2)
            except asyncio.TimeoutError:
                break
            responses.append(response.text)
        await event.client.send_read_acknowledge(conv.chat_id)
    if not responses:
        await edit_delete(misty, "bot can't fetch results")
    if "No records found" in responses:
        await edit_delete(misty, "The user doesn't have any record")
    names, usernames = await sanga_seperator(responses)
    cmd = event.pattern_match.group(1)
    serena = None
    check = usernames if cmd == "u" else names
    for i in check:
        if serena:
            await event.reply(i, parse_mode=_format.parse_pre)
        else:
            serena = True
            await misty.edit(i, parse_mode=_format.parse_pre)
