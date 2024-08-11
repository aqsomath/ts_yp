from aiogram.types import CallbackQuery
from states.yolovchi_pochta_statet import Pochta_andijon

from keyboards.inline.pochta_yuborish.pochta_yuborish_tugmalari import pochta_viloyatlar
from keyboards.inline.yolovchi.callback_data import menu_callback
from loader import dp, db


@dp.callback_query_handler(menu_callback.filter(item_name='pochtayuborishkerak'))
async def pochta(call:CallbackQuery):
        last_get_orders = await db.get_order_joined_in_last_day_2()
        count = []
        for order in last_get_orders:
                if order[1] == call.from_user.id:
                        count.append(call.from_user.id)
        if len(count) > 5:
                await call.message.answer("Kechirasiz bugungi limitingiz tugadi !")
        else:
                await call.message.answer("Qaysi viloyatdan pochta yubormoqchisiz ? ",reply_markup=pochta_viloyatlar)
                await Pochta_andijon.asosiy.set()
                await call.message.delete()