from pyrogram import filters
from pyrogram.types import Message, User, Chat
from typing import List

from utils.TelegramClient import TelegramClient


@TelegramClient.on_message(filters.command("user", prefixes=".") & filters.me)
async def user_info(c: TelegramClient, m: Message):
    args: List[str] = m.command
    

    if m.reply_to_message:
        user: User = m.reply_to_message.from_user

        await m.edit(
            text=f'<b>🗂 Informations</b>\n\n'
                f'<b>👤 Name:</b> {user.mention}\n'
                f'<b>🌐 Username:</b> @{user.username}\n'
                f'<b>🆔 Id:</b> <code>{user.id}</code>\n'
                f'<b>🇪🇺 DC:</b> {user.dc_id}\n'
                f'<b>⚙️ Bot:</b> {"Yes" if user.is_bot else "No"}\n'
                f'<b>⭐️ Premium:</b> {"Yes" if user.is_premium else "No"}'
        )


    elif len(args) > 1:
        user: User = await c.get_users(user_ids=args[1])
        if user:
            await m.edit(
                text=f'<b>🗂 Informations</b>\n\n'
                    f'<b>👤 Name:</b> {user.mention}\n'
                    f'<b>🌐 Username:</b> @{user.username}\n'
                    f'<b>🆔 Id:</b> <code>{user.id}</code>\n'
                    f'<b>🇪🇺 DC:</b> {user.dc_id}\n'
                    f'<b>⚙️ Bot:</b> {"Yes" if user.is_bot else "No"}\n'
                    f'<b>⭐️ Premium:</b> {"Yes" if user.is_premium else "No"}'
            )
        else:
            await m.edit('User not found.')

    else:
        await m.edit('You have to reply to a message or specify the id/username of the user.')



@TelegramClient.on_message(filters.command("chat", prefixes=".") & filters.me)
async def chat_info(c: TelegramClient, m: Message):
    args: List[str] = m.command
    chat: Chat = m.chat 

    if len(args) > 1:
        chat: Chat = await c.get_chat(chat_id=args[1])
        if chat:
            await m.edit(
                text=f'<b>🗂 Informations</b>\n\n'
                    f'<b>👥 Name:</b> {chat.title if chat.title else "-"}\n'
                    f'<b>🌐 Username:</b> @{chat.username if chat.username else "-"}\n'
                    f'<b>🆔 Id:</b> <code>{chat.id}</code>\n'
                    f'<b>🇪🇺 DC:</b> {chat.dc_id if chat.dc_id else "-"}\n'
                    f'<b>👨‍👩‍👦 Members:</b> {chat.members_count if chat.members_count else "-"}\n'
            )

        else:
            await m.edit(
                text='Group not found.'
            )

    else:
        await m.edit(
            text=f'<b>🗂 Informations</b>\n\n'
                f'<b>👥 Name:</b> {chat.title if chat.title else "-"}\n'
                f'<b>🌐 Username:</b> @{chat.username if chat.username else "-"}\n'
                f'<b>🆔 Id:</b> <code>{chat.id}</code>\n'
                f'<b>🇪🇺 DC:</b> {chat.dc_id if chat.dc_id else "-"}\n'
                f'<b>👨‍👩‍👦 Members:</b> {chat.members_count if chat.members_count else "-"}\n'
        )
        