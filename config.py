##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv('API_ID', "6435225"))
API_HASH = getenv('API_HASH', '4e984ea35f854762dcde906dce426c2d')
START_MESSAGE = getenv("START_MESSAGE", "THIS BOT IS MADE BY https://github.com/VENOM-CRAZY/START-BOT ")
START_PHOTO = getenv("START_PHOTO", "https://telegra.ph/file/7de370c57f1a1b7fba923.jpg")
OWNER_USERNAME = list(map(int, getenv('OWNER_USERNAME', '').split()))
