from loader import dp, db
from aiogram.types import CallbackQuery
from keyboards.inline.yolovchi.callback_data import  viloyatlar_callback,qashqadaryo_callback
from keyboards.inline.yolovchi.qashtuman import qashqadaryo_tumanlari
Dehqonobod={*()}
Kasbi={*()}
Kitob={*()}
Koson={*()}
Koʻkdala={*()}
Mirishkor={*()}
Muborak={*()}
Nishon={*()}
Qamashi={*()}
Qarshi={*()}
Yakkabogʻ={*()}
Gʻuzor={*()}
Shahrisabz={*()}
Chiroqchi={*()}
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='qadaryyy'))
async def qashqadaryo_edit(call: CallbackQuery):
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="dehqonobod", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="kasbi", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="kitob", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="koson", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="kokdala", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="mirishkor", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="muborak", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="nishon", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="qamashi", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="qarshi", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="yakkabog", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="guzor", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="shahrisabz", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="chiroqchi", telegram_id=call.from_user.id)

    await call.message.answer("Qashqadaryo viloyati tumanlari ", reply_markup=qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='dehqonobod'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="dehqonobod", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][0][0]['text'] = "❌ Dehqonobod"
    qashqadaryo_tumanlari['inline_keyboard'][0][0]['callback_data'] = "course:dehqon"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='dehqon'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="dehqonobod", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][0][0]['text'] = "✅ Dehqonobod"
    qashqadaryo_tumanlari['inline_keyboard'][0][0]['callback_data'] = "course:dehqonobod"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='kasbi'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="kasbi", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][0][1]['text'] = "❌ Kasbi"
    qashqadaryo_tumanlari['inline_keyboard'][0][1]['callback_data'] = "course:kasb"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='kasb'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="kasbi", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][0][1]['text'] = "✅ Kasbi"
    qashqadaryo_tumanlari['inline_keyboard'][0][1]['callback_data'] = "course:kasbi"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='kitob'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="kitob", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][0][2]['text'] = "❌ Kitob"
    qashqadaryo_tumanlari['inline_keyboard'][0][2]['callback_data'] = "course:kitoblar"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='kitoblar'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="kitob", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][0][2]['text'] = "✅ Kitob"
    qashqadaryo_tumanlari['inline_keyboard'][0][2]['callback_data'] = "course:kitob"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='koson'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="koson", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][0][3]['text'] = "❌ Koson"
    qashqadaryo_tumanlari['inline_keyboard'][0][3]['callback_data'] = "course:koso"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='koso'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="koson", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][0][3]['text'] = "✅ Koson"
    qashqadaryo_tumanlari['inline_keyboard'][0][3]['callback_data'] = "course:koson"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='kokdala'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="kokdala", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][1][0]['text'] = "❌ Ko'kdala"
    qashqadaryo_tumanlari['inline_keyboard'][1][0]['callback_data'] = "course:kokda"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='kokda'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="kokdala", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][1][0]['text'] = "✅ Ko'kdala"
    qashqadaryo_tumanlari['inline_keyboard'][1][0]['callback_data'] = "course:kokdala"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='mirishkor'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="mirishkor", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][1][1]['text'] = "❌ Mirishkor"
    qashqadaryo_tumanlari['inline_keyboard'][1][1]['callback_data'] = "course:mirish"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='mirish'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="mirishkor", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][1][1]['text'] = "✅ Mirishkor"
    qashqadaryo_tumanlari['inline_keyboard'][1][1]['callback_data'] = "course:mirishkor"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='muborak'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="muborak", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][1][2]['text'] = "❌ Muborak"
    qashqadaryo_tumanlari['inline_keyboard'][1][2]['callback_data'] = "course:mubor"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='mubor'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="muborak", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][1][2]['text'] = "✅ Muborak"
    qashqadaryo_tumanlari['inline_keyboard'][1][2]['callback_data'] = "course:muborak"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)



@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='nishon'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="nishon", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][1][3]['text'] = "❌ Nishon"
    qashqadaryo_tumanlari['inline_keyboard'][1][3]['callback_data'] = "course:nisho"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='nisho'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="nishon", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][1][3]['text'] = "✅ Nishon"
    qashqadaryo_tumanlari['inline_keyboard'][1][3]['callback_data'] = "course:nishon"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)



@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='qamashi'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="qamashi", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][2][0]['text'] = "❌ Qamashi"
    qashqadaryo_tumanlari['inline_keyboard'][2][0]['callback_data'] = "course:qamas"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='qamas'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="qamashi", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][2][0]['text'] = "✅ Qamashi"
    qashqadaryo_tumanlari['inline_keyboard'][2][0]['callback_data'] = "course:qamashi"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)



@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='qarshi'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="qarshi", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][2][1]['text'] = "❌ Qarshi"
    qashqadaryo_tumanlari['inline_keyboard'][2][1]['callback_data'] = "course:qars"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='qars'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="qarshi", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][2][1]['text'] = "✅ Qarshi"
    qashqadaryo_tumanlari['inline_keyboard'][2][1]['callback_data'] = "course:qarshi"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='yakkabog'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="yakkabog", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][2][2]['text'] = "❌ Yakkabog'"
    qashqadaryo_tumanlari['inline_keyboard'][2][2]['callback_data'] = "course:yak"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='yak'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="yakkabog", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][2][2]['text'] = "✅ Yakkabog'"
    qashqadaryo_tumanlari['inline_keyboard'][2][2]['callback_data'] = "course:yakkabog"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)



@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='guzor'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="guzor", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][2][3]['text'] = "❌ Guzor'"
    qashqadaryo_tumanlari['inline_keyboard'][2][3]['callback_data'] = "course:guz"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='guz'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="guzor", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][2][3]['text'] = "✅ Guzor'"
    qashqadaryo_tumanlari['inline_keyboard'][2][3]['callback_data'] = "course:guzor"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='shahrisabz'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="shahrisabz", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][3][0]['text'] = "❌ Shahrisabz'"
    qashqadaryo_tumanlari['inline_keyboard'][3][0]['callback_data'] = "course:shahri"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='shahri'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="shahrisabz", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][3][0]['text'] = "✅ Shahrisabz'"
    qashqadaryo_tumanlari['inline_keyboard'][3][0]['callback_data'] = "course:shahrisabz"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='chiroqchi'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="chiroqchi", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][3][1]['text'] = "❌ Chiroqchi'"
    qashqadaryo_tumanlari['inline_keyboard'][3][1]['callback_data'] = "course:chiroq"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='chiroq'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Qashqadaryo", tuman="chiroqchi", telegram_id=call.from_user.id)
    qashqadaryo_tumanlari['inline_keyboard'][3][1]['text'] = "✅ Chiroqchi'"
    qashqadaryo_tumanlari['inline_keyboard'][3][1]['callback_data'] = "course:chiroqchi"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)