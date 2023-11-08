from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from keyboards.inline.tayyor_buyurtmalar.tayyor_pochta_keyboards import tayyor_pochta_and, buxoro_tayyor_pochta, \
    fargona_tayyor_pochta, namangan_tayyor_pochta, sirdaryo_tayyor_pochta, surxondaryo_tayyor_pochta, \
    toshkent_tayyor_pochta, qashqadaryo_tayyor_pochta, xorazm_tayyor_pochta, samarqand_tayyor_pochta, \
    jizzax_tayyor_pochta, navoiy_tayyor_pochta
from keyboards.inline.yolovchi.callback_data import menu_callback
from loader import dp, bot


pochta_tayyor_callback_and = CallbackData("tayyor_pchta_", "item_name")
viloyat = {
    "Andijon":"asxasdasdasdasda",
    "Namangan":".khcskgfkjsfkjds",
    "Farg'ona":"kjdklshlwkekdcsdnc",
    "Buxoro":"s6dc6s54d6s54dfs8f798ds",
    "Toshkent":"5d46s4d6sdf4s6f4s6df46",
    "Sirdaryo":"qw6eqweqweq5we4wewq",
    "Surxondaryo":"weds4f54sdf4s6as6",
    "Qashqadaryo":"vo5s5d4fsf54sdsdsem",
    "Xorazm":"sdfsd4f545d4fs",
    "Navoiy":"d4sd5s5df45f4s5df",
    "Jizzax":"6565d56s5f6s5dsdfsdfsdfs",
    "Samarqand":"4ds5dfsdfs545d5s6s6d42d",
}
pochta_tayin_vil = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat.items():
    pochta_tayin_vil.insert(InlineKeyboardButton(text=key, callback_data=pochta_tayyor_callback_and.new(item_name=value)))


@dp.callback_query_handler(menu_callback.filter(item_name='tayyorpochta'))
async def call_qur(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Pochta qaysi viloyatdan bo'lsin ? ",reply_markup=pochta_tayin_vil)


@dp.callback_query_handler(pochta_tayyor_callback_and.filter(item_name='asxasdasdasdasda'))
async def and_tayyor(call:CallbackQuery):
        await call.message.answer("Qaysi tumanidan pochta kerak ? ", reply_markup=tayyor_pochta_and)
@dp.callback_query_handler(pochta_tayyor_callback_and.filter(item_name='s6dc6s54d6s54dfs8f798ds'))
async def and_tayyor(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ", reply_markup=buxoro_tayyor_pochta)

@dp.callback_query_handler(pochta_tayyor_callback_and.filter(item_name='kjdklshlwkekdcsdnc'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ",reply_markup=fargona_tayyor_pochta)

@dp.callback_query_handler(pochta_tayyor_callback_and.filter(item_name='khcskgfkjsfkjds'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ",reply_markup=namangan_tayyor_pochta)


@dp.callback_query_handler(pochta_tayyor_callback_and.filter(item_name='qw6eqweqweq5we4wewq'))
async def namangan_tayr(call: CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ", reply_markup=sirdaryo_tayyor_pochta)



@dp.callback_query_handler(pochta_tayyor_callback_and.filter(item_name='weds4f54sdf4s6as6'))
async def namangan_tayr(call: CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ", reply_markup=surxondaryo_tayyor_pochta)

@dp.callback_query_handler(pochta_tayyor_callback_and.filter(item_name='5d46s4d6sdf4s6f4s6df46'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ",reply_markup=toshkent_tayyor_pochta)


@dp.callback_query_handler(pochta_tayyor_callback_and.filter(item_name='vo5s5d4fsf54sdsdsem'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ",reply_markup=qashqadaryo_tayyor_pochta)

@dp.callback_query_handler(pochta_tayyor_callback_and.filter(item_name='sdfsd4f545d4fs'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ",reply_markup=xorazm_tayyor_pochta)

@dp.callback_query_handler(pochta_tayyor_callback_and.filter(item_name='4ds5dfsdfs545d5s6s6d42d'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ",reply_markup=samarqand_tayyor_pochta)


@dp.callback_query_handler(pochta_tayyor_callback_and.filter(item_name='6565d56s5f6s5dsdfsdfsdfs'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ",reply_markup=jizzax_tayyor_pochta)

@dp.callback_query_handler(pochta_tayyor_callback_and.filter(item_name='d4sd5s5df45f4s5df'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ",reply_markup=navoiy_tayyor_pochta)