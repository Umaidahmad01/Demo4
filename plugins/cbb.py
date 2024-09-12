#(©)Codeflix-Bots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>⌬ ᴏᴡɴᴇʀ : <a href=https://t.me/WoW_Gameplayes_YT>ᴀᴅɪᴛɪʏᴀ</a>\n⌬ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/animes_in_hindi_sub'>ᴀɴɪᴍᴇ ʜs</a>\n⌬ ᴀɴɪᴍᴇ ʜs : <a href='https://t.me/animes_in_hindi_sub'></a>\n⌬ ᴀɴɪᴍᴇ ʜs ᴄʜᴀᴛ : <a href='https://t.me/+xgMSJVXJnyM1MDY1'>ᴄʜᴀᴛ ᴢᴏɴᴇ</a>\n࿂ Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ : <a href='https://t.me/i_killed_my_clan'>❰⏤͟͞ 𝚯𝗕𝗜𝗧𝗢 -//-❱</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('⛩️ ʜᴏᴍᴇ ⛩️ ', url='https://t.me/animes_in_hindi_sub')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
