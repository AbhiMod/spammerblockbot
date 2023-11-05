from os.path import exists
from sqlite3 import connect
from Python_ARQ import ARQ
import logging
import os
import sys
import ast
import time
import base64
from aiohttp import ClientSession
from pyrogram import Client, errors
from telethon import TelegramClient



SESSION_NAME = "spambot"
DB_NAME = "db.sqlite3"
API_ID = 27733303
API_HASH = "c3c9d5e5d89c99fb8bb85a22a0cb5a26"
ARQ_API_URL = "https://arq.hamker.dev"

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
