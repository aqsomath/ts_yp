from aiogram.types import CallbackQuery
from keyboards.inline.yolovchi.callback_data import viloyatlar_callback, fargona_callback
from loader import dp, db
from keyboards.inline.yolovchi.fartuman import fargona

Oltiariq={*()}
Bagdod={*()}
Beshariq={*()}
Buvayda={*()}
Dangara={*()}
Fargona={*()}
Furqat={*()}
Qoshtepa={*()}
Quva={*()}
Rishton={*()}
Sox={*()}
Toshloq={*()}
Ozbekiston={*()}
Uchkoprik={*()}
Yozyovon={*()}

@dp.callback_query_handler(viloyatlar_callback.filter(item_name='onaa'))
async def fargona_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Farg'ona", tuman="o'zbekiston", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Farg'ona", tuman="uchko'prik", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Farg'ona", tuman="yozyovon", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Farg'ona", tuman="toshloq", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Farg'ona", tuman="sox", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Farg'ona", tuman="rishton", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Farg'ona", tuman="quva", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Farg'ona", tuman="oltiariq", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Farg'ona", tuman="fergana", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Farg'ona", tuman="furqat", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Farg'ona", tuman="qo'shtepa", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Farg'ona", tuman="dangara", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Farg'ona", tuman="buvayda", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Farg'ona", tuman="beshariq", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Farg'ona", tuman="bog'dod", telegram_id=call.from_user.id)
    await call.message.answer("Farg'ona tumanlari", reply_markup=fargona)
@dp.callback_query_handler(fargona_callback.filter(item_name='olti'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="oltiariq", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][0][0]['text']='❌ Oltiariq'
    fargona['inline_keyboard'][0][0]['callback_data']='course:yetti'
    await call.message.edit_reply_markup(fargona)

@dp.callback_query_handler(fargona_callback.filter(item_name='yetti'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Farg'ona", tuman="oltiariq", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][0][0]['text']='✅ Oltiariq'
    fargona['inline_keyboard'][0][0]['callback_data']='course:olti'
    await call.message.edit_reply_markup(fargona)


@dp.callback_query_handler(fargona_callback.filter(item_name='bogdod'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="bog'dod", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][0][1]['text']="❌ Bog'dod "
    fargona['inline_keyboard'][0][1]['callback_data']='course:bog'
    await call.message.edit_reply_markup(fargona)

@dp.callback_query_handler(fargona_callback.filter(item_name='bog'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Farg'ona", tuman="bog'dod", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][0][1]['text']="✅ Bog'dod "
    fargona['inline_keyboard'][0][1]['callback_data']='course:bogdod'
    await call.message.edit_reply_markup(fargona)



@dp.callback_query_handler(fargona_callback.filter(item_name='beshariq'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="beshariq", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][0][2]['text']="❌ Beshariq "
    fargona['inline_keyboard'][0][2]['callback_data']='course:besh'
    await call.message.edit_reply_markup(fargona)

@dp.callback_query_handler(fargona_callback.filter(item_name='besh'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Farg'ona", tuman="beshariq", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][0][2]['text']="✅ Beshariq "
    fargona['inline_keyboard'][0][2]['callback_data']='course:beshariq'
    await call.message.edit_reply_markup(fargona)



@dp.callback_query_handler(fargona_callback.filter(item_name='buvayda'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="buvayda", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][0][3]['text']="❌ Buvayda"
    fargona['inline_keyboard'][0][3]['callback_data']='course:buv'
    await call.message.edit_reply_markup(fargona)

@dp.callback_query_handler(fargona_callback.filter(item_name='buv'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Farg'ona", tuman="buvayda", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][0][3]['text']="✅ Buvayda"
    fargona['inline_keyboard'][0][3]['callback_data']='course:buvayda'
    await call.message.edit_reply_markup(fargona)

@dp.callback_query_handler(fargona_callback.filter(item_name='dangara'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="dangara", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][1][0]['text']="❌ Dang'ara"
    fargona['inline_keyboard'][1][0]['callback_data']='course:dangar'
    await call.message.edit_reply_markup(fargona)

@dp.callback_query_handler(fargona_callback.filter(item_name='dangar'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Farg'ona", tuman="dangara", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][1][0]['text']="✅ Dang'ara"
    fargona['inline_keyboard'][1][0]['callback_data']='course:dangara'
    await call.message.edit_reply_markup(fargona)


@dp.callback_query_handler(fargona_callback.filter(item_name='fargona'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="fergana", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][1][1]['text']="❌ Farg'ona"
    fargona['inline_keyboard'][1][1]['callback_data']='course:faro'
    await call.message.edit_reply_markup(fargona)

@dp.callback_query_handler(fargona_callback.filter(item_name='faro'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Farg'ona", tuman="fergana", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][1][1]['text']="✅ Farg'ona"
    fargona['inline_keyboard'][1][1]['callback_data']='course:fargona'
    await call.message.edit_reply_markup(fargona)


@dp.callback_query_handler(fargona_callback.filter(item_name='furqat'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="furqat", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][1][2]['text']="❌ Furqat"
    fargona['inline_keyboard'][1][2]['callback_data']='course:fur'
    await call.message.edit_reply_markup(fargona)

@dp.callback_query_handler(fargona_callback.filter(item_name='fur'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Farg'ona", tuman="furqat", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][1][2]['text']="✅ Furqat"
    fargona['inline_keyboard'][1][2]['callback_data']='course:furqat'
    await call.message.edit_reply_markup(fargona)


@dp.callback_query_handler(fargona_callback.filter(item_name='qoshtepa'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="qo'shtepa", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][1][3]['text']="❌ Qo'shtepa"
    fargona['inline_keyboard'][1][3]['callback_data']='course:qosh'
    await call.message.edit_reply_markup(fargona)

@dp.callback_query_handler(fargona_callback.filter(item_name='qosh'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Farg'ona", tuman="qo'shtepa", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][1][3]['text']="✅ Qo'shtepa"
    fargona['inline_keyboard'][1][3]['callback_data']='course:qoshtepa'
    await call.message.edit_reply_markup(fargona)


@dp.callback_query_handler(fargona_callback.filter(item_name='quva'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="quva", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][2][0]['text']="❌ Quva"
    fargona['inline_keyboard'][2][0]['callback_data']='course:quv'
    await call.message.edit_reply_markup(fargona)

@dp.callback_query_handler(fargona_callback.filter(item_name='quv'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Farg'ona", tuman="quva", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][2][0]['text']="✅ Quva"
    fargona['inline_keyboard'][2][0]['callback_data']='course:quva'
    await call.message.edit_reply_markup(fargona)


@dp.callback_query_handler(fargona_callback.filter(item_name='rishton'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="rishton", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][2][1]['text']="❌ Rishton"
    fargona['inline_keyboard'][2][1]['callback_data']='course:risht'
    await call.message.edit_reply_markup(fargona)

@dp.callback_query_handler(fargona_callback.filter(item_name='risht'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Farg'ona", tuman="rishton", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][2][1]['text']="✅ Rishton"
    fargona['inline_keyboard'][2][1]['callback_data']='course:rishton'
    await call.message.edit_reply_markup(fargona)

@dp.callback_query_handler(fargona_callback.filter(item_name='sox'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="sox", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][2][2]['text']="❌ So'x"
    fargona['inline_keyboard'][2][2]['callback_data']='course:so'
    await call.message.edit_reply_markup(fargona)

@dp.callback_query_handler(fargona_callback.filter(item_name='so'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Farg'ona", tuman="sox", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][2][2]['text']="✅ So'x"
    fargona['inline_keyboard'][2][2]['callback_data']='course:sox'
    await call.message.edit_reply_markup(fargona)


@dp.callback_query_handler(fargona_callback.filter(item_name='toshloq'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="toshloq", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][2][3]['text']="❌ Toshloq"
    fargona['inline_keyboard'][2][3]['callback_data']='course:tosh'
    await call.message.edit_reply_markup(fargona)

@dp.callback_query_handler(fargona_callback.filter(item_name='tosh'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Farg'ona", tuman="toshloq", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][2][3]['text']="✅ Toshloq"
    fargona['inline_keyboard'][2][3]['callback_data']='course:tosh'
    await call.message.edit_reply_markup(fargona)


@dp.callback_query_handler(fargona_callback.filter(item_name='ozbekiston'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="o'zbekiston", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][3][0]['text']="❌ O'zbekiston"
    fargona['inline_keyboard'][3][0]['callback_data']='course:uzb'
    await call.message.edit_reply_markup(fargona)

@dp.callback_query_handler(fargona_callback.filter(item_name='uzb'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Farg'ona", tuman="o'zbekiston", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][3][0]['text']="✅ O'zbekiston"
    fargona['inline_keyboard'][3][0]['callback_data']='course:ozbekiston'
    await call.message.edit_reply_markup(fargona)


@dp.callback_query_handler(fargona_callback.filter(item_name='uchkoprik'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="uchko'prik", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][3][1]['text']="❌ Uchko'prik"
    fargona['inline_keyboard'][3][1]['callback_data']='course:uchk'
    await call.message.edit_reply_markup(fargona)

@dp.callback_query_handler(fargona_callback.filter(item_name='uchk'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Farg'ona", tuman="uchko'prik", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][3][1]['text']="✅ Uchko'prik"
    fargona['inline_keyboard'][3][1]['callback_data']='course:uchkoprik'
    await call.message.edit_reply_markup(fargona)


@dp.callback_query_handler(fargona_callback.filter(item_name='yozyovon'))
async def oltiariq_edit(call:CallbackQuery):
    await db.delete_driver_info(tuman="yozyovon", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][3][2]['text']="❌ Yozyovon"
    fargona['inline_keyboard'][3][2]['callback_data']='course:yozov'
    await call.message.edit_reply_markup(fargona)

@dp.callback_query_handler(fargona_callback.filter(item_name='yozov'))
async def oltiariq_edit(call:CallbackQuery):
    await db.add_driver_info(viloyat="Farg'ona", tuman="yozyovon", telegram_id=call.from_user.id)
    fargona['inline_keyboard'][3][2]['text']="✅ Yozyovon"
    fargona['inline_keyboard'][3][2]['callback_data']='course:yozyovon'
    await call.message.edit_reply_markup(fargona)