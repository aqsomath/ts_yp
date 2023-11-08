from aiogram.types import CallbackQuery

from keyboards.inline.haydovchi_reys.haydovchi_pochta_reys import tax_pochta_vil
from keyboards.inline.yolovchi.callback_data import menu_callback
from loader import dp


@dp.callback_query_handler(menu_callback.filter(item_name='pochtakerak'))
async def yuk_reys_asosiy(call:CallbackQuery):
    await call.message.answer("Qaysi viloyatlardan pochta olasiz ? ",reply_markup=tax_pochta_vil)
