from aiogram.types import CallbackQuery

from keyboards.inline.haydovchi_reys.haydovchi_sayohatchi_reys import tax_say_vil
from keyboards.inline.haydovchi_reys.haydovchi_yuk_reys import tax_yuk_vil
from keyboards.inline.yolovchi.callback_data import menu_callback
from loader import dp
from states.haydovchi_sayohat_reys_states import Hay_say_andijon


@dp.callback_query_handler(menu_callback.filter(item_name='sayohatgayolovchi'))
async def yuk_reys_asosiy(call:CallbackQuery):
        await call.message.answer("Qaysi viloyatlardan sayohatchi olasiz ? ",reply_markup=tax_say_vil)
        await Hay_say_andijon.asosiy.set()
        await call.message.delete()
