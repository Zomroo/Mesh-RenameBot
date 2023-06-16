from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "postgres://oypdrwxq:gZHTqsJSmlyQ0rp_DWSnGDrOsTcYM-Pl@suleiman.db.elephantsql.com/oypdrwxq"]
        API_HASH = [str, "1e26ebacf23466ed6144d29496aa5d5b"]
        API_ID = [int, 14091414]
        BOT_TOKEN = [str, "5752952621:AAGO61IiffzN23YuXyv71fbDztA_ubGM6qo"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 5]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, False]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[5500572462]]
        OWNER_ID = [int, 0]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,""]
        FORCEJOIN_ID = [int,0]

        TRACE_CHANNEL = [int, 0]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
