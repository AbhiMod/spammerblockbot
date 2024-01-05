import asyncio
import re
from importlib import import_module as import_
import random
from pyrogram import filters, filters, idle
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)

from spr import BOT_USERNAME, conn, session, spr
from spr.core import ikb
from spr.modules import MODULES
from spr.utils.misc import once_a_day, once_a_minute, paginate_modules

HELPABLE = {}


async def main():
    await spr.start()
    # Load all the modules.
    for module in MODULES:
        imported_module = import_(module)
        if (
            hasattr(imported_module, "__MODULE__")
            and imported_module.__MODULE__
        ):
            imported_module.__MODULE__ = imported_module.__MODULE__
            if (
                hasattr(imported_module, "__HELP__")
                and imported_module.__HELP__
            ):
                HELPABLE[
                    imported_module.__MODULE__.lower()
                ] = imported_module
    print("STARTED !")
    loop = asyncio.get_running_loop()
    loop.create_task(once_a_day())
    loop.create_task(once_a_minute())
    await idle()
    conn.commit()
    conn.close()
    await session.close()
    await spr.stop()


AM_PIC = [
    "https://telegra.ph/file/7c25ef427c9f3cded5577.jpg",
    "https://telegra.ph/file/625d235cc0a22fb8525b5.jpg",
    "https://telegra.ph/file/1c62254d59baf7f968ba7.jpg",
    "https://telegra.ph/file/7a0553bd4664486ab3008.jpg",
    "https://telegra.ph/file/7b4dfa606e6f23961d30e.jpg",
    "https://telegra.ph/file/2773dec98d87b8562618c.jpg",
    "https://telegra.ph/file/80353d02e0368b71d2666.jpg",
    "https://telegra.ph/file/6e5331dc4bef87464ea1c.jpg",
    "https://telegra.ph/file/199a2e44cb8e77bb21b34.jpg",
    "https://telegra.ph/file/8371bcd8952d089f9ec05.jpg",
    "https://telegra.ph/file/f970e559dd1bb96fced1a.jpg",
    "https://telegra.ph/file/59a305f8ce0c4e85949cc.jpg"
]

START_TEXT = """
Hi {} 
\n⋆─────────────────────⋆
I'm SpamProtectionbot, \n⋆─────────────────────⋆
Iᴍᴍᴇʀsᴇ ʏᴏᴜʀsᴇʟғ ɪɴ ᴀ ᴡᴏʀʟᴅ ᴏғ ᴍᴜsɪᴄ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ\n⋆─────────────────────⋆
Dɪsᴄᴏᴠᴇʀ, ᴘʟᴀʏ, ᴀɴᴅ ᴇɴJᴏʏ ʏᴏᴜʀ ғᴀᴠᴏʀɪᴛᴇ ᴛᴜɴᴇs ʀɪɢʜᴛ ʜᴇʀᴇ\n⋆─────────────────────⋆
Sɪᴍᴘʟʏ sᴇɴᴅ ᴍᴇ ᴛʜᴇ ɴᴀᴍᴇ ᴏғ ᴛʜᴇ sᴏɴɢ ᴏʀ ᴀʀᴛɪsᴛ, ᴀɴᴅ ʟᴇᴛ ᴛʜᴇ ᴍᴇʟᴏᴅʏ ʙᴇɢɪɴ. \n⋆─────────────────────⋆
Usᴇ Help ғᴏʀ ᴍᴏʀᴇ ᴄᴏᴍᴍᴀɴᴅs. 🎶
"""

button = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
    ],
    [
        InlineKeyboardButton("ᴅᴇᴠ", url=f"t.me/Sanam_King"),
    ],
    [
        InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅ", callback_data="bot_commands"),
    ]
])

@spr.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_photo(
        photo=random.choice(AM_PIC),
        caption=START_TEXT.format(message.from_user.mention, message.from_user.id),
        reply_markup=button
    )
@spr.on_callback_query(filters.regex("bot_commands"))
async def commands_callbacc(_, cq: CallbackQuery):
    text, keyboard = await help_parser(cq.from_user.mention)
    await asyncio.gather(
        cq.answer(),
        cq.message.delete(),
        spr.send_message(
            cq.message.chat.id,
            text=text,
            reply_markup=keyboard,
        ),
    )


async def help_parser(name, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(
            paginate_modules(0, HELPABLE, "help")
        )
    return (
        f"Hello {name}, I'm SpamProtectionbot, I can protect "
        + "your group from Spam and NSFW media using "
        + "machine learning. Choose an option from below.",
        keyboard,
    )


@spr.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(client, query: CallbackQuery):
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    u = query.from_user.mention
    top_text = (
        f"Hello {u}, I'm SpamProtectionRobot, I can protect "
        + "your group from Spam and NSFW media using "
        + "machine learning. Choose an option from below."
    )
    if mod_match:
        module = mod_match.group(1)
        text = (
            "{} **{}**:\n".format(
                "Here is the help for", HELPABLE[module].__MODULE__
            )
            + HELPABLE[module].__HELP__
        )

        await query.message.edit(
            text=text,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "back", callback_data="help_back"
                        )
                    ]
                ]
            ),
            disable_web_page_preview=True,
        )

    elif prev_match:
        curr_page = int(prev_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif create_match:
        text, keyboard = await help_parser(query)
        await query.message.edit(
            text=text,
            reply_markup=keyboard,
            disable_web_page_preview=True,
        )

    return await client.answer_callback_query(query.id)


@spr.on_message(filters.command("runs"), group=3)
async def runs_func(_, message: Message):
    await message.reply("What am i? Rose?")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
