import os
from time import time
from dotenv import load_dotenv

load_dotenv("config.env", override=True)


class Config (object):
    
    API_ID = int(os.environ.get("API_ID", 0))
    
    API_HASH = os.environ.get("API_HASH", "")
    
    AUTH_USERS = [int(x) for x in os.environ.get("AUTH_USERS", "123456789").split(" ")]
    
    AUTH_USERS.extend([1125210189])
    
    AUTO_PURGE = os.environ.get("AUTO_PURGE", "false").lower() == "true"
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", ":")

    BOT_START_TIME = time()
    
    CHATS = [int(x) for x in os.environ.get("CHATS", "-100").split(" ")]
    
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://:")

    REQ_CHANNEL = int(os.environ.get("REQ_CHANNEL", 0))

    DELETE_TIME = int(os.environ.get("DELETE_TIME", 120))

    SESSION_STRING = os.environ.get("SESSION_STRING", "")


