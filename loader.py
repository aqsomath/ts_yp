from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils.db_api.postgresql import Database
bot = Bot(token='6896966695:AAGw8Gb8mgzHwB-eCVi8xrkOPaY0WHnn2FA', parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()