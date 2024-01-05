import asyncio
import functools

import speedtest
from pyrogram import filters
from pyrogram.types import Message

from spr import spr as app
from spr import SUDOERS

def testspeed(m, _):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit_text("<b>⇆ ʀᴜɴɴɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅ sᴩᴇᴇᴅᴛᴇsᴛ...</b>")
        test.download()
        m = m.edit_text("<b>⇆ ʀᴜɴɴɪɴɢ ᴜᴩʟᴏᴀᴅ sᴩᴇᴇᴅᴛᴇsᴛ...</b>")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit_text("<b>↻ sʜᴀʀɪɴɢ sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs...</b>")
    except Exception as e:
        return m.edit_text(f"<code>{e}</code>")
    return result

@app.on_message(filters.command("speedtest"), group=3)
async def speedtest_function(client, message: Message):
    m = await message.reply_text("» ʀᴜɴɴɪɴɢ ᴀ sᴘᴇᴇᴅᴛᴇsᴛ...")
    loop = asyncio.get_event_loop()
    partial_func = functools.partial(testspeed, m)
    result = await loop.run_in_executor(None, partial_func)
    output = "✯ <b>sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs</b> ✯\n\n<u><b>ᴄʟɪᴇɴᴛ :</b></u>\n<b>» ɪsᴩ :</b> {0}\n<b>» ᴄᴏᴜɴᴛʀʏ :</b> {1}\n\n<u><b>sᴇʀᴠᴇʀ :</b></u>\n<b>» ɴᴀᴍᴇ :</b> {2}\n<b>» ᴄᴏᴜɴᴛʀʏ :</b> {3}, {4}\n<b>» sᴩᴏɴsᴏʀ :</b> {5}\n<b>» ʟᴀᴛᴇɴᴄʏ :</b> {6}\n<b>» ᴩɪɴɢ :</b> {7}".format(
        result["client"]["isp"],
        result["client"]["country"],
        result["server"]["name"],
        result["server"]["country"],
        result["server"]["cc"],
        result["server"]["sponsor"],
        result["server"]["latency"],
        result["ping"],
    )
    msg = await message.reply_photo(photo=result["share"], caption=output)
    await m.delete()

__MODULE__ = "SpeedTest"
__HELP__ = """
**Server SpeedTest**

/speedtest - server speed Test

"""
