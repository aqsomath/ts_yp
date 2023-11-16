from loader import dp, db
from aiogram.types import CallbackQuery
from keyboards.inline.yolovchi.callback_data import  viloyatlar_callback,samarqand_callback
from keyboards.inline.yolovchi.samartuman import samarqaand_tumalari
Bulungʻur={*()}
Ishtixon={*()}
Jomboy={*()}
Kattaqoʻrgʻon={*()}
Qoʻshrabot={*()}
Narpay={*()}
Nurobod={*()}
Oqdaryo={*()}
Paxtachi={*()}
Payariq={*()}
Pastdargʻom={*()}
Samarqand={*()}
Toyloq={*()}
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='marqa'))
async def jizzax_edit(call: CallbackQuery):
    await db.add_driver_info(viloyat="Samarqand", tuman="bulungur", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Samarqand", tuman="ishtixon", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Samarqand", tuman="jomboy", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Samarqand", tuman="kattaqorgon", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Samarqand", tuman="qoshrabot", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Samarqand", tuman="narpay", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Samarqand", tuman="nurobod", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Samarqand", tuman="oqdaryo", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Samarqand", tuman="paxtachi", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Samarqand", tuman="payariq", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Samarqand", tuman="pastdargom", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Samarqand", tuman="samarqand shahar", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Samarqand", tuman="toyloq", telegram_id=call.from_user.id)

    await call.message.answer("Samarqand viloyati tumanlari ", reply_markup=samarqaand_tumalari)


@dp.callback_query_handler(samarqand_callback.filter(item_name='bulungur'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="bulungur", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][0][0]['text'] = "❌ Bulung'ur"
    samarqaand_tumalari['inline_keyboard'][0][0]['callback_data'] = "course:bulun"
    await call.message.edit_reply_markup(samarqaand_tumalari)

@dp.callback_query_handler(samarqand_callback.filter(item_name='bulun'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Samarqand", tuman="bulungur", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][0][0]['text'] = "✅ Bulung'ur"
    samarqaand_tumalari['inline_keyboard'][0][0]['callback_data'] = "course:bulungur"
    await call.message.edit_reply_markup(samarqaand_tumalari)



@dp.callback_query_handler(samarqand_callback.filter(item_name='ishtixon'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="ishtixon", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][0][1]['text'] = "❌ Ishtixon"
    samarqaand_tumalari['inline_keyboard'][0][1]['callback_data'] = "course:ishti"
    await call.message.edit_reply_markup(samarqaand_tumalari)

@dp.callback_query_handler(samarqand_callback.filter(item_name='ishti'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Samarqand", tuman="ishtixon", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][0][1]['text'] = "✅ Ishtixon"
    samarqaand_tumalari['inline_keyboard'][0][1]['callback_data'] = "course:ishtixon"
    await call.message.edit_reply_markup(samarqaand_tumalari)


@dp.callback_query_handler(samarqand_callback.filter(item_name='jomboy'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="jomboy", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][0][2]['text'] = "❌ Jomboy"
    samarqaand_tumalari['inline_keyboard'][0][2]['callback_data'] = "course:jom"
    await call.message.edit_reply_markup(samarqaand_tumalari)

@dp.callback_query_handler(samarqand_callback.filter(item_name='jom'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Samarqand", tuman="jomboy", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][0][2]['text'] = "✅ Jomboy"
    samarqaand_tumalari['inline_keyboard'][0][2]['callback_data'] = "course:jomboy"
    await call.message.edit_reply_markup(samarqaand_tumalari)


@dp.callback_query_handler(samarqand_callback.filter(item_name='kattaqorgon'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="kattaqorgon", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][0][3]['text'] = "❌ Kattaqo'rg'on"
    samarqaand_tumalari['inline_keyboard'][0][3]['callback_data'] = "course:kattaq"
    await call.message.edit_reply_markup(samarqaand_tumalari)

@dp.callback_query_handler(samarqand_callback.filter(item_name='kattaq'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Samarqand", tuman="kattaqorgon", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][0][3]['text'] = "✅ Kattaqo'rg'on"
    samarqaand_tumalari['inline_keyboard'][0][3]['callback_data'] = "course:kattaqorg'on"
    await call.message.edit_reply_markup(samarqaand_tumalari)


@dp.callback_query_handler(samarqand_callback.filter(item_name='qoshrabot'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="qoshrabot", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][1][0]['text'] = "❌ Qo'shrabot"
    samarqaand_tumalari['inline_keyboard'][1][0]['callback_data'] = "course:qoshra"
    await call.message.edit_reply_markup(samarqaand_tumalari)

@dp.callback_query_handler(samarqand_callback.filter(item_name='qoshra'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Samarqand", tuman="qoshrabot", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][1][0]['text'] = "✅ Qo'shrabot"
    samarqaand_tumalari['inline_keyboard'][1][0]['callback_data'] = "course:qoshrabot"
    await call.message.edit_reply_markup(samarqaand_tumalari)



@dp.callback_query_handler(samarqand_callback.filter(item_name='narpay'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="narpay", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][1][1]['text'] = "❌ Narpay"
    samarqaand_tumalari['inline_keyboard'][1][1]['callback_data'] = "course:narp"
    await call.message.edit_reply_markup(samarqaand_tumalari)

@dp.callback_query_handler(samarqand_callback.filter(item_name='narp'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Samarqand", tuman="narpay", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][1][1]['text'] = "✅ Narpay"
    samarqaand_tumalari['inline_keyboard'][1][1]['callback_data'] = "course:narpay"
    await call.message.edit_reply_markup(samarqaand_tumalari)


@dp.callback_query_handler(samarqand_callback.filter(item_name='nurobodoo'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="nurobod", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][1][2]['text'] = "❌ Nurobod"
    samarqaand_tumalari['inline_keyboard'][1][2]['callback_data'] = "course:nurobo"
    await call.message.edit_reply_markup(samarqaand_tumalari)

@dp.callback_query_handler(samarqand_callback.filter(item_name='nurobo'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Samarqand", tuman="nurobod", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][1][2]['text'] = "✅ Nurobod"
    samarqaand_tumalari['inline_keyboard'][1][2]['callback_data'] = "course:nurobodoo"
    await call.message.edit_reply_markup(samarqaand_tumalari)



@dp.callback_query_handler(samarqand_callback.filter(item_name='oqdaryo'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="oqdaryo", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][1][3]['text'] = "❌ Oqdaryo"
    samarqaand_tumalari['inline_keyboard'][1][3]['callback_data'] = "course:oqdar"
    await call.message.edit_reply_markup(samarqaand_tumalari)

@dp.callback_query_handler(samarqand_callback.filter(item_name='oqdar'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Samarqand", tuman="oqdaryo", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][1][3]['text'] = "✅ Oqdaryo"
    samarqaand_tumalari['inline_keyboard'][1][3]['callback_data'] = "course:oqdaryo"
    await call.message.edit_reply_markup(samarqaand_tumalari)


@dp.callback_query_handler(samarqand_callback.filter(item_name='paxtachi'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="paxtachi", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][2][0]['text'] = "❌ Paxtachi"
    samarqaand_tumalari['inline_keyboard'][2][0]['callback_data'] = "course:paxtaxh"
    await call.message.edit_reply_markup(samarqaand_tumalari)

@dp.callback_query_handler(samarqand_callback.filter(item_name='paxtaxh'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Samarqand", tuman="paxtachi", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][2][0]['text'] = "✅ Paxtachi"
    samarqaand_tumalari['inline_keyboard'][2][0]['callback_data'] = "course:paxtachi"
    await call.message.edit_reply_markup(samarqaand_tumalari)


@dp.callback_query_handler(samarqand_callback.filter(item_name='payariq'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="payariq", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][2][1]['text'] = "❌ Payariq"
    samarqaand_tumalari['inline_keyboard'][2][1]['callback_data'] = "course:payaq"
    await call.message.edit_reply_markup(samarqaand_tumalari)

@dp.callback_query_handler(samarqand_callback.filter(item_name='payaq'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Samarqand", tuman="payariq", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][2][1]['text'] = "✅ Payariq"
    samarqaand_tumalari['inline_keyboard'][2][1]['callback_data'] = "course:payariq"
    await call.message.edit_reply_markup(samarqaand_tumalari)


@dp.callback_query_handler(samarqand_callback.filter(item_name='pastdargom'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="pastdargom", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][2][2]['text'] = "❌ Pastdarg'om"
    samarqaand_tumalari['inline_keyboard'][2][2]['callback_data'] = "course:pastdar"
    await call.message.edit_reply_markup(samarqaand_tumalari)

@dp.callback_query_handler(samarqand_callback.filter(item_name='pastdar'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Samarqand", tuman="pastdargom", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][2][2]['text'] = "✅ Pastdarg'om"
    samarqaand_tumalari['inline_keyboard'][2][2]['callback_data'] = "course:pastdargom"
    await call.message.edit_reply_markup(samarqaand_tumalari)


@dp.callback_query_handler(samarqand_callback.filter(item_name='samarqand shahar'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="samarqand shahar", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][2][3]['text'] = "❌ Samarqand shahar"
    samarqaand_tumalari['inline_keyboard'][2][3]['callback_data'] = "course:samarqq"
    await call.message.edit_reply_markup(samarqaand_tumalari)

@dp.callback_query_handler(samarqand_callback.filter(item_name='samarqq'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Samarqand", tuman="samarqand shahar", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][2][3]['text'] = "✅ Samarqand shahar"
    samarqaand_tumalari['inline_keyboard'][2][3]['callback_data'] = "course:samarqand shahar"
    await call.message.edit_reply_markup(samarqaand_tumalari)



@dp.callback_query_handler(samarqand_callback.filter(item_name='toyloq'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="toyloq", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][3][0]['text'] = "❌ Toyloq"
    samarqaand_tumalari['inline_keyboard'][3][0]['callback_data'] = "course:toylo"
    await call.message.edit_reply_markup(samarqaand_tumalari)

@dp.callback_query_handler(samarqand_callback.filter(item_name='toylo'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Samarqand", tuman="toyloq", telegram_id=call.from_user.id)
    samarqaand_tumalari['inline_keyboard'][3][0]['text'] = "✅ Toyloq"
    samarqaand_tumalari['inline_keyboard'][3][0]['callback_data'] = "course:toyloq"
    await call.message.edit_reply_markup(samarqaand_tumalari)