from os.path import exists
from sqlite3 import connect

from aiohttp import ClientSession
from pyrogram import Client
from Python_ARQ import ARQ

SESSION_NAME = "BQChRclD6suwWBL-I4n9rD-K0Hgm7cQ_Ks98CrAvtaCRDznRr3ArNbunyjKT1TihOiwvQcXX-aSvZSy9uoxc-tBg4hPAnXH1E3wY5rb_Bf39OnNmXCNKCTnO8018hM6UdkURi2K1V2HbpDGgdl9D6duML4a8Jl52JpuwpQ10DejrQQDrB4qCPIWu8cgIEteWmg91IEFIfNLHrWK-sSVS0nuUmI1JwvOQZXt7fW5NmspO2EBAfAt2DF5p65pHpjrSdMKRNXaFH5afRXRGJjlGGJIFKrGmRoEEFmvZSkLc-s9jGlWe3_67_Rl5zZqZUrRgld5WtXdGt0zLQ8bZWa705oilAAAAAXHVJUAA"
DB_NAME = "postgres://yone:Kushal55@yone.cirqmtrbghab.us-east-1.rds.amazonaws.com:5432/yone"
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
