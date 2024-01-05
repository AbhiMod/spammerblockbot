import psutil
import time
from spr import spr  
from pyrogram import Client
from pyrogram import filters 
from pyrogram.types import Message
import random
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)

AM_SUPPORT = "-1001841879487"


@spr.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    for members in message.new_chat_members:
        if members.id == spr.id:
            count = await spr.get_chat_members_count(chat.id)

            msg = (
                f"📝 ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                f"____________________________________\n\n"
                f"📌 ᴄʜᴀᴛ ɴᴀᴍᴇ: {message.chat.title}\n"
                f"🍂 ᴄʜᴀᴛ ɪᴅ: {message.chat.id}\n"
                f"🔐 ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{message.chat.username}\n"
                f"📈 ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs: {count}\n"
                f"🤔 ᴀᴅᴅᴇᴅ ʙʏ: {message.from_user.mention}"
            )
            await spr.send_message(AM_SUPPORT, msg)
                                 

@spr.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await spr.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ #𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ ✫\n✫ 𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n✫ 𝐂ʜᴀᴛ 𝐈ᴅ : {chat_id}\n✫ 𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n✫ 𝐁ᴏᴛ : @SpamProtection_Bot"
        await spr.send_message(AM_SUPPORT, left)
      

__MODULE__ = "Lᴏɢɢᴇʀꜱ"
__HELP__ = """
**ᴛʜɪꜱ ᴄᴍᴅꜱ ɪꜱ ᴏɴʟʏ ᴄᴀɴ ꜱᴇᴇɴ ᴏᴡɴᴇʀ**


"""
