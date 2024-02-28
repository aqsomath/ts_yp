from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    if message.from_user.id == 6132434228:
        text = ("Buyruqlar: ",
                "/start - Botni ishga tushirish",
                "/help - Yordam",
                "/statics - botning statistikasi",
                )

        await message.answer("\n".join(text))
    else:
        text = ("Buyruqlar: ",
                "/start - Botni ishga tushirish",
                "/help - Yordam",
                )
        await message.answer("\n".join(text))
