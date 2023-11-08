# from environs import Env
#
# # environs kutubxonasidan foydalanish
# env = Env()
# env.read_env()
# # .env fayl ichidan quyidagilarni o'qiymiz
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# DB_USER=env.str("DB_USER")
# DB_PASS=env.str("DB_PASS")
# DB_HOST=env.str("DB_HOST")
# DB_NAME=env.str("DB_NAME")


import os

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))  # Bot token
ADMINS = list(os.environ.get("ADMINS"))  # adminlar ro'yxati
DB_USER = list(os.environ.get("DB_USER"))
DB_HOST = list(os.environ.get("DB_HOST"))
DB_NAME = list(os.environ.get("DB_NAME"))
DB_PASS = list(os.environ.get("DB_PASS"))