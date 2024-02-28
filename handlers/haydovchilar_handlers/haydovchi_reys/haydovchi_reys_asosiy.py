from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from states.haydovchi_reys_states import Reys_andijon

from keyboards.inline.haydovchi_reys.haydovchi_reys_tugmalar import tax_resy_vil, taxi_reys_callback
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu_1
from loader import dp


@dp.callback_query_handler(menu_callback.filter(item_name='yolovchikerak'))
async def yolovchi_kerak(call:CallbackQuery,state:FSMContext):
    
        await call.message.answer("Qaysi viloyatdan yo'lovchi kerak ? ",reply_markup=tax_resy_vil)
        await Reys_andijon.asosiy.set()
        await call.message.delete()
@dp.callback_query_handler(taxi_reys_callback.filter(item_name='hdisdjsdhk'))
async def orga(call:CallbackQuery,state:FSMContext):
    
        await call.message.answer("Sizga kerakli xizmat turini tanlang !!!",reply_markup=umumiy_menu_1)
        await call.message.delete()
