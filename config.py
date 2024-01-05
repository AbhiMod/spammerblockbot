from os import environ as env

from dotenv import load_dotenv

load_dotenv("config.env")

"""
READ EVERYTHING CAREFULLY!!!
"""


DEPLOYING_ON_HEROKU = (
    True  # Make this False if you're not deploying On heroku/Docker
)


if not DEPLOYING_ON_HEROKU:
    BOT_TOKEN = "6408453159:AAFGnJBvwSWnYGHdTu6N4xawyFM7itLQK_A"
    SUDOERS = [5360305806]
    NSFW_LOG_CHANNEL = -1002104689794
    SPAM_LOG_CHANNEL = -1001827829745
    OWNER_ID = "5360305806"
    GBANS = -1001908711819
    ARQ_API_KEY = "MRCDOC-TOYWRA-PYSBZU-VIMOOW-ARQ"  # Get it from @ARQRobot
else:
    BOT_TOKEN = env.get("BOT_TOKEN","6408453159:AAFGnJBvwSWnYGHdTu6N4xawyFM7itLQK_A")
    SUDOERS = [int(x) for x in env.get("SUDO_USERS_ID", "5360305806").split()]
    NSFW_LOG_CHANNEL = int(env.get("NSFW_LOG_CHANNEL","-1002104689794"))
    SPAM_LOG_CHANNEL = int(env.get("SPAM_LOG_CHANNEL","-1001827829745"))
    ARQ_API_KEY = env.get("ARQ_API_KEY","MRCDOC-TOYWRA-PYSBZU-VIMOOW-ARQ")
    OWNER_ID = env.get("OWNER_ID","5360305806")
    GBANS = int(env.get("GBANS","-1001908711819"))
