from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
ADMINS = env.list("ADMINS")  # adminlar ro'yxati

DB_USER=env.str("DB_USER")
DB_PASS=env.str("DB_PASS")
DB_HOST=env.str("DB_HOST")
DB_NAME=env.str("DB_NAME")


