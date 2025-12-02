"""
from os import getenv


API_ID = int(getenv("API_ID", "26003553"))
API_HASH = getenv("API_HASH", "c1f27c622acecf9bf6e71d0d295e75f9")
BOT_TOKEN = getenv("BOT_TOKEN", "8172684751:AAFrKOePs4i_8Zbo3OciESAnP40EVT9cQlQ")
OWNER_ID = int(getenv("OWNER_ID", "8152589217"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8152589217,6073936818").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://MRDAXX:MRDAXX@mrdaxx.prky3aj.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002656120306"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002630993737"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "27400172"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "56d0a75c5f9a9de6beb5452aa63c2d36")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8040470417:AAHM6Jqwy28x0-78UbdQtyQg500dzoBokqI")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("Noobkacpbot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "7540570087"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7540570087").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003475251323"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://greenhornet63603:CvnxnjzknPLxYOfo@cluster0.qif4g18.mongodb.net/?appName=Cluster0"")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1003475251323"))

