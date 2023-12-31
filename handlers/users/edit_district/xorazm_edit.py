from loader import dp, db
from aiogram.types import CallbackQuery
from keyboards.inline.yolovchi.callback_data import  viloyatlar_callback,xorazm_callback
from keyboards.inline.yolovchi.xorazmtuman import xorazm_tumanlari
Bogot={*()}
Gurlan={*()}
Xonqa={*()}
Hazorasp={*()}
Xiva={*()}
Qoshkopir={*()}
Shovot={*()}
Urganch={*()}
Yangiariq={*()}
Yangibozor={*()}
Tupproqqala={*()}
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='azmm'))
async def xorazm_edit(call: CallbackQuery):
    await db.add_driver_info(viloyat="Toshkent", tuman="bog'ot", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Toshkent", tuman="gurlan", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Toshkent", tuman="xonqa", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Toshkent", tuman="hazorasp", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Toshkent", tuman="xiva", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Toshkent", tuman="qoshko'prik", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Toshkent", tuman="shovot", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Toshkent", tuman="urganch", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Toshkent", tuman="yangiariq", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Toshkent", tuman="yangibozor", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Toshkent", tuman="tuproqqal'a", telegram_id=call.from_user.id)

    await call.message.answer("Xorazm viloyati tumanlari ", reply_markup=xorazm_tumanlari)


@dp.callback_query_handler(xorazm_callback.filter(item_name='bogot'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="bog'ot", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][0][0]['text'] = "❌ Bog'ot"
    xorazm_tumanlari['inline_keyboard'][0][0]['callback_data'] = "course:bogo"
    await call.message.edit_reply_markup(xorazm_tumanlari)

@dp.callback_query_handler(xorazm_callback.filter(item_name='bogo'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Toshkent", tuman="bog'ot", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][0][0]['text'] = "✅ Bog'ot"
    xorazm_tumanlari['inline_keyboard'][0][0]['callback_data'] = "course:bogot"
    await call.message.edit_reply_markup(xorazm_tumanlari)



@dp.callback_query_handler(xorazm_callback.filter(item_name='gurlan'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="gurlan", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][0][1]['text'] = "❌ Gurlan"
    xorazm_tumanlari['inline_keyboard'][0][1]['callback_data'] = "course:gurla"
    await call.message.edit_reply_markup(xorazm_tumanlari)

@dp.callback_query_handler(xorazm_callback.filter(item_name='gurla'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Toshkent", tuman="gurlan", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][0][1]['text'] = "✅ Gurlan"
    xorazm_tumanlari['inline_keyboard'][0][1]['callback_data'] = "course:gurlan"
    await call.message.edit_reply_markup(xorazm_tumanlari)



@dp.callback_query_handler(xorazm_callback.filter(item_name='xonqa'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="xonqa", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][0][2]['text'] = "❌ Xonqa"
    xorazm_tumanlari['inline_keyboard'][0][2]['callback_data'] = "course:xonqaa"
    await call.message.edit_reply_markup(xorazm_tumanlari)

@dp.callback_query_handler(xorazm_callback.filter(item_name='xonqaa'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Toshkent", tuman="xonqa", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][0][2]['text'] = "✅ Xonqa"
    xorazm_tumanlari['inline_keyboard'][0][2]['callback_data'] = "course:xonqa"
    await call.message.edit_reply_markup(xorazm_tumanlari)



@dp.callback_query_handler(xorazm_callback.filter(item_name='hazorasp'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="hazorasp", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][0][3]['text'] = "❌ Hazorasp"
    xorazm_tumanlari['inline_keyboard'][0][3]['callback_data'] = "course:hazor"
    await call.message.edit_reply_markup(xorazm_tumanlari)

@dp.callback_query_handler(xorazm_callback.filter(item_name='hazor'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Toshkent", tuman="hazorasp", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][0][3]['text'] = "✅ Hazorasp"
    xorazm_tumanlari['inline_keyboard'][0][3]['callback_data'] = "course:hazorasp"
    await call.message.edit_reply_markup(xorazm_tumanlari)



@dp.callback_query_handler(xorazm_callback.filter(item_name='xiva'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="xiva", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][1][0]['text'] = "❌ Xiva"
    xorazm_tumanlari['inline_keyboard'][1][0]['callback_data'] = "course:xivaa"
    await call.message.edit_reply_markup(xorazm_tumanlari)

@dp.callback_query_handler(xorazm_callback.filter(item_name='xivaa'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Toshkent", tuman="xiva", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][1][0]['text'] = "✅ Xiva"
    xorazm_tumanlari['inline_keyboard'][1][0]['callback_data'] = "course:Xiva"
    await call.message.edit_reply_markup(xorazm_tumanlari)



@dp.callback_query_handler(xorazm_callback.filter(item_name='qoshkoprik'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="qoshko'prik", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][1][1]['text'] = "❌ Qoshko'prik"
    xorazm_tumanlari['inline_keyboard'][1][1]['callback_data'] = "course:qoshkop"
    await call.message.edit_reply_markup(xorazm_tumanlari)

@dp.callback_query_handler(xorazm_callback.filter(item_name='qoshkop'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Toshkent", tuman="qoshko'prik", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][1][1]['text'] = "✅ Qoshko'prik"
    xorazm_tumanlari['inline_keyboard'][1][1]['callback_data'] = "course:qoshkoprik"
    await call.message.edit_reply_markup(xorazm_tumanlari)



@dp.callback_query_handler(xorazm_callback.filter(item_name='shovot'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="shovot", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][1][2]['text'] = "❌ Shovot"
    xorazm_tumanlari['inline_keyboard'][1][2]['callback_data'] = "course:shovi"
    await call.message.edit_reply_markup(xorazm_tumanlari)

@dp.callback_query_handler(xorazm_callback.filter(item_name='shovi'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Toshkent", tuman="shovot", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][1][2]['text'] = "✅ Shovot"
    xorazm_tumanlari['inline_keyboard'][1][2]['callback_data'] = "course:shovot"
    await call.message.edit_reply_markup(xorazm_tumanlari)


@dp.callback_query_handler(xorazm_callback.filter(item_name='urganch'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="urganch", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][1][3]['text'] = "❌ Urganch"
    xorazm_tumanlari['inline_keyboard'][1][3]['callback_data'] = "course:urgan"
    await call.message.edit_reply_markup(xorazm_tumanlari)

@dp.callback_query_handler(xorazm_callback.filter(item_name='urgan'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Toshkent", tuman="urganch", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][1][3]['text'] = "✅ Urganch"
    xorazm_tumanlari['inline_keyboard'][1][3]['callback_data'] = "course:urganch"
    await call.message.edit_reply_markup(xorazm_tumanlari)



@dp.callback_query_handler(xorazm_callback.filter(item_name='yangiariq'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="yangiariq", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][2][0]['text'] = "❌ Yangi ariq"
    xorazm_tumanlari['inline_keyboard'][2][0]['callback_data'] = "course:yariq"
    await call.message.edit_reply_markup(xorazm_tumanlari)

@dp.callback_query_handler(xorazm_callback.filter(item_name='yariq'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Toshkent", tuman="yangiariq", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][2][0]['text'] = "✅ Yangi ariq"
    xorazm_tumanlari['inline_keyboard'][2][0]['callback_data'] = "course:yangiariq"
    await call.message.edit_reply_markup(xorazm_tumanlari)


@dp.callback_query_handler(xorazm_callback.filter(item_name='yangibozor'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="yangibozor", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][2][1]['text'] = "❌ Yangi bozor"
    xorazm_tumanlari['inline_keyboard'][2][1]['callback_data'] = "course:bozor"
    await call.message.edit_reply_markup(xorazm_tumanlari)

@dp.callback_query_handler(xorazm_callback.filter(item_name='bozor'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Toshkent", tuman="yangibozor", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][2][1]['text'] = "✅ Yangi bozor"
    xorazm_tumanlari['inline_keyboard'][2][1]['callback_data'] = "course:yangibozor"
    await call.message.edit_reply_markup(xorazm_tumanlari)


@dp.callback_query_handler(xorazm_callback.filter(item_name='tuproqqala'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="tuproqqal'a", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][2][2]['text'] = "❌ Tuproqqal'a"
    xorazm_tumanlari['inline_keyboard'][2][2]['callback_data'] = "course:qala"
    await call.message.edit_reply_markup(xorazm_tumanlari)

@dp.callback_query_handler(xorazm_callback.filter(item_name='qala'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Toshkent", tuman="tuproqqal'a", telegram_id=call.from_user.id)

    xorazm_tumanlari['inline_keyboard'][2][2]['text'] = "✅ Tuproqqal'a"
    xorazm_tumanlari['inline_keyboard'][2][2]['callback_data'] = "course:tuproqqala"
    await call.message.edit_reply_markup(xorazm_tumanlari)