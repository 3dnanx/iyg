from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from pyro import validate_session

# ضع القيم الخاصة بك هنا مباشرة
APP_ID = 24464838
# ضع هنا الـ APP_ID الخاص بك كرقم صحيح
APP_HASH = "15acca41a7d564edeb681bb267acfdff"
# ضع هنا الـ APP_HASH كسلسلة نصية
ss = "1BJWap1sAUFpJapT6uWw5YlXnPHns_LofRSlr8MN4JT7C3sxWLeoOi8ECWFx9D3e8oZ8fFNe5zhvxcuBUVuhnVGtQbDJL7UT5SiAt2tMdVXRUu-bzUXqtFECdFjiQkAE5DFefZEzsQyg6KGlSOIXMF3X6lDJDCE7-S3aY-x53-j-LLR2zrIEbWht7ZbfgvqzFyOAJD2pGxGNXh0-Ih-z8i63pbT2V4Lc6L3ZewxROOImRFvJgasZJ1ymCmxKzF2NN1hScOtizfQutKdD8cFZSfpPJw1S2xLQ6nVUxpyQ6R1iu9s0vvNmIWaTkbNCatCXeOs5ZINHyBB_MKj8WSveT-edHBlhY8KQ="
  # ضع هنا الـ String Session كنص

# التحقق من صحة الجلسة
session = validate_session(ss)

# إنشاء العميل
IEX = TelegramClient(StringSession(session), APP_ID, APP_HASH)

ispay = ['yes']

# إذا كنت تستخدم بوت، يمكنك تفعيل الأسطر التالية:
# BOT_USERNAME = "your_bot_username"
# token = "your_bot_token"
# bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
# bot.start()
