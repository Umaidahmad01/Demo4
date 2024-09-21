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
            text = f"<b>⌬ ᴏᴡɴᴇʀ : <a href=https://t.me/rin_nanakura>ʀɪɴ</a>\n⌬ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Ongoing_society'>ᴏɴɢᴏɪɴɢ sᴏᴄɪᴇᴛʏ</a>\n⌬ ᴀɴɪᴍᴇ sᴏᴄɪᴇᴛʏ : <a href='https://t.me/anime_sub_society'>ᴀɴɪᴍᴇ sᴏᴄɪᴇᴛʏ</a>\n⌬ ʙᴏᴛ sᴏᴄɪᴇᴛʏ : <a href='https://t.me/team_society_1'>ʙᴏᴛ sᴏᴄɪᴇᴛʏ</a>\n⌬ sᴏᴄɪᴇᴛʏ ᴄʜᴀᴛ ᴢᴏɴᴇ : <a href='https://t.me/ahss_help_zone'>ᴄʜᴀᴛ ᴢᴏɴᴇ</a>\n࿂ Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ : <a href='https://t.me/i_killed_my_clan'>❰⏤͟͞ 𝚯𝗕𝗜𝗧𝗢 -//-❱</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('⛩️ ʜᴏᴍᴇ ⛩️ ', url='https://t.me/anime_sub_society')
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
