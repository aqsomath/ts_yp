from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from keyboards.inline.tayyor_buyurtmalar.tayyor_pochta_keyboards import  buxoro_tayyor_massay, \
    fargona_tayyor_massay, namangan_tayyor_massay, sirdaryo_tayyor_massay, surxondaryo_tayyor_massay, \
    toshkent_tayyor_massay, qashqadaryo_tayyor_massay, xorazm_tayyor_massay, samarqand_tayyor_massay, \
    jizzax_tayyor_massay, navoiy_tayyor_massay, tayyor_massay_and
from keyboards.inline.yolovchi.callback_data import menu_callback
from loader import dp


massay_tayyor_callback_and = CallbackData("tayyor_pyukk_massayhii", "item_name")
viloyat = {
    "Andijon":"iuhgvds",
    "Namangan":"tdysui",
    "Farg'ona":"qpoxnsl",
    "Buxoro":"eydhsjnklx",
    "Toshkent":"s465x12az",
    "Sirdaryo":"aea4s4d",
    "Surxondaryo":"8d79s8d79",
    "Qashqadaryo":"weds45sd",
    "Xorazm":"egdjsklznn",
    "Navoiy":"w7e6dysi",
    "Jizzax":"e3ejwkd",
    "Samarqand":"87ds98cz",
}
yukss_tayin_vil = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat.items():
    yukss_tayin_vil.insert(InlineKeyboardButton(text=key, callback_data=massay_tayyor_callback_and.new(item_name=value)))


@dp.callback_query_handler(menu_callback.filter(item_name='tayyorsayohatgamashina'))
async def call_qur(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Qaysi viloyatdan sayohatchi mashina kerak ? ",reply_markup=yukss_tayin_vil)


@dp.callback_query_handler(massay_tayyor_callback_and.filter(item_name='iuhgvds'))
async def and_tayyor(call:CallbackQuery):
        await call.message.answer("Qaysi tumanidan sayohatchi mashina kerak ? ", reply_markup=tayyor_massay_and)
@dp.callback_query_handler(massay_tayyor_callback_and.filter(item_name='eydhsjnklx'))
async def and_tayyor(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi mashina kerak ? ", reply_markup=buxoro_tayyor_massay)

@dp.callback_query_handler(massay_tayyor_callback_and.filter(item_name='qpoxnsl'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi mashina kerak ? ",reply_markup=fargona_tayyor_massay)

@dp.callback_query_handler(massay_tayyor_callback_and.filter(item_name='tdysui'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi mashina kerak ? ",reply_markup=namangan_tayyor_massay)


@dp.callback_query_handler(massay_tayyor_callback_and.filter(item_name='aea4s4d'))
async def namangan_tayr(call: CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi mashina kerak ? ", reply_markup=sirdaryo_tayyor_massay)



@dp.callback_query_handler(massay_tayyor_callback_and.filter(item_name='8d79s8d79'))
async def namangan_tayr(call: CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi mashina kerak ? ", reply_markup=surxondaryo_tayyor_massay)

@dp.callback_query_handler(massay_tayyor_callback_and.filter(item_name='s465x12az'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi mashina kerak ? ",reply_markup=toshkent_tayyor_massay)


@dp.callback_query_handler(massay_tayyor_callback_and.filter(item_name='weds45sd'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi mashina kerak ? ",reply_markup=qashqadaryo_tayyor_massay)

@dp.callback_query_handler(massay_tayyor_callback_and.filter(item_name='egdjsklznn'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi mashina kerak ? ",reply_markup=xorazm_tayyor_massay)

@dp.callback_query_handler(massay_tayyor_callback_and.filter(item_name='87ds98cz'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi mashina kerak ? ",reply_markup=samarqand_tayyor_massay)


@dp.callback_query_handler(massay_tayyor_callback_and.filter(item_name='e3ejwkd'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi mashina kerak ? ",reply_markup=jizzax_tayyor_massay)

@dp.callback_query_handler(massay_tayyor_callback_and.filter(item_name='w7e6dysi'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan sayohatchi mashina kerak ? ",reply_markup=navoiy_tayyor_massay)