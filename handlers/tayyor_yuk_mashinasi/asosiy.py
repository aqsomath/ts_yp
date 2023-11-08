from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from keyboards.inline.tayyor_buyurtmalar.tayyor_pochta_keyboards import  buxoro_tayyor_mashin, \
    fargona_tayyor_mashin, namangan_tayyor_mashin, sirdaryo_tayyor_mashin, surxondaryo_tayyor_mashin, \
    toshkent_tayyor_mashin, qashqadaryo_tayyor_mashin, xorazm_tayyor_mashin, samarqand_tayyor_mashin, \
    jizzax_tayyor_mashin, navoiy_tayyor_mashin, tayyor_mashin_and
from keyboards.inline.yolovchi.callback_data import menu_callback
from loader import dp


tayyor_yuk_mashinasi_callback = CallbackData("tayyor_pyukk_mashin_", "item_name")
viloyat = {
    "Andijon":"weffwfsdfsdfsfdsdfdsfsdf",
    "Namangan":".asksahadshashadshads",
    "Farg'ona":"dweiudiudcsdcbdcjsjchshkcakj",
    "Buxoro":"sliuffkadshfljadsgfjkds",
    "Toshkent":"sifuehfuyhhajdsaahdsvadhsadsvh4d6sdf4s6f4",
    "Sirdaryo":"edwdwdcsdcsdvsfvffv",
    "Surxondaryo":"6sd64s64d6s4d654cs64c6d4c6ds5c",
    "Qashqadaryo":"wewdedwed4wds545d45s4c54d",
    "Xorazm":"1d1d1sd11c1c1d11d1s1d1",
    "Navoiy":"s2s2d2s22f2d2de2w2w2w",
    "Jizzax":"3a3sas3as3a3s3c3ds3s3d3sd3sd33wew3e3w",
    "Samarqand":"as4a4s4d4s4d4sf44s4df4dg4fe4r4e4r",
}
yukss_tayin_vil = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat.items():
    yukss_tayin_vil.insert(InlineKeyboardButton(text=key, callback_data=tayyor_yuk_mashinasi_callback.new(item_name=value)))


@dp.callback_query_handler(menu_callback.filter(item_name='tayyoryukmashinasi'))
async def call_qur(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Yuk qaysi viloyatdan bo'lsin ? ",reply_markup=yukss_tayin_vil)


@dp.callback_query_handler(tayyor_yuk_mashinasi_callback.filter(item_name='weffwfsdfsdfsfdsdfdsfsdf'))
async def and_tayyor(call:CallbackQuery):
        await call.message.answer("Qaysi tumanidan yuk kerak ? ", reply_markup=tayyor_mashin_and)
@dp.callback_query_handler(tayyor_yuk_mashinasi_callback.filter(item_name='sliuffkadshfljadsgfjkds'))
async def and_tayyor(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ", reply_markup=buxoro_tayyor_mashin)

@dp.callback_query_handler(tayyor_yuk_mashinasi_callback.filter(item_name='dweiudiudcsdcbdcjsjchshkcakj'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ",reply_markup=fargona_tayyor_mashin)

@dp.callback_query_handler(tayyor_yuk_mashinasi_callback.filter(item_name='asksahadshashadshads'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ",reply_markup=namangan_tayyor_mashin)


@dp.callback_query_handler(tayyor_yuk_mashinasi_callback.filter(item_name='edwdwdcsdcsdvsfvffv'))
async def namangan_tayr(call: CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ", reply_markup=sirdaryo_tayyor_mashin)



@dp.callback_query_handler(tayyor_yuk_mashinasi_callback.filter(item_name='6sd64s64d6s4d654cs64c6d4c6ds5c'))
async def namangan_tayr(call: CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ", reply_markup=surxondaryo_tayyor_mashin)

@dp.callback_query_handler(tayyor_yuk_mashinasi_callback.filter(item_name='sifuehfuyhhajdsaahdsvadhsadsvh4d6sdf4s6f4'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ",reply_markup=toshkent_tayyor_mashin)


@dp.callback_query_handler(tayyor_yuk_mashinasi_callback.filter(item_name='wewdedwed4wds545d45s4c54d'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ",reply_markup=qashqadaryo_tayyor_mashin)

@dp.callback_query_handler(tayyor_yuk_mashinasi_callback.filter(item_name='1d1d1sd11c1c1d11d1s1d1'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ",reply_markup=xorazm_tayyor_mashin)

@dp.callback_query_handler(tayyor_yuk_mashinasi_callback.filter(item_name='as4a4s4d4s4d4sf44s4df4dg4fe4r4e4r'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ",reply_markup=samarqand_tayyor_mashin)


@dp.callback_query_handler(tayyor_yuk_mashinasi_callback.filter(item_name='3a3sas3as3a3s3c3ds3s3d3sd3sd33wew3e3w'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ",reply_markup=jizzax_tayyor_mashin)

@dp.callback_query_handler(tayyor_yuk_mashinasi_callback.filter(item_name='s2s2d2s22f2d2de2w2w2w'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan yuk kerak ? ",reply_markup=navoiy_tayyor_mashin)