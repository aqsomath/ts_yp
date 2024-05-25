from aiogram.types import CallbackQuery

from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yuk_yuborish.yuk_tugmalari import yuk_viloyatlar
from loader import dp, db
from states.yuk_states import Yuk_xorazm


@dp.callback_query_handler(menu_callback.filter(item_name="yukyuborishkerak"))
async def yukyuborish(call:CallbackQuery):
        last_get_orders = await db.get_order_joined_in_last_day_2()
        count = []
        for order in last_get_orders:
                if order[1] == call.from_user.id:
                        count.append(call.from_user.id)
        if len(count) > 3:
                await call.message.answer("Kechirasiz bugungi limitingiz tugadi !")
        else:
                await call.message.answer("Yukni qaysi viloyatdan yuborasiz ?",reply_markup=yuk_viloyatlar)
                await Yuk_xorazm.asosiy.set()
                await call.message.delete()