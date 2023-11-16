from aiogram.types import CallbackQuery
from keyboards.inline.yolovchi.callback_data import  viloyatlar_callback, buxoro_callback
from keyboards.inline.yolovchi.buxtuman import buxoro_viloyati_tumanlari
from loader import dp, db

Olot={*()}
Buxoroshaxar={*()}
Jondor={*()}
Kogon={*()}
Qorakoʻl={*()}
Peshku={*()}
Vobkent={*()}
Shofirkon={*()}
Romitan={*()}
Qorovulbozor={*()}
Gijduvon={*()}
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='oroo'))
async def toshkenttuman(call:CallbackQuery):
    await db.add_driver_info(viloyat="Buxoro", tuman="olot", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Buxoro", tuman="buxoro shaxar", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Buxoro", tuman="g'ijduvon", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Buxoro", tuman="jondor", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Buxoro", tuman="kogon", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Buxoro", tuman="qorako'l", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Buxoro", tuman="qorovulbozor", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Buxoro", tuman="peshku", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Buxoro", tuman="romitan", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Buxoro", tuman="shofirkon", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Buxoro", tuman="vobkent", telegram_id=call.from_user.id)

    await call.message.answer("Buxoro tumanlari", reply_markup=buxoro_viloyati_tumanlari)


@dp.callback_query_handler(buxoro_callback.filter(item_name='olot'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="olot", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][0][0]['text']='❌ Olot'
    buxoro_viloyati_tumanlari['inline_keyboard'][0][0]['callback_data']='course:olo'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='olo'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Buxoro", tuman="olot", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][0][0]['text']='✅ Olot'
    buxoro_viloyati_tumanlari['inline_keyboard'][0][0]['callback_data']='course:olot'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)


@dp.callback_query_handler(buxoro_callback.filter(item_name='buxor'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="buxoro shaxar", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][0][1]['text']='❌ Buxoro'
    buxoro_viloyati_tumanlari['inline_keyboard'][0][1]['callback_data']='course:buxori'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='buxori'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Buxoro", tuman="buxoro shaxar", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][0][1]['text']='✅ Buxoro'
    buxoro_viloyati_tumanlari['inline_keyboard'][0][1]['callback_data']='course:buxor'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)


@dp.callback_query_handler(buxoro_callback.filter(item_name='gijduvon'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="g'ijduvon", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][0][2]['text']="❌ G'ijduvon"
    buxoro_viloyati_tumanlari['inline_keyboard'][0][2]['callback_data']='course:gijd'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='gijd'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Buxoro", tuman="g'ijduvon", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][0][2]['text']="✅ G'ijduvon"
    buxoro_viloyati_tumanlari['inline_keyboard'][0][2]['callback_data']='course:gijduvon'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)



@dp.callback_query_handler(buxoro_callback.filter(item_name='jondor'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="jondor", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][0][3]['text']="❌ Jondor"
    buxoro_viloyati_tumanlari['inline_keyboard'][0][3]['callback_data']='course:jondo'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='jondo'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Buxoro", tuman="jondor", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][0][3]['text']="✅ Jondor"
    buxoro_viloyati_tumanlari['inline_keyboard'][0][3]['callback_data']='course:jondor'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)


@dp.callback_query_handler(buxoro_callback.filter(item_name='kogon'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="kogon", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][1][0]['text']="❌ Kogon"
    buxoro_viloyati_tumanlari['inline_keyboard'][1][0]['callback_data']='course:kogo'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='kogo'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Buxoro", tuman="kogon", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][1][0]['text']="✅ Kogon"
    buxoro_viloyati_tumanlari['inline_keyboard'][1][0]['callback_data']='course:kogon'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)



@dp.callback_query_handler(buxoro_callback.filter(item_name='qorakol'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="qorako'l", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][1][1]['text']="❌ Qorako'l"
    buxoro_viloyati_tumanlari['inline_keyboard'][1][1]['callback_data']='course:qorak'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='qorak'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Buxoro", tuman="qorako'l", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][1][1]['text']="✅ Qorako'l"
    buxoro_viloyati_tumanlari['inline_keyboard'][1][1]['callback_data']='course:qorakol'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)



@dp.callback_query_handler(buxoro_callback.filter(item_name='qorovul'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="qorovulbozor", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][1][2]['text']="❌ Qoravulbozor"
    buxoro_viloyati_tumanlari['inline_keyboard'][1][2]['callback_data']='course:qorav'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='qorav'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Buxoro", tuman="qorovulbozor", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][1][2]['text']="✅ Qoravulbozor"
    buxoro_viloyati_tumanlari['inline_keyboard'][1][2]['callback_data']='course:qorovul'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)


@dp.callback_query_handler(buxoro_callback.filter(item_name='peshku'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="peshku", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][1][3]['text']="❌ Peshku"
    buxoro_viloyati_tumanlari['inline_keyboard'][1][3]['callback_data']='course:pesh'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='pesh'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Buxoro", tuman="peshku", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][1][3]['text']="✅ Peshku"
    buxoro_viloyati_tumanlari['inline_keyboard'][1][3]['callback_data']='course:peshku'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)



@dp.callback_query_handler(buxoro_callback.filter(item_name='romitan'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="romitan", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][2][0]['text']="❌ Romitan"
    buxoro_viloyati_tumanlari['inline_keyboard'][2][0]['callback_data']='course:promiesh'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='promiesh'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Buxoro", tuman="romitan", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][2][0]['text']="✅ Romitan"
    buxoro_viloyati_tumanlari['inline_keyboard'][2][0]['callback_data']='course:romitan'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)


@dp.callback_query_handler(buxoro_callback.filter(item_name='shofirkon'))
async def oltiariq_edit(call: CallbackQuery):
    await db.delete_driver_info(tuman="shofirkon", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][2][1]['text'] = "❌ Shofirkon"
    buxoro_viloyati_tumanlari['inline_keyboard'][2][1]['callback_data'] = 'course:shofir'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)


@dp.callback_query_handler(buxoro_callback.filter(item_name='shofir'))
async def oltiariq_edit(call: CallbackQuery):
    await db.add_driver_info(viloyat="Buxoro", tuman="shofirkon", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][2][1]['text'] = "✅ Shofirkon"
    buxoro_viloyati_tumanlari['inline_keyboard'][2][1]['callback_data'] = 'course:shofirkon'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)



@dp.callback_query_handler(buxoro_callback.filter(item_name='vobkent'))
async def oltiariq_edit(call: CallbackQuery):
    await db.delete_driver_info(tuman="vobkent", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][2][2]['text'] = "❌ Vobkent"
    buxoro_viloyati_tumanlari['inline_keyboard'][2][2]['callback_data'] = 'course:vob'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)


@dp.callback_query_handler(buxoro_callback.filter(item_name='vob'))
async def oltiariq_edit(call: CallbackQuery):
    await db.add_driver_info(viloyat="Buxoro", tuman="vobkent", telegram_id=call.from_user.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][2][2]['text'] = "✅ Vobkent"
    buxoro_viloyati_tumanlari['inline_keyboard'][2][2]['callback_data'] = 'course:vobkent'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)
