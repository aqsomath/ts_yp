from aiogram.types import CallbackQuery

from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yuk_yuborish.yuk_tugmalari import yuk_viloyatlar
from loader import dp
from states.yuk_states import Yuk_xorazm


@dp.callback_query_handler(menu_callback.filter(item_name="yukyuborishkerak"))
async def yukyuborish(call:CallbackQuery):

        await call.message.answer("Yukni qaysi viloyatdan yuborasiz ?",reply_markup=yuk_viloyatlar)
        await Yuk_xorazm.asosiy.set()
        await call.message.delete()