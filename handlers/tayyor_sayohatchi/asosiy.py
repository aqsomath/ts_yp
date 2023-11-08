from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from keyboards.inline.tayyor_buyurtmalar.tayyor_pochta_keyboards import  buxoro_tayyor_sayyoh, \
    fargona_tayyor_sayyoh, namangan_tayyor_sayyoh, sirdaryo_tayyor_sayyoh, surxondaryo_tayyor_sayyoh, \
    toshkent_tayyor_sayyoh, qashqadaryo_tayyor_sayyoh, xorazm_tayyor_sayyoh, samarqand_tayyor_sayyoh, \
    jizzax_tayyor_sayyoh, navoiy_tayyor_sayyoh, tayyor_sayyoh_and
from keyboards.inline.yolovchi.callback_data import menu_callback
from loader import dp


sayohatchi_tayyor_callback_and = CallbackData("tayyor_pyukk_sayyohhii", "item_name")
viloyat = {
    "Andijon":"eruidsxm",
    "Namangan":"dsjkl",
    "Farg'ona":"wpdkcn",
    "Buxoro":"ncdjkew",
    "Toshkent":"9q8w7e",
    "Sirdaryo":"f4d5s6a",
    "Surxondaryo":"t9f5c1x",
    "Qashqadaryo":"q75s23x",
    "Xorazm":"a1s2d5re8ds5",
    "Navoiy":"de7w85a2sxdF",
    "Jizzax":"9q8we75a6sd4s",
    "Samarqand":"rueiwodjfn",
}
yukss_tayin_vil = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat.items():
    yukss_tayin_vil.insert(InlineKeyboardButton(text=key, callback_data=sayohatchi_tayyor_callback_and.new(item_name=value)))


@dp.callback_query_handler(menu_callback.filter(item_name='tayyorsayohatchi'))
async def call_qur(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Qaysi viloyatdan sayohatchi kerak ? ",reply_markup=yukss_tayin_vil)


@dp.callback_query_handler(sayohatchi_tayyor_callback_and.filter(item_name='eruidsxm'))
async def and_tayyor(call:CallbackQuery):
        await call.message.answer("Qaysi tumanidan sayohatchi kerak ? ", reply_markup=tayyor_sayyoh_and)
@dp.callback_query_handler(sayohatchi_tayyor_callback_and.filter(item_name='ncdjkew'))
async def and_tayyor(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi kerak ? ", reply_markup=buxoro_tayyor_sayyoh)

@dp.callback_query_handler(sayohatchi_tayyor_callback_and.filter(item_name='wpdkcn'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi kerak ? ",reply_markup=fargona_tayyor_sayyoh)

@dp.callback_query_handler(sayohatchi_tayyor_callback_and.filter(item_name='dsjkl'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi kerak ? ",reply_markup=namangan_tayyor_sayyoh)


@dp.callback_query_handler(sayohatchi_tayyor_callback_and.filter(item_name='f4d5s6a'))
async def namangan_tayr(call: CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi kerak ? ", reply_markup=sirdaryo_tayyor_sayyoh)



@dp.callback_query_handler(sayohatchi_tayyor_callback_and.filter(item_name='t9f5c1x'))
async def namangan_tayr(call: CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi kerak ? ", reply_markup=surxondaryo_tayyor_sayyoh)

@dp.callback_query_handler(sayohatchi_tayyor_callback_and.filter(item_name='9q8w7e'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi kerak ? ",reply_markup=toshkent_tayyor_sayyoh)


@dp.callback_query_handler(sayohatchi_tayyor_callback_and.filter(item_name='q75s23x'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi kerak ? ",reply_markup=qashqadaryo_tayyor_sayyoh)

@dp.callback_query_handler(sayohatchi_tayyor_callback_and.filter(item_name='a1s2d5re8ds5'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi kerak ? ",reply_markup=xorazm_tayyor_sayyoh)

@dp.callback_query_handler(sayohatchi_tayyor_callback_and.filter(item_name='rueiwodjfn'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi kerak ? ",reply_markup=samarqand_tayyor_sayyoh)


@dp.callback_query_handler(sayohatchi_tayyor_callback_and.filter(item_name='9q8we75a6sd4s'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi kerak ? ",reply_markup=jizzax_tayyor_sayyoh)

@dp.callback_query_handler(sayohatchi_tayyor_callback_and.filter(item_name='de7w85a2sxdF'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi kerak ? ",reply_markup=navoiy_tayyor_sayyoh)