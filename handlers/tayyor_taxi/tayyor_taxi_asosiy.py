import random

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery,InlineKeyboardMarkup,InlineKeyboardButton

from handlers.haydovchilar_handlers.haydovchi_reys.hardovchi_reys_andijon import Hammasi, messages_drive
from keyboards.inline.haydovchi_reys.tayyor_taxi_keyboards import tax_tayin_vil, taxi_tayyor_callback, toshkent_tayyor, \
    surxondaryo_tayyor, sirdaryo_tayyor, namangan_tayyor, fargona_tayyor, buxoro_tayyor, tayyor_and, qashqadaryo_tayyor, \
    xorazm_tayyor, samarqand_tayyor, jizzax_tayyor, navoiy_tayyor
from keyboards.inline.yolovchi.callback_data import menu_callback
from keyboards.inline.yolovchi.kirish import umumiy_menu
from loader import dp, bot


next_back = InlineKeyboardMarkup(row_width=2)
next_back.insert(InlineKeyboardButton(text='🔙 Ortga', callback_data='back_for'))
next_back.insert(InlineKeyboardButton(text='Keyingisi 🔜', callback_data='next_for'))
next_back.insert(InlineKeyboardButton(text='Qabul qilish 📝', callback_data='qabul_qilish'))
next_back.insert(InlineKeyboardButton(text='Filtrlash 🔍', callback_data='filtrlash'))
next_back.insert(InlineKeyboardButton(text='Asosiy menu 📱', callback_data='asosiymenu'))





@dp.callback_query_handler(menu_callback.filter(item_name='tayyortaksi'))
@dp.callback_query_handler(text='next_for')
@dp.callback_query_handler(text='back_for')
async def tayyor_axi(call:CallbackQuery,state:FSMContext):
    if len(messages_drive)==0:
        await call.message.answer("Hozircha tayyor taxilar yo'q",reply_markup=next_back)
    else:
        x = random.randint(0, len(messages_drive)-1)
        await state.update_data(
            {
                "x":x
            }
        )
        await call.message.answer(messages_drive[x][0],reply_markup=next_back)



@dp.callback_query_handler(text='qabul_qilish')
async def tayyor_axi(call:CallbackQuery,state:FSMContext):
    data= await state.get_data()
    x = data.get('x')
    await call.message.answer(messages_drive[x][1])
    await state.finish()

@dp.callback_query_handler(text=['asosiymenu','asosiy'])
async def qayt(call:CallbackQuery):
    await call.message.answer("Sizga kerakli xizmat turini belgilang.",reply_markup=umumiy_menu)


@dp.callback_query_handler(text=['filtrlash'])
async def filtrlash(call:CallbackQuery):
    await call.message.answer("Qaysi viloyatdan taxi kerak",reply_markup=tax_tayin_vil)


@dp.callback_query_handler(taxi_tayyor_callback.filter(item_name='raz'))
async def and_tayyor(call:CallbackQuery):
        await call.message.answer("Qaysi tumanidan taxi kerak ? ", reply_markup=tayyor_and)
@dp.callback_query_handler(taxi_tayyor_callback.filter(item_name='chitiri'))
async def and_tayyor(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan taxi kerak ? ", reply_markup=buxoro_tayyor)

@dp.callback_query_handler(taxi_tayyor_callback.filter(item_name='tri'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan taxi kerak ? ",reply_markup=fargona_tayyor)

@dp.callback_query_handler(taxi_tayyor_callback.filter(item_name='dva'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan taxi kerak ? ",reply_markup=namangan_tayyor)


@dp.callback_query_handler(taxi_tayyor_callback.filter(item_name='shest'))
async def namangan_tayr(call: CallbackQuery):
    await call.message.answer("Qaysi tumanidan taxi kerak ? ", reply_markup=sirdaryo_tayyor)



@dp.callback_query_handler(taxi_tayyor_callback.filter(item_name='sem'))
async def namangan_tayr(call: CallbackQuery):
    await call.message.answer("Qaysi tumanidan taxi kerak ? ", reply_markup=surxondaryo_tayyor)

@dp.callback_query_handler(taxi_tayyor_callback.filter(item_name='pyat'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan taxi kerak ? ",reply_markup=toshkent_tayyor)


@dp.callback_query_handler(taxi_tayyor_callback.filter(item_name='vosem'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan taxi kerak ? ",reply_markup=qashqadaryo_tayyor)

@dp.callback_query_handler(taxi_tayyor_callback.filter(item_name='devit'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan taxi kerak ? ",reply_markup=xorazm_tayyor)

@dp.callback_query_handler(taxi_tayyor_callback.filter(item_name='dvinatsad'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan taxi kerak ? ",reply_markup=samarqand_tayyor)


@dp.callback_query_handler(taxi_tayyor_callback.filter(item_name='adinatsat'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan taxi kerak ? ",reply_markup=jizzax_tayyor)

@dp.callback_query_handler(taxi_tayyor_callback.filter(item_name='desit'))
async def namangan_tayr(call:CallbackQuery):
    await call.message.answer("Qaysi tumanidan taxi kerak ? ",reply_markup=navoiy_tayyor)