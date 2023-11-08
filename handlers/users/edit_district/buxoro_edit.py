from aiogram.types import CallbackQuery
from keyboards.inline.yolovchi.callback_data import  viloyatlar_callback, buxoro_callback
from keyboards.inline.yolovchi.buxtuman import buxoro_viloyati_tumanlari
from loader import dp

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
    Olot.add(call.message.chat.id)
    Buxoroshaxar.add(call.message.chat.id)
    Jondor.add(call.message.chat.id)
    Kogon.add(call.message.chat.id)
    Qorakoʻl.add(call.message.chat.id)
    Peshku.add(call.message.chat.id)
    Vobkent.add(call.message.chat.id)
    Shofirkon.add(call.message.chat.id)
    Romitan.add(call.message.chat.id)
    Qorovulbozor.add(call.message.chat.id)
    Gijduvon.add(call.message.chat.id)
    await call.message.answer("Buxoro tumanlari", reply_markup=buxoro_viloyati_tumanlari)


@dp.callback_query_handler(buxoro_callback.filter(item_name='olot'))
async def oltiariq_edit(call:CallbackQuery):
    Olot.remove(call.message.chat.id)
    buxoro_viloyati_tumanlari['inline_keyboard'][0][0]['text']='❌ Olot'
    buxoro_viloyati_tumanlari['inline_keyboard'][0][0]['callback_data']='course:olo'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='olo'))
async def oltiariq_edit(call:CallbackQuery):
    Olot.add(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][0][0]['text']='✅ Olot'
    buxoro_viloyati_tumanlari['inline_keyboard'][0][0]['callback_data']='course:olot'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)


@dp.callback_query_handler(buxoro_callback.filter(item_name='buxor'))
async def oltiariq_edit(call:CallbackQuery):
    Buxoroshaxar.remove(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][0][1]['text']='❌ Buxoro'
    buxoro_viloyati_tumanlari['inline_keyboard'][0][1]['callback_data']='course:buxori'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='buxori'))
async def oltiariq_edit(call:CallbackQuery):
    Buxoroshaxar.add(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][0][1]['text']='✅ Buxoro'
    buxoro_viloyati_tumanlari['inline_keyboard'][0][1]['callback_data']='course:buxor'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)


@dp.callback_query_handler(buxoro_callback.filter(item_name='gijduvon'))
async def oltiariq_edit(call:CallbackQuery):
    Gijduvon.remove(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][0][2]['text']="❌ G'ijduvon"
    buxoro_viloyati_tumanlari['inline_keyboard'][0][2]['callback_data']='course:gijd'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='gijd'))
async def oltiariq_edit(call:CallbackQuery):
    Gijduvon.add(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][0][2]['text']="✅ G'ijduvon"
    buxoro_viloyati_tumanlari['inline_keyboard'][0][2]['callback_data']='course:gijduvon'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)



@dp.callback_query_handler(buxoro_callback.filter(item_name='jondor'))
async def oltiariq_edit(call:CallbackQuery):
    Jondor.remove(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][0][3]['text']="❌ Jondor"
    buxoro_viloyati_tumanlari['inline_keyboard'][0][3]['callback_data']='course:jondo'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='jondo'))
async def oltiariq_edit(call:CallbackQuery):
    Jondor.add(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][0][3]['text']="✅ Jondor"
    buxoro_viloyati_tumanlari['inline_keyboard'][0][3]['callback_data']='course:jondor'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)


@dp.callback_query_handler(buxoro_callback.filter(item_name='kogon'))
async def oltiariq_edit(call:CallbackQuery):
    Kogon.remove(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][1][0]['text']="❌ Kogon"
    buxoro_viloyati_tumanlari['inline_keyboard'][1][0]['callback_data']='course:kogo'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='kogo'))
async def oltiariq_edit(call:CallbackQuery):
    Kogon.add(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][1][0]['text']="✅ Kogon"
    buxoro_viloyati_tumanlari['inline_keyboard'][1][0]['callback_data']='course:kogon'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)



@dp.callback_query_handler(buxoro_callback.filter(item_name='qorakol'))
async def oltiariq_edit(call:CallbackQuery):
    Qorakoʻl.remove(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][1][1]['text']="❌ Qorako'l"
    buxoro_viloyati_tumanlari['inline_keyboard'][1][1]['callback_data']='course:qorak'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='qorak'))
async def oltiariq_edit(call:CallbackQuery):
    Qorakoʻl.add(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][1][1]['text']="✅ Qorako'l"
    buxoro_viloyati_tumanlari['inline_keyboard'][1][1]['callback_data']='course:qorakol'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)



@dp.callback_query_handler(buxoro_callback.filter(item_name='qorovul'))
async def oltiariq_edit(call:CallbackQuery):
    Qorovulbozor.remove(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][1][2]['text']="❌ Qoravulbozor"
    buxoro_viloyati_tumanlari['inline_keyboard'][1][2]['callback_data']='course:qorav'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='qorav'))
async def oltiariq_edit(call:CallbackQuery):
    Qorovulbozor.add(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][1][2]['text']="✅ Qoravulbozor"
    buxoro_viloyati_tumanlari['inline_keyboard'][1][2]['callback_data']='course:qorovul'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)


@dp.callback_query_handler(buxoro_callback.filter(item_name='peshku'))
async def oltiariq_edit(call:CallbackQuery):
    Peshku.remove(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][1][3]['text']="❌ Peshku"
    buxoro_viloyati_tumanlari['inline_keyboard'][1][3]['callback_data']='course:pesh'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='pesh'))
async def oltiariq_edit(call:CallbackQuery):
    Peshku.add(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][1][3]['text']="✅ Peshku"
    buxoro_viloyati_tumanlari['inline_keyboard'][1][3]['callback_data']='course:peshku'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)



@dp.callback_query_handler(buxoro_callback.filter(item_name='romitan'))
async def oltiariq_edit(call:CallbackQuery):
    Romitan.remove(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][2][0]['text']="❌ Romitan"
    buxoro_viloyati_tumanlari['inline_keyboard'][2][0]['callback_data']='course:promiesh'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)

@dp.callback_query_handler(buxoro_callback.filter(item_name='promiesh'))
async def oltiariq_edit(call:CallbackQuery):
    Romitan.add(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][2][0]['text']="✅ Romitan"
    buxoro_viloyati_tumanlari['inline_keyboard'][2][0]['callback_data']='course:romitan'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)


@dp.callback_query_handler(buxoro_callback.filter(item_name='shofirkon'))
async def oltiariq_edit(call: CallbackQuery):
    Shofirkon.remove(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][2][1]['text'] = "❌ Shofirkon"
    buxoro_viloyati_tumanlari['inline_keyboard'][2][1]['callback_data'] = 'course:shofir'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)


@dp.callback_query_handler(buxoro_callback.filter(item_name='shofir'))
async def oltiariq_edit(call: CallbackQuery):
    Shofirkon.add(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][2][1]['text'] = "✅ Shofirkon"
    buxoro_viloyati_tumanlari['inline_keyboard'][2][1]['callback_data'] = 'course:shofirkon'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)



@dp.callback_query_handler(buxoro_callback.filter(item_name='vobkent'))
async def oltiariq_edit(call: CallbackQuery):
    Vobkent.remove(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][2][2]['text'] = "❌ Vobkent"
    buxoro_viloyati_tumanlari['inline_keyboard'][2][2]['callback_data'] = 'course:vob'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)


@dp.callback_query_handler(buxoro_callback.filter(item_name='vob'))
async def oltiariq_edit(call: CallbackQuery):
    Vobkent.add(call.message.chat.id)

    buxoro_viloyati_tumanlari['inline_keyboard'][2][2]['text'] = "✅ Vobkent"
    buxoro_viloyati_tumanlari['inline_keyboard'][2][2]['callback_data'] = 'course:vobkent'
    await call.message.edit_reply_markup(buxoro_viloyati_tumanlari)
