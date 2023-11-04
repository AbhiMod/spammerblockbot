from os.path import exists
from sqlite3 import connect

from aiohttp import ClientSession
from pyrogram import Client
from Python_ARQ import ARQ

SESSION_NAME = "BQC92TNmQRV2YX9WNXHM8xQ6F7Iu-UOjLmUCa52LXluXwVs_aFMfqUjyN5vr8Cj4bZ5Nxh4QUNHWn1bu2BOLs7WY9nZ8Uon0S7O6A7ozrMx0hzjkrwAuaD5Y7-1Qv3i0Hz8ggvkqPMcJaroRJwioX4YXrCAgwkwLSNbOOiKz-04NXbFVe8ffe7QxoAKedqzZ0NvkiqBgG3bKOz7S_D6SM_OE6Qw0PCZy-h7-S6dSIiAJ7TIJJP4aKVoJRxpro1i7Vtzvyk_sAvdEjCmoUcNFkFm2lCogZ0IUiw5t-sD9h-61jc3saVbauDeBex2rlZ-nDcUP0-Hss-onKIM_77UxS11FAAAAAYzDgH8A"
DB_NAME = "db.sqlite3"
API_ID = 27733303
API_HASH = "c3c9d5e5d89c99fb8bb85a22a0cb5a26"
ARQ_API_URL = "https://arq.hamker.in"

if exists("config.py"):
    from config import *
else:
    from sample_config import *

session = ClientSession()

arq = ARQ(ARQ_API_URL, ARQ_API_KEY, session)

conn = connect(DB_NAME)

spr = Client(
    SESSION_NAME,
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
)
with spr:
    bot = spr.get_me()
    BOT_ID = bot.id
    BOT_USERNAME = bot.username
