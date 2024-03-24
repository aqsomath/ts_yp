from aiogram import types

from loader import db


async def set_default_commands(dp):


        commands = [
                types.BotCommand("start", "Botni ishga tushurish"),
                types.BotCommand("help", "Yordam"),
        ]

        await dp.bot.set_my_commands(commands)
