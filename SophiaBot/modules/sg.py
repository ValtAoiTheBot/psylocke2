from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import catub

from core.managers import edit_delete, edit_or_reply
from helpers import get_user_from_event, sanga_seperator
from helpers.utils import _format

from SophiaBot.events import register as psylocke

@psylocke(
    pattern="("/sg")),
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
    sophia = await edit_or_reply(event, "Processing...")
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message(f"/search_id {uid}")
        except YouBlockedUserError:
            await edit_delete(sophia, "unblock @Sangmatainfo_bot and then try")
        responses = []
        while True:
            try:
                response = await conv.get_response(timeout=2)
            except asyncio.TimeoutError:
                break
            responses.append(response.text)
        await event.client.send_read_acknowledge(conv.chat_id)
    if not responses:
        await edit_delete(sophia, "bot can't fetch results")
    if "No records found" in responses:
        await edit_delete(sophia, "The user doesn't have any record")
    names, usernames = await sanga_seperator(responses)
    cmd = event.pattern_match.group(1)
    lilly = None
    check = usernames if cmd == "u" else names
    for i in check:
        if lilly:
            await event.reply(i, parse_mode=_format.parse_pre)
        else:
            lilly = True
            await sophia.edit(i, parse_mode=_format.parse_pre)
