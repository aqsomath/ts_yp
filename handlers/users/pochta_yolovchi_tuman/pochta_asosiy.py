from aiogram.types import CallbackQuery
from states.yolovchi_pochta_statet import Pochta_andijon

from keyboards.inline.pochta_yuborish.pochta_yuborish_tugmalari import pochta_viloyatlar
from keyboards.inline.yolovchi.callback_data import menu_callback
from loader import dp


@dp.callback_query_handler(menu_callback.filter(item_name='pochtayuborishkerak'))
async def pochta(call:CallbackQuery):
        await call.message.answer("Qaysi viloyatdan pochta yubormoqchisiz ? ",reply_markup=pochta_viloyatlar)
        await Pochta_andijon.asosiy.set()
        await call.message.delete()