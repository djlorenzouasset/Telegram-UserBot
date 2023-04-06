from pyrogram import filters
from pyrogram.types import Message

from utils.TelegramClient import TelegramClient


@TelegramClient.on_message(filters.command("leave", prefixes=".") & filters.me)
async def leave_chat(c: TelegramClient, m: Message):
    await m.edit(
        text='Bye bye!'
    )

    await c.leave_chat(
        chat_id=m.chat.id
    )