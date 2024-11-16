import json
import os


def get_user_list(config, key):
    with open("{}/Emilia/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    API_HASH = "3fc2b371f4fbb0166758736414d8be92" # API_HASH from my.telegram.org
    API_ID = 25475489 # API_ID from my.telegram.org

    BOT_ID = 7617090520 # BOT_ID
    BOT_USERNAME = "Fubuki_cutibot" # BOT_USERNAME

    MONGO_DB_URL = "mongodb+srv://1:1@cluster0.ull4r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" # MongoDB URL from MongoDB Atlas

    SUPPORT_CHAT = "TheSuperiorDynasty" # Support Chat Username
    UPDATE_CHANNEL = "Choco_for_u" # Update Channel Username
    START_PIC = "https://pic-bstarstatic.akamaized.net/ugc/9e98b6c8872450f3e8b19e0d0aca02deff02981f.jpg@1200w_630h_1e_1c_1f.webp" # Start Image
    DEV_USERS = [7512760579, 6940098429, 1266240012] # Dev Users
    TOKEN = "7617090520:AAH6OqlzkAGlJUhtd6O3yd9sRfDo6lxwn00" # Bot Token from @BotFather

    EVENT_LOGS = -1002122538649 # Event Logs Chat ID
    OWNER_ID = 1266240012 # Owner ID
 
    TEMP_DOWNLOAD_DIRECTORY = "./" # Temporary Download Directory
    BOT_NAME = "˹𝙁ᴜʙᴜᴋɪ ✘ 𝐌ᴜsɪᴄ˼🫧" # Bot Name
    WALL_API = "6950f53" # Wall API from wall.alphacoders.com
    ORIGINAL_EVENT_LOOP = True # Do not Change


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
