from loader import dp
from aiogram.types import CallbackQuery
from keyboards.inline.yolovchi.callback_data import  viloyatlar_callback, sirdaryo_callback
from keyboards.inline.yolovchi.sirtuman import sirdaryo_viloyati_tumanlari
Oqoltin={*()}
Boyovut={*()}
Guliston={*()}
Xovos={*()}
Mirzaobod={*()}
Sardoba={*()}
Sayxunobod={*()}
Sirdaryoshahri={*()}
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='ryoo'))
async def namangan_edit(call: CallbackQuery):
    await call.message.answer("Sirdaryo viloyati tumanlari ", reply_markup=sirdaryo_viloyati_tumanlari)
    Oqoltin.add(call.message.chat.id)
    Boyovut.add(call.message.chat.id)
    Guliston.add(call.message.chat.id)
    Xovos.add(call.message.chat.id)
    Mirzaobod.add(call.message.chat.id)
    Sardoba.add(call.message.chat.id)
    Sayxunobod.add(call.message.chat.id)
    Sirdaryoshahri.add(call.message.chat.id)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='oqoltin'))
async def chortoq(call: CallbackQuery):
    Oqoltin.remove(call.message.chat.id)

    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][0]['text'] = "❌ Oqoltin"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][0]['callback_data'] = "course:oqol"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='oqol'))
async def chortoq(call: CallbackQuery):
    Oqoltin.add(call.message.chat.id)

    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][0]['text'] = "✅ Oqoltin"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][0]['callback_data'] = "course:oqoltin"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)


@dp.callback_query_handler(sirdaryo_callback.filter(item_name='boyovut'))
async def chortoq(call: CallbackQuery):
    Boyovut.remove(call.message.chat.id)

    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][1]['text'] = "❌ Boyovut"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][1]['callback_data'] = "course:boyov"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='boyov'))
async def chortoq(call: CallbackQuery):
    Boyovut.add(call.message.chat.id)

    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][1]['text'] = "✅ Boyovut"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][1]['callback_data'] = "course:boyovut"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)


@dp.callback_query_handler(sirdaryo_callback.filter(item_name='guliston'))
async def chortoq(call: CallbackQuery):
    Guliston.remove(call.message.chat.id)

    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][2]['text'] = "❌ Guliston"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][2]['callback_data'] = "course:gulis"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='gulis'))
async def chortoq(call: CallbackQuery):
    Guliston.add(call.message.chat.id)

    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][2]['text'] = "✅ Guliston"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][2]['callback_data'] = "course:guliston"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)



@dp.callback_query_handler(sirdaryo_callback.filter(item_name='xovos'))
async def chortoq(call: CallbackQuery):
    Xovos.remove(call.message.chat.id)

    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][3]['text'] = "❌ Xovos"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][3]['callback_data'] = "course:xovo"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='xovo'))
async def chortoq(call: CallbackQuery):
    Xovos.add(call.message.chat.id)

    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][3]['text'] = "✅ Xovos"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][3]['callback_data'] = "course:xovos"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='mirzaobod'))
async def chortoq(call: CallbackQuery):
    Mirzaobod.remove(call.message.chat.id)

    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][0]['text'] = "❌ Mirzaobod"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][0]['callback_data'] = "course:mobod"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='mobod'))
async def chortoq(call: CallbackQuery):
    Mirzaobod.add(call.message.chat.id)

    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][0]['text'] = "✅ Mirzaobod"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][0]['callback_data'] = "course:mirzaobod"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)


@dp.callback_query_handler(sirdaryo_callback.filter(item_name='sardoba'))
async def chortoq(call: CallbackQuery):
    Sardoba.remove(call.message.chat.id)

    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][1]['text'] = "❌ Sardoba"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][1]['callback_data'] = "course:sardob"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='sardob'))
async def chortoq(call: CallbackQuery):
    Sardoba.add(call.message.chat.id)

    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][1]['text'] = "✅ Sardoba"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][1]['callback_data'] = "course:sardoba"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)


@dp.callback_query_handler(sirdaryo_callback.filter(item_name='sayxunobod'))
async def chortoq(call: CallbackQuery):
    Sayxunobod.remove(call.message.chat.id)

    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][2]['text'] = "❌ Sayxunobod"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][2]['callback_data'] = "course:sayxun"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='sayxun'))
async def chortoq(call: CallbackQuery):
    Sayxunobod.add(call.message.chat.id)

    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][2]['text'] = "✅ Sayxunobod"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][2]['callback_data'] = "course:sayxunobod"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)


@dp.callback_query_handler(sirdaryo_callback.filter(item_name='sirdaryo shaxri'))
async def chortoq(call: CallbackQuery):
    Sirdaryoshahri.remove(call.message.chat.id)

    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][3]['text'] = "❌ Sirdayo shaxar"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][3]['callback_data'] = "course:sizshar"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='sizshar'))
async def chortoq(call: CallbackQuery):
    Sirdaryoshahri.add(call.message.chat.id)

    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][3]['text'] = "✅ Sirdaryo shaxar"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][3]['callback_data'] = "course:sirdaryo shaxri"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)