from pyrogram import filters
from pyrogram.types import Message

from utils.TelegramClient import TelegramClient


@TelegramClient.on_message(filters.command("save", prefixes=".") & filters.me)
async def save_message(_, m: Message):
    if m.reply_to_message:
        
        await m.reply_to_message.forward(
            chat_id="me"
        )

        await m.edit(
            text="Message saved."
        )

    else:
        await m.edit(text="You have to reply to a message.")