import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "your-token-here")
API_ID = int(os.getenv("API_ID", 123456))  # Get from my.telegram.org
API_HASH = os.getenv("API_HASH", "your-api-hash")
OWNER = type("OWNER", (), {"ID": int(os.getenv("OWNER_ID", 123456789))})
