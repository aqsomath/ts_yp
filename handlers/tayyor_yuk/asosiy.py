from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from keyboards.inline.tayyor_buyurtmalar.tayyor_pochta_keyboards import  buxoro_tayyor_yukbor, \
    fargona_tayyor_yukbor, namangan_tayyor_yukbor, sirdaryo_tayyor_yukbor, surxondaryo_tayyor_yukbor, \
    toshkent_tayyor_yukbor, qashqadaryo_tayyor_yukbor, xorazm_tayyor_yukbor, samarqand_tayyor_yukbor, \
    jizzax_tayyor_yukbor, navoiy_tayyor_yukbor, tayyor_yukbor_and
from keyboards.inline.yolovchi.callback_data import menu_callback
from loader import dp


yuk_tayyor_callback_and = CallbackData("tayyor_pyukk_", "item_name")
viloyat = {
    "Andijon":"asxasdasdas",
    "Namangan":".khcskgfkjsfkjdsdsdsdsdqqq",
    "Farg'ona":"kjdklshlw",
    "Buxoro":"s6dc6s54d6s54dfs8",
    "Toshkent":"5d46s4d6sdf4s6f4",
    "Sirdaryo":"qw6eqweqweq5we4",
    "Surxondaryo":"weds4f54sdf4s6",
    "Qashqadaryo":"vo5s5d4fsf54sdsdseasdsdsdm",
    "Xorazm":"sdfsd4sdadasdasdf545d4fs",
    "Navoiy":"d4sd5s5dfaaaaaa45f4s5df",
    "Jizzax":"6565d56s5asqw1212f6s5dsdfsdfsdfs",
    "Samarqand":"4ds5dfsdfs5swwewe45d5s6s6d42d",
}
yukss_tayin_vil = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat.items():
    yukss_tayin_vil.insert(InlineKeyboardButton(text=key, callback_data=yuk_tayyor_callback_and.new(item_name=value)))


@dp.callback_query_handler(menu_callback.filter(item_name='tayyoryuk'))
async def call_qur(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Yuk qaysi viloyatdan bo'lsin ? ",reply_markup=yukss_tayin_vil)


@dp.callback_query_handler(yuk_tayyor_callback_and.filter(item_name='asxasdasdas'))
async def and_tayyor(call:CallbackQuery):
        await call.message.answer("Qaysi tumanidan yuk kerak ? ", reply_markup=tayyor_yukbor_and)
@dp.callback_query_handler(yuk_tayyor_callback_and.filter(item_name='s6dc6s54d6s54dfs8'))
async def and_tayyor(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ", reply_markup=buxoro_tayyor_yukbor)

@dp.callback_query_handler(yuk_tayyor_callback_and.filter(item_name='kjdklshlw'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ",reply_markup=fargona_tayyor_yukbor)

@dp.callback_query_handler(yuk_tayyor_callback_and.filter(item_name='khcskgfkjsfkjdsdsdsdsdqqq'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ",reply_markup=namangan_tayyor_yukbor)


@dp.callback_query_handler(yuk_tayyor_callback_and.filter(item_name='qw6eqweqweq5we4'))
async def namangan_tayr(call: CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ", reply_markup=sirdaryo_tayyor_yukbor)



@dp.callback_query_handler(yuk_tayyor_callback_and.filter(item_name='weds4f54sdf4s6'))
async def namangan_tayr(call: CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ", reply_markup=surxondaryo_tayyor_yukbor)

@dp.callback_query_handler(yuk_tayyor_callback_and.filter(item_name='5d46s4d6sdf4s6f4'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ",reply_markup=toshkent_tayyor_yukbor)


@dp.callback_query_handler(yuk_tayyor_callback_and.filter(item_name='vo5s5d4fsf54sdsdseasdsdsdm'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ",reply_markup=qashqadaryo_tayyor_yukbor)

@dp.callback_query_handler(yuk_tayyor_callback_and.filter(item_name='sdfsd4sdadasdasdf545d4fs'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ",reply_markup=xorazm_tayyor_yukbor)

@dp.callback_query_handler(yuk_tayyor_callback_and.filter(item_name='4ds5dfsdfs5swwewe45d5s6s6d42d'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ",reply_markup=samarqand_tayyor_yukbor)


@dp.callback_query_handler(yuk_tayyor_callback_and.filter(item_name='6565d56s5asqw1212f6s5dsdfsdfsdfs'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ",reply_markup=jizzax_tayyor_yukbor)

@dp.callback_query_handler(yuk_tayyor_callback_and.filter(item_name='d4sd5s5dfaaaaaa45f4s5df'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ",reply_markup=navoiy_tayyor_yukbor)