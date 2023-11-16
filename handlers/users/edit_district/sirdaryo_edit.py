from loader import dp, db
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
    await db.add_driver_info(viloyat="Sirdaryo", tuman="oqoltin", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Sirdaryo", tuman="boyovut", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Sirdaryo", tuman="guliston", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Sirdaryo", tuman="xovos", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Sirdaryo", tuman="mirzaobod", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Sirdaryo", tuman="sardoba", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Sirdaryo", tuman="sayxunobod", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Sirdaryo", tuman="sirdaryo shaxri", telegram_id=call.from_user.id)

    await call.message.answer("Sirdaryo viloyati tumanlari ", reply_markup=sirdaryo_viloyati_tumanlari)


@dp.callback_query_handler(sirdaryo_callback.filter(item_name='oqoltin'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="oqoltin", telegram_id=call.from_user.id)
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][0]['text'] = "❌ Oqoltin"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][0]['callback_data'] = "course:oqol"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='oqol'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Sirdaryo", tuman="oqoltin", telegram_id=call.from_user.id)
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][0]['text'] = "✅ Oqoltin"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][0]['callback_data'] = "course:oqoltin"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)


@dp.callback_query_handler(sirdaryo_callback.filter(item_name='boyovut'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="boyovut", telegram_id=call.from_user.id)
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][1]['text'] = "❌ Boyovut"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][1]['callback_data'] = "course:boyov"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='boyov'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Sirdaryo", tuman="boyovut", telegram_id=call.from_user.id)
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][1]['text'] = "✅ Boyovut"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][1]['callback_data'] = "course:boyovut"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)


@dp.callback_query_handler(sirdaryo_callback.filter(item_name='guliston'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="guliston", telegram_id=call.from_user.id)
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][2]['text'] = "❌ Guliston"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][2]['callback_data'] = "course:gulis"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='gulis'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Sirdaryo", tuman="guliston", telegram_id=call.from_user.id)
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][2]['text'] = "✅ Guliston"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][2]['callback_data'] = "course:guliston"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)



@dp.callback_query_handler(sirdaryo_callback.filter(item_name='xovos'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="xovos", telegram_id=call.from_user.id)
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][3]['text'] = "❌ Xovos"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][3]['callback_data'] = "course:xovo"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='xovo'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Sirdaryo", tuman="xovos", telegram_id=call.from_user.id)
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][3]['text'] = "✅ Xovos"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][0][3]['callback_data'] = "course:xovos"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='mirzaobod'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="mirzaobod", telegram_id=call.from_user.id)
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][0]['text'] = "❌ Mirzaobod"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][0]['callback_data'] = "course:mobod"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='mobod'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Sirdaryo", tuman="mirzaobod", telegram_id=call.from_user.id)
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][0]['text'] = "✅ Mirzaobod"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][0]['callback_data'] = "course:mirzaobod"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)


@dp.callback_query_handler(sirdaryo_callback.filter(item_name='sardoba'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="sardoba", telegram_id=call.from_user.id)
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][1]['text'] = "❌ Sardoba"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][1]['callback_data'] = "course:sardob"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='sardob'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Sirdaryo", tuman="sardoba", telegram_id=call.from_user.id)
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][1]['text'] = "✅ Sardoba"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][1]['callback_data'] = "course:sardoba"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)


@dp.callback_query_handler(sirdaryo_callback.filter(item_name='sayxunobod'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="sayxunobod", telegram_id=call.from_user.id)
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][2]['text'] = "❌ Sayxunobod"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][2]['callback_data'] = "course:sayxun"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='sayxun'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Sirdaryo", tuman="sayxunobod", telegram_id=call.from_user.id)
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][2]['text'] = "✅ Sayxunobod"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][2]['callback_data'] = "course:sayxunobod"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)


@dp.callback_query_handler(sirdaryo_callback.filter(item_name='sirdaryo shaxri'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="sirdaryo shaxri", telegram_id=call.from_user.id)
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][3]['text'] = "❌ Sirdayo shaxar"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][3]['callback_data'] = "course:sizshar"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)

@dp.callback_query_handler(sirdaryo_callback.filter(item_name='sizshar'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Sirdaryo", tuman="sirdaryo shaxri", telegram_id=call.from_user.id)
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][3]['text'] = "✅ Sirdaryo shaxar"
    sirdaryo_viloyati_tumanlari['inline_keyboard'][1][3]['callback_data'] = "course:sirdaryo shaxri"
    await call.message.edit_reply_markup(sirdaryo_viloyati_tumanlari)