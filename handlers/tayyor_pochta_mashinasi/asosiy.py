from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from keyboards.inline.tayyor_buyurtmalar.tayyor_pochta_keyboards import  buxoro_tayyor_pocmas, \
    fargona_tayyor_pocmas, namangan_tayyor_pocmas, sirdaryo_tayyor_pocmas, surxondaryo_tayyor_pocmas, \
    toshkent_tayyor_pocmas, qashqadaryo_tayyor_pocmas, xorazm_tayyor_pocmas, samarqand_tayyor_pocmas, \
    jizzax_tayyor_pocmas, navoiy_tayyor_pocmas, tayyor_pocmas_and
from keyboards.inline.yolovchi.callback_data import menu_callback
from loader import dp


pochta_mashina_tayyor_callback_and = CallbackData("tayyor_pochta_mashina", "item_name")
viloyat = {
    "Andijon":"susdf",
    "Namangan":"aslasjlakjslk",
    "Farg'ona":"askjdoie",
    "Buxoro":"krejhgihf",
    "Toshkent":"sdkhriuewuw98w",
    "Sirdaryo":"wuery73y8237",
    "Surxondaryo":"32r788ewdhfkjd",
    "Qashqadaryo":"4r98wefkdjfklj",
    "Xorazm":"r3498fufn",
    "Navoiy":"03eofoefndfs",
    "Jizzax":"fehfidckscnslkdj",
    "Samarqand":"5sd66sc6s4dc4s",
}
yukss_tayin_vil = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat.items():
    yukss_tayin_vil.insert(InlineKeyboardButton(text=key, callback_data=pochta_mashina_tayyor_callback_and.new(item_name=value)))


@dp.callback_query_handler(menu_callback.filter(item_name='tayyorpochtamashinasi'))
async def call_qur(call:CallbackQuery,state:FSMContext):
    await call.message.answer("Qaysi viloyatdan pochta kerak ? ",reply_markup=yukss_tayin_vil)


@dp.callback_query_handler(pochta_mashina_tayyor_callback_and.filter(item_name='susdf'))
async def and_tayyor(call:CallbackQuery):
        await call.message.answer("Qaysi tumanidan pochta kerak ? ", reply_markup=tayyor_pocmas_and)
@dp.callback_query_handler(pochta_mashina_tayyor_callback_and.filter(item_name='krejhgihf'))
async def and_tayyor(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ", reply_markup=buxoro_tayyor_pocmas)

@dp.callback_query_handler(pochta_mashina_tayyor_callback_and.filter(item_name='askjdoie'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ",reply_markup=fargona_tayyor_pocmas)

@dp.callback_query_handler(pochta_mashina_tayyor_callback_and.filter(item_name='aslasjlakjslk'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ",reply_markup=namangan_tayyor_pocmas)


@dp.callback_query_handler(pochta_mashina_tayyor_callback_and.filter(item_name='wuery73y8237'))
async def namangan_tayr(call: CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ", reply_markup=sirdaryo_tayyor_pocmas)



@dp.callback_query_handler(pochta_mashina_tayyor_callback_and.filter(item_name='32r788ewdhfkjd'))
async def namangan_tayr(call: CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ", reply_markup=surxondaryo_tayyor_pocmas)

@dp.callback_query_handler(pochta_mashina_tayyor_callback_and.filter(item_name='sdkhriuewuw98w'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ",reply_markup=toshkent_tayyor_pocmas)


@dp.callback_query_handler(pochta_mashina_tayyor_callback_and.filter(item_name='4r98wefkdjfklj'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ",reply_markup=qashqadaryo_tayyor_pocmas)

@dp.callback_query_handler(pochta_mashina_tayyor_callback_and.filter(item_name='r3498fufn'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ",reply_markup=xorazm_tayyor_pocmas)

@dp.callback_query_handler(pochta_mashina_tayyor_callback_and.filter(item_name='5sd66sc6s4dc4s'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ",reply_markup=samarqand_tayyor_pocmas)


@dp.callback_query_handler(pochta_mashina_tayyor_callback_and.filter(item_name='fehfidckscnslkdj'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ",reply_markup=jizzax_tayyor_pocmas)

@dp.callback_query_handler(pochta_mashina_tayyor_callback_and.filter(item_name='03eofoefndfs'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan pochta kerak ? ",reply_markup=navoiy_tayyor_pocmas)