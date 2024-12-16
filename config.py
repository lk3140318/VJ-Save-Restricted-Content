import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24335028"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "b204ec833fb451fb913fc8e683b232d0")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5213073489"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://aadarshkumar1234768:Q8ptH5spkMkR93eg@cluster0.0ntbfcn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "aadarshkumar1234768")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
