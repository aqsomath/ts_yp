from aiogram.types import CallbackQuery

from keyboards.inline.haydovchi_reys.haydovchi_yuk_reys import tax_yuk_vil
from keyboards.inline.yolovchi.callback_data import menu_callback
from loader import dp


@dp.callback_query_handler(menu_callback.filter(item_name='yukkerak'))
async def yuk_reys_asosiy(call:CallbackQuery):
    await call.message.answer("Qaysi viloyatlardan yuk olasiz ? ",reply_markup=tax_yuk_vil)
