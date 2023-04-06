import asyncio

from pyrogram import filters
from pyrogram.types import Message
from typing import List

from utils.TelegramClient import TelegramClient


@TelegramClient.on_message((filters.private | filters.mentioned) & ~filters.me & ~filters.bot, group=1)
async def afk_handler(c: TelegramClient, m: Message):
    if not c.settings.afk.enabled:
        return
    
    x = await m.reply(
        c.settings.afk.answer.format(c.settings.afk.message), # you can change this text in the settings.json file at 'afk_answer_message'.
    )

    await asyncio.sleep(5)
    await x.delete()


@TelegramClient.on_message(filters.command("afk", prefixes=".") & filters.me)
async def afk(c: TelegramClient, m: Message):
    args: List[str] = m.command
    reason: str = ''

    if c.settings.afk.enabled:
        await m.edit('You are already AFK.')
        return await m.stop_propagation()
    

    if len(args) > 1:
        reason = ' '.join(args[1:])
    

    await c.settings.set_afk(reason=reason)
    await m.edit(text='I\'ve set your AFK! 💤')


@TelegramClient.on_message(filters.command("unafk", prefixes=".") & filters.me)
async def unafk(c: TelegramClient, m: Message):
    if not c.settings.afk.enabled:
        return await m.edit('You are not AFK! ❌')
        

    await c.settings.remove_afk()
    await m.edit(text='AFK removed! ✅')