from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.haydovchi_reys.haydovchi_reys_tugmalar import tax_resy_vil
from keyboards.inline.yolovchi.callback_data import menu_callback
from loader import dp

@dp.callback_query_handler(menu_callback.filter(item_name='yolovchikerak'))
async def yolovchi_kerak(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Qaysi viloyatdan yo'lovchi kerak ? ",reply_markup=tax_resy_vil)