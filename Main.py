import os
from dotenv import load_dotenv
from pyrogram import Client

# بارکردنی فایل .env
load_dotenv()

# وەرگرتنی API و توکنەکان لە فایل .env
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# دەستپێکردنی بۆت
app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ڕاکێشانی بۆت
app.run()
