import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
     try:
            print("Ishga tushdim ..")

     except Exception as err:
            logging.exception(err)
