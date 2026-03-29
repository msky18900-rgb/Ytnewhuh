import os


class Config:

    BOT_TOKEN = os.environ.get("8646298365:AAH95QvkjsTBW-IT78vvTxrSYqLpFQjWvTs")

    SESSION_NAME = os.environ.get("SESSION_NAME", "Newtester221Bot")

    API_ID = int(os.environ.get("36114630"))

    API_HASH = os.environ.get("eb058bb41fdd880a6aa81a5050025b69")

    CLIENT_ID = os.environ.get("268331620393-hni6mriqsknm8g437msmflm4lg8nkp73.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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")

    BOT_OWNER = int(os.environ.get("8001413907"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 374321319] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
