from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from keyboards.inline.tayyor_buyurtmalar.tayyor_pochta_keyboards import  buxoro_tayyor_yolovc, \
    fargona_tayyor_yolovc, namangan_tayyor_yolovc, sirdaryo_tayyor_yolovc, surxondaryo_tayyor_yolovc, \
    toshkent_tayyor_yolovc, qashqadaryo_tayyor_yolovc, xorazm_tayyor_yolovc, samarqand_tayyor_yolovc, \
    jizzax_tayyor_yolovc, navoiy_tayyor_yolovc, tayyor_yolovc_and
from keyboards.inline.yolovchi.callback_data import menu_callback
from loader import dp


yolovchi_tayyor_callback_and = CallbackData("tayyor_pyukk_yolovchii", "item_name")
viloyat = {
    "Andijon":"yusyw",
    "Namangan":"ewee32212",
    "Farg'ona":"2323rdewew",
    "Buxoro":"121eweds",
    "Toshkent":"09esadedefd",
    "Sirdaryo":"2002kkj",
    "Surxondaryo":"122ooei",
    "Qashqadaryo":"565sjwhw",
    "Xorazm":"weiut62",
    "Navoiy":"989djdhsk",
    "Jizzax":"89weujas",
    "Samarqand":"e2d55s4d4d",
}
yukss_tayin_vil = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat.items():
    yukss_tayin_vil.insert(InlineKeyboardButton(text=key, callback_data=yolovchi_tayyor_callback_and.new(item_name=value)))


@dp.callback_query_handler(menu_callback.filter(item_name='tayyoryolovchi'))
async def call_qur(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Qaysi viloyatdan yo'lovchi kerak ? ",reply_markup=yukss_tayin_vil)


@dp.callback_query_handler(yolovchi_tayyor_callback_and.filter(item_name='yusyw'))
async def and_tayyor(call:CallbackQuery):
        await call.message.answer("Qaysi tumanidan yo'lovchi kerak ? ", reply_markup=tayyor_yolovc_and)
@dp.callback_query_handler(yolovchi_tayyor_callback_and.filter(item_name='121eweds'))
async def and_tayyor(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yo'lovchi kerak ? ", reply_markup=buxoro_tayyor_yolovc)

@dp.callback_query_handler(yolovchi_tayyor_callback_and.filter(item_name='2323rdewew'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yo'lovchi kerak ? ",reply_markup=fargona_tayyor_yolovc)

@dp.callback_query_handler(yolovchi_tayyor_callback_and.filter(item_name='ewee32212'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yo'lovchi kerak ? ",reply_markup=namangan_tayyor_yolovc)


@dp.callback_query_handler(yolovchi_tayyor_callback_and.filter(item_name='2002kkj'))
async def namangan_tayr(call: CallbackQuery):
    await call.message.answer("Qaysi tumanidan yo'lovchi kerak ? ", reply_markup=sirdaryo_tayyor_yolovc)



@dp.callback_query_handler(yolovchi_tayyor_callback_and.filter(item_name='122ooei'))
async def namangan_tayr(call: CallbackQuery):
    await call.message.answer("Qaysi tumanidan yo'lovchi kerak ? ", reply_markup=surxondaryo_tayyor_yolovc)

@dp.callback_query_handler(yolovchi_tayyor_callback_and.filter(item_name='09esadedefd'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yo'lovchi kerak ? ",reply_markup=toshkent_tayyor_yolovc)


@dp.callback_query_handler(yolovchi_tayyor_callback_and.filter(item_name='565sjwhw'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yo'lovchi kerak ? ",reply_markup=qashqadaryo_tayyor_yolovc)

@dp.callback_query_handler(yolovchi_tayyor_callback_and.filter(item_name='weiut62'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yo'lovchi kerak ? ",reply_markup=xorazm_tayyor_yolovc)

@dp.callback_query_handler(yolovchi_tayyor_callback_and.filter(item_name='e2d55s4d4d'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yo'lovchi kerak ? ",reply_markup=samarqand_tayyor_yolovc)


@dp.callback_query_handler(yolovchi_tayyor_callback_and.filter(item_name='89weujas'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yo'lovchi kerak ? ",reply_markup=jizzax_tayyor_yolovc)

@dp.callback_query_handler(yolovchi_tayyor_callback_and.filter(item_name='989djdhsk'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yo'lovchi kerak ? ",reply_markup=navoiy_tayyor_yolovc)