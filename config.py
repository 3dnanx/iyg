from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from pyro import validate_session

# ضع القيم الخاصة بك هنا مباشرة
APP_ID = 23035518
# ضع هنا الـ APP_ID الخاص بك كرقم صحيح
APP_HASH = "038341bd1a28b4cd0c6ca8802d94fb4d"
# ضع هنا الـ APP_HASH كسلسلة نصية
ss = "1BJWap1sAUFosxIHlA-jYLvxNS8uuybvvXkLZQbbCvZA5yuhF6aPGuEFz-UnS0_T8UN0iB0O8NQ6fXWE2wWHwbzK1tB4ZajgH6Z9IX284PCRdbGYe6iuAc1hPxczqwPd1_gPgxi2NhUBWQW0WICx_sKa9zk5Bt9vhJtq-OleMi6HtrTWjH8-U6jHxKDYTBWEjVd3Q_vkenul13Ll-psSt9REJ7R5HQkIY_XbBUZjxsJ-IN9IteoCgFXKB4Zcj263n7hqW-7Jc_yXLBB_89AwVZWBKifaZFAyxJqltrTKxCxCwRH0rshAFonqysEmza4d2Ni8M1WtiVp3q5D9nbJR3uitVz5M-2SI="
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
