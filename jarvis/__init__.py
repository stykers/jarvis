""" Jarvis initialization. """

import os

from sys import version_info
from logging import basicConfig, getLogger, INFO, DEBUG
from distutils.util import strtobool as sb

from dotenv import load_dotenv
from shutil import copyfile
from telethon import TelegramClient
import redis

load_dotenv("config.env")

# logging stuff
debug = sb(os.environ.get("DEBUG", "False"))
if debug:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=DEBUG,
    )
else:
    basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=INFO
    )
logs = getLogger(__name__)

if version_info[0] < 3 or version_info[1] < 6:
    logs.error(
        "Please upgrade your python interpreter to at least 3.6."
    )
    exit(1)

if os.path.exists("database.db"):
    os.remove("database.db")
else:
    logs.info("SQLite3 database file doesn't exist, generating...")

copyfile("utils/database.db", "database.db")

api_key = os.environ.get("API_KEY", None)
api_hash = os.environ.get("API_HASH", None)
bot = TelegramClient("jarvis", api_key, api_hash)

redis = redis.StrictRedis(host='localhost', port=6379, db=3)


def redis_check():
    try:
        redis.ping()
        return True
    except:
        return False


# a bunch of vars possibly used in other classes
count_msg = 0
users = {}
wide_map = dict((i, i + 0xFEE0) for i in range(0x21, 0x7F))
wide_map[0x20] = 0x3000
count_pm = {}
lastmsg = {}
enable_suicide = True
command_help = {}
afkreason = "work"
database_test = []