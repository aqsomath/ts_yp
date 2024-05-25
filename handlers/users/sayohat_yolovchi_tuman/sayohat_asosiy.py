from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from states.sayohat_states import Sayohat_andijon

from keyboards.inline.sayohat_qilish.sayohat_viloyatlar import sayohat_vil
from keyboards.inline.yolovchi.callback_data import menu_callback
from loader import dp, db


@dp.callback_query_handler(menu_callback.filter(item_name='sayohatgamashina'))
async def sayohat_asosiy(call:CallbackQuery,state:FSMContext):
        last_get_orders = await db.get_order_joined_in_last_day_2()
        count = []
        for order in last_get_orders:
                if order[1] == call.from_user.id:
                        count.append(call.from_user.id)
        if len(count) > 3:
                await call.message.answer("Kechirasiz bugungi limitingiz tugadi !")
        else:
                await call.message.answer("Qaysi viloyatdan sayohatga chiqmoqchisiz ? ", reply_markup=sayohat_vil)
                await Sayohat_andijon.asosiy.set()
                await call.message.delete()