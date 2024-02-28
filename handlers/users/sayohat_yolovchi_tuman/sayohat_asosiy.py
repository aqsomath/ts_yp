from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from states.sayohat_states import Sayohat_andijon

from keyboards.inline.sayohat_qilish.sayohat_viloyatlar import sayohat_vil
from keyboards.inline.yolovchi.callback_data import menu_callback
from loader import dp


@dp.callback_query_handler(menu_callback.filter(item_name='sayohatgamashina'))
async def sayohat_asosiy(call:CallbackQuery,state:FSMContext):

        await call.message.answer("Qaysi viloyatdan sayohatga chiqmoqchisiz ? ", reply_markup=sayohat_vil)
        await Sayohat_andijon.asosiy.set()
        await call.message.delete()