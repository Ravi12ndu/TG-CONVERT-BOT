import pyrogram

from pyrogram import Filters, InlineKeyboardMarkup, InlineKeyboardButton
from translation import Translation

@Client.on_message(Filters.command(["start"]))
async def start(c, m):
    await c.send_message(chat_id=m.chat.id,
                         text=Translation.START.format(m.from_user.first_name),
                         reply_to_message=m.message_id)

@Client.on_message(Filters.command(["help"]))
async def help(c, m):
    await c.send_message(chat_id=m.chat.id,
                         text=Translation.HELP,
                         reply_to_message=m.message_id)
