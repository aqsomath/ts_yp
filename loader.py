import asyncio

from aiogram import Bot, Dispatcher, types,filters
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.postgresql import Database





import random
import aiolimiter
import asyncio

MESSAGE_CAP_PER_ITER = 28

limiter = aiolimiter.AsyncLimiter(MESSAGE_CAP_PER_ITER, 1)









bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()

