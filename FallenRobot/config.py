class Config(object):
    LOGGER = True

    API_ID = "22029156"
    API_HASH = "7c7d75736193b71d40b00dc0b0981725"
    TOKEN = "5835236187:AAFP4OxZVBhrTxsmjjm6p-CAuA3qwLR_4g4"
    OWNER_ID = "5530347700"
    OWNER_USERNAME = "kailas_vg"
    SUPPORT_CHAT = "Pranav_support_Chat"
    JOIN_LOGGER = (-1001703890329)
    EVENT_LOGS = (-1001703890329)

    SQLALCHEMY_DATABASE_URI = "4-tEYOIkovamHgWSrChRXi5N4uIdcsIJ@mouse.db.elephantsql.com"
    MONGO_DB_URI = "mongodb+srv://kailasvg:kailasvg@cluster04.gvju7bn.mongodb.net/?retryWrites=true&w=majority"
    LOAD = []
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    URL = None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = 
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = 
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = 
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = 
    WOLVES = 

    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = (
        "CAACAgUAAxkBAAEDafNhq5Z0DegqVzauwSighMw5cPWp8QACVgQAAuUG0FRXfCEuBziNzCIE"
    )
    ALLOW_EXCL = True
    CASH_API_KEY = ""
    TIME_API_KEY = ""
    BL_CHATS = []
    SPAMMERS = None
    ALLOW_CHATS = True
    START_IMG = ""
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    ALLOW_EXCL = None
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
