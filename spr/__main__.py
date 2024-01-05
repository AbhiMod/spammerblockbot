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

AMBOT = "5360305806"

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
    "https://graph.org/file/72157e2add09a703c8fea.jpg",
    "https://graph.org/file/fe83c0e20b3ccd5bfa16a.jpg",
   "https://graph.org/file/fd93b9bde07fff9fb91b5.jpg"
]

START_TEXT = """
Hi {} 
\n⋆─────────────────────⋆
ɪ'ᴍ [SpamProtection](https://t.me/SpamProtection_Bot), \n⋆─────────────────────⋆
ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀꜱ ᴀᴅᴍɪɴ ᴡɪᴛʜ \n⋆─────────────────────⋆
ʙᴀɴ ʀɪɢʜᴛ ᴅᴇʟᴇᴛᴇ ᴍᴇꜱꜱᴇɢᴇ  \n⋆─────────────────────⋆
ɪ ᴡɪʟʟ ᴘʀᴏᴛᴇᴄᴛᴇᴅ ꜰʀᴏᴍ \n⋆─────────────────────⋆
ꜱᴘᴀᴍᴍᴇʀꜱ,ꜱᴄᴀᴍᴍᴇʀꜱ,ɴꜱꜰᴡꜱ ᴘᴀᴍᴍᴇʀꜱ\n⋆─────────────────────⋆
ꜰᴜʟʟ ᴛʀᴜꜱᴛᴇᴅ ꜱᴀꜰᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ \n⋆─────────────────────⋆
Usᴇ Help ғᴏʀ ᴍᴏʀᴇ ᴄᴏᴍᴍᴀɴᴅs.
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

@spr.on_message(filters.command("help"))
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
        f"Hello {name}, I'm [SpamProtectionbot](https://t.me/SpamProtection_Bot), I can protect "
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
