from loader import dp
from aiogram.types import CallbackQuery
from keyboards.inline.yolovchi.callback_data import  viloyatlar_callback,navoiy_callback
from keyboards.inline.yolovchi.navoiytuman import navoiy_tumanlari

Konimex={*()}
Karmana={*()}
Qiziltepa={*()}
Xatirchi={*()}
Navbahor={*()}
Nurota={*()}
Tomdi={*()}
Uchquduq={*()}
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='voyy'))
async def xorazm_edit(call: CallbackQuery):
    await call.message.answer("Navoiy viloyati tumanlari ", reply_markup=navoiy_tumanlari)
    Konimex.add(call.message.chat.id)
    Karmana.add(call.message.chat.id)
    Qiziltepa.add(call.message.chat.id)
    Xatirchi.add(call.message.chat.id)
    Navbahor.add(call.message.chat.id)
    Nurota.add(call.message.chat.id)
    Tomdi.add(call.message.chat.id)
    Uchquduq.add(call.message.chat.id)

@dp.callback_query_handler(navoiy_callback.filter(item_name='konimex'))
async def chortoq(call: CallbackQuery):
    Konimex.remove(call.message.chat.id)

    navoiy_tumanlari['inline_keyboard'][0][0]['text'] = "❌ Konimex"
    navoiy_tumanlari['inline_keyboard'][0][0]['callback_data'] = "course:komi"
    await call.message.edit_reply_markup(navoiy_tumanlari)

@dp.callback_query_handler(navoiy_callback.filter(item_name='komi'))
async def chortoq(call: CallbackQuery):
    Konimex.add(call.message.chat.id)

    navoiy_tumanlari['inline_keyboard'][0][0]['text'] = "✅ Konimex"
    navoiy_tumanlari['inline_keyboard'][0][0]['callback_data'] = "course:konimex"
    await call.message.edit_reply_markup(navoiy_tumanlari)


@dp.callback_query_handler(navoiy_callback.filter(item_name='karmana'))
async def chortoq(call: CallbackQuery):
    Karmana.remove(call.message.chat.id)

    navoiy_tumanlari['inline_keyboard'][0][1]['text'] = "❌ Karmana"
    navoiy_tumanlari['inline_keyboard'][0][1]['callback_data'] = "course:karma"
    await call.message.edit_reply_markup(navoiy_tumanlari)

@dp.callback_query_handler(navoiy_callback.filter(item_name='karma'))
async def chortoq(call: CallbackQuery):
    Karmana.add(call.message.chat.id)

    navoiy_tumanlari['inline_keyboard'][0][1]['text'] = "✅ Karmana"
    navoiy_tumanlari['inline_keyboard'][0][1]['callback_data'] = "course:karmana"
    await call.message.edit_reply_markup(navoiy_tumanlari)


@dp.callback_query_handler(navoiy_callback.filter(item_name='qiziltepa'))
async def chortoq(call: CallbackQuery):
    Qiziltepa.remove(call.message.chat.id)

    navoiy_tumanlari['inline_keyboard'][0][2]['text'] = "❌ Qiziltepa"
    navoiy_tumanlari['inline_keyboard'][0][2]['callback_data'] = "course:qizilte"
    await call.message.edit_reply_markup(navoiy_tumanlari)

@dp.callback_query_handler(navoiy_callback.filter(item_name='qizilte'))
async def chortoq(call: CallbackQuery):
    Qiziltepa.add(call.message.chat.id)

    navoiy_tumanlari['inline_keyboard'][0][2]['text'] = "✅ Qiziltepa"
    navoiy_tumanlari['inline_keyboard'][0][2]['callback_data'] = "course:qiziltepa"
    await call.message.edit_reply_markup(navoiy_tumanlari)



@dp.callback_query_handler(navoiy_callback.filter(item_name='xatirchi'))
async def chortoq(call: CallbackQuery):
    Xatirchi.remove(call.message.chat.id)

    navoiy_tumanlari['inline_keyboard'][0][3]['text'] = "❌ Xatirchi"
    navoiy_tumanlari['inline_keyboard'][0][3]['callback_data'] = "course:xatir"
    await call.message.edit_reply_markup(navoiy_tumanlari)

@dp.callback_query_handler(navoiy_callback.filter(item_name='xatir'))
async def chortoq(call: CallbackQuery):
    Xatirchi.add(call.message.chat.id)

    navoiy_tumanlari['inline_keyboard'][0][3]['text'] = "✅ Xatirchi"
    navoiy_tumanlari['inline_keyboard'][0][3]['callback_data'] = "course:xatirchi"
    await call.message.edit_reply_markup(navoiy_tumanlari)


@dp.callback_query_handler(navoiy_callback.filter(item_name='navbahor'))
async def chortoq(call: CallbackQuery):
    Navbahor.remove(call.message.chat.id)

    navoiy_tumanlari['inline_keyboard'][1][0]['text'] = "❌ Navbahor"
    navoiy_tumanlari['inline_keyboard'][1][0]['callback_data'] = "course:navba"
    await call.message.edit_reply_markup(navoiy_tumanlari)

@dp.callback_query_handler(navoiy_callback.filter(item_name='navba'))
async def chortoq(call: CallbackQuery):
    Navbahor.add(call.message.chat.id)

    navoiy_tumanlari['inline_keyboard'][1][0]['text'] = "✅ Navbahor"
    navoiy_tumanlari['inline_keyboard'][1][0]['callback_data'] = "course:navbahor"
    await call.message.edit_reply_markup(navoiy_tumanlari)


@dp.callback_query_handler(navoiy_callback.filter(item_name='nurota'))
async def chortoq(call: CallbackQuery):
    Nurota.remove(call.message.chat.id)

    navoiy_tumanlari['inline_keyboard'][1][1]['text'] = "❌ Nurota"
    navoiy_tumanlari['inline_keyboard'][1][1]['callback_data'] = "course:nuro"
    await call.message.edit_reply_markup(navoiy_tumanlari)

@dp.callback_query_handler(navoiy_callback.filter(item_name='nuro'))
async def chortoq(call: CallbackQuery):
    Nurota.add(call.message.chat.id)

    navoiy_tumanlari['inline_keyboard'][1][1]['text'] = "✅ Nurota"
    navoiy_tumanlari['inline_keyboard'][1][1]['callback_data'] = "course:nurota"
    await call.message.edit_reply_markup(navoiy_tumanlari)


@dp.callback_query_handler(navoiy_callback.filter(item_name='tomdi'))
async def chortoq(call: CallbackQuery):
    Tomdi.remove(call.message.chat.id)

    navoiy_tumanlari['inline_keyboard'][1][2]['text'] = "❌ Tomdi"
    navoiy_tumanlari['inline_keyboard'][1][2]['callback_data'] = "course:tomdii"
    await call.message.edit_reply_markup(navoiy_tumanlari)

@dp.callback_query_handler(navoiy_callback.filter(item_name='tomdii'))
async def chortoq(call: CallbackQuery):
    Tomdi.add(call.message.chat.id)

    navoiy_tumanlari['inline_keyboard'][1][2]['text'] = "✅ Tomdi"
    navoiy_tumanlari['inline_keyboard'][1][2]['callback_data'] = "course:tomdi"
    await call.message.edit_reply_markup(navoiy_tumanlari)



@dp.callback_query_handler(navoiy_callback.filter(item_name='uchquduq'))
async def chortoq(call: CallbackQuery):
    Uchquduq.remove(call.message.chat.id)

    navoiy_tumanlari['inline_keyboard'][1][3]['text'] = "❌ Uchquduq"
    navoiy_tumanlari['inline_keyboard'][1][3]['callback_data'] = "course:uchuu"
    await call.message.edit_reply_markup(navoiy_tumanlari)

@dp.callback_query_handler(navoiy_callback.filter(item_name='uchuu'))
async def chortoq(call: CallbackQuery):
    Uchquduq.add(call.message.chat.id)

    navoiy_tumanlari['inline_keyboard'][1][3]['text'] = "✅ Uchquduq"
    navoiy_tumanlari['inline_keyboard'][1][3]['callback_data'] = "course:uchquduq"
    await call.message.edit_reply_markup(navoiy_tumanlari)