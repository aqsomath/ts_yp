from environs import Env
import os

#
# # environs kutubxonasidan foydalanish
env = Env()
env.read_env()
# # .env fayl ichidan quyidagilarni o'qiymiz

# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# BOT_TOKEN = env.str("BOT_TOKEN")  # adminlar ro'yxati
# DB_USER=env.str("DB_USER")
# DB_PASS=env.str("DB_PASS")
# DB_HOST=env.str("DB_HOST")
# DB_NAME=env.str("DB_NAME")


#
# # .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))  # Bot token
ADMINS = list(os.environ.get("ADMINS"))  # adminlar ro'yxati
DB_USER = str(os.environ.get("DB_USER"))
DB_HOST = str(os.environ.get("DB_HOST"))
DB_NAME = str(os.environ.get("DB_NAME"))
DB_PASS = str(os.environ.get("DB_PASS"))

