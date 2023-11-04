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
    BOT_TOKEN = "6408453159:AAE1zyZc_KJ26xkJRCjZefhR0SJ3r-OAdIw"
    SUDOERS = [6204761408]
    NSFW_LOG_CHANNEL = -1002104689794
    SPAM_LOG_CHANNEL = -1001827829745
    ARQ_API_KEY = "EJSUNZ-BJXKAI-AKQDZL-NMPKWQ-ARQ"  # Get it from @ARQRobot
else:
    BOT_TOKEN = env.get("BOT_TOKEN","6408453159:AAE1zyZc_KJ26xkJRCjZefhR0SJ3r-OAdIw")
    SUDOERS = [int(x) for x in env.get("SUDO_USERS_ID", "6204761408 5360305806").split()]
    NSFW_LOG_CHANNEL = int(env.get("NSFW_LOG_CHANNEL","-1002104689794"))
    SPAM_LOG_CHANNEL = int(env.get("SPAM_LOG_CHANNEL","-1001827829745"))
    ARQ_API_KEY = env.get("ARQ_API_KEY","IWBOLK-SHIUBT-OJHGHB-AWNHNL-ARQ")
