import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCctL8XA_vSEXw4KHMM4QU_1858cFQ4Hs8DJQLqSryxFeRsmbxOGK-EDCw-Px6Qv11A5C832EUXcuZGGLrlhe5zj0nEb2ITpVFoVbb-cRTB39Usl3o295ozOjbqZK6sJ7LW2-TG0qjJtcIj3CrAMbOeTdsx2nabIfRJ0R2NAo1T-DQ9EmggjTszoSE0exUebJz4vZHbT-hywZN9_djRRArVjWu96r_-7BCrdYXc4JHwX_SFfZCCAZ9IGSZBf4hfNUXANeBzUj8O7cAy817_jaFLSVyClJT0RLU0TnTBWt-Jouou2eaqV8mWpT6Bb1C7-dkHp3VUuEqFdkKgSs9ZcJ4mfQMqfgA")
BOT_TOKEN = getenv("BOT_TOKEN","5042486379:AAFCIcYnS-A-BpJC8mBAVX_U4ONe3hVmlug")
BOT_NAME = getenv("BOT_NAME", "calclator bot")
API_ID = getenv("API_ID", "8064991")
API_HASH = getenv("API_HASH", "9c1ef35f4339c2153f3f6254eee60691")
OWNER_NAME = getenv("OWNER_NAME", "janith_sadanuwan")
ALIVE_NAME = getenv("ALIVE_NAME", "hii janith")
BOT_USERNAME = getenv("BOT_USERNAME", "A_Calculator_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "janith_sadanuwan")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "janithbots")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "janithbots")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/a381b439e2bf6c61703f9.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "30"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/a381b439e2bf6c61703f9.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/a381b439e2bf6c61703f9.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/a381b439e2bf6c61703f9.png")
