from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

from typing import List

from utils.TelegramClient import TelegramClient


@TelegramClient.on_message(filters.command("spam", prefixes=".") & filters.me)
async def spam(c: TelegramClient, m: Message):
    args: List[str] = m.command 

    if len(args) > 2:
        await m.delete()

        messages_to_send: int = int(args[1])
        message: str = ' '.join(args[2:])

        for _ in range(messages_to_send): # send messages
            try:
                await c.send_message(
                    chat_id=m.chat.id,
                    text=message
                )
            except FloodWait:
                pass

    else:
        await m.edit(text='You have to specify the number of messages to send and the message.')