class Config:
    # === HARD-CODED VALUES ===
    BOT_TOKEN = "8646298365:AAH95QvkjsTBW-IT78vvTxrSYqLpFQjWvTs"
    SESSION_NAME = "Newtester221Bot"
    API_ID = 36114630
    API_HASH = "eb058bb41fdd880a6aa81a5050025b69"
    CLIENT_ID = "268331620393-hni6mriqsknm8g437msmflm4lg8nkp73.apps.googleusercontent.com"
    CLIENT_SECRET = "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"
    BOT_OWNER = 8001413907

    # === Computed / defaults (no environment variables needed) ===
    AUTH_USERS_TEXT = ""   # change this if you want to add more users via string
    AUTH_USERS = [BOT_OWNER, 374321319] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = ""
    VIDEO_CATEGORY = 0
    VIDEO_TITLE_PREFIX = ""
    VIDEO_TITLE_SUFFIX = ""

    DEBUG = False
    UPLOAD_MODE = False
    CRED_FILE = "auth_token.txt"
