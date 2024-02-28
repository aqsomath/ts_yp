from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from states.yuk_reys_states import Yuk_reys_andijon

from keyboards.inline.haydovchi_reys.haydovchi_yuk_reys import tax_yuk_vil, taxi_yuk_callback
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu_1
from loader import dp


@dp.callback_query_handler(menu_callback.filter(item_name='yukkerak'))
async def yuk_reys_asosiy(call:CallbackQuery):
    
        await call.message.answer("Qaysi viloyatlardan yuk olasiz ? ",reply_markup=tax_yuk_vil)
        await Yuk_reys_andijon.asosiy.set()
        await call.message.delete()
@dp.callback_query_handler(taxi_yuk_callback.filter(item_name='ortga'))
async def orga(call:CallbackQuery,state:FSMContext):
    
        await call.message.answer("Sizga kerakli xizmat turini tanlang !!!",reply_markup=umumiy_menu_1)
        await call.message.delete()
