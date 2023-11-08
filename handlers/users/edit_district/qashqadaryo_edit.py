from loader import dp
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
    await call.message.answer("Qashqadaryo viloyati tumanlari ", reply_markup=qashqadaryo_tumanlari)
    Dehqonobod.add(call.message.chat.id)
    Chiroqchi.add(call.message.chat.id)
    Shahrisabz.add(call.message.chat.id)
    Gʻuzor.add(call.message.chat.id)
    Yakkabogʻ.add(call.message.chat.id)
    Qarshi.add(call.message.chat.id)
    Qamashi.add(call.message.chat.id)
    Nishon.add(call.message.chat.id)
    Muborak.add(call.message.chat.id)
    Mirishkor.add(call.message.chat.id)
    Koʻkdala.add(call.message.chat.id)
    Koson.add(call.message.chat.id)
    Kitob.add(call.message.chat.id)
    Kasbi.add(call.message.chat.id)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='dehqonobod'))
async def chortoq(call: CallbackQuery):
    Dehqonobod.remove(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][0][0]['text'] = "❌ Dehqonobod"
    qashqadaryo_tumanlari['inline_keyboard'][0][0]['callback_data'] = "course:dehqon"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='dehqon'))
async def chortoq(call: CallbackQuery):
    Dehqonobod.add(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][0][0]['text'] = "✅ Dehqonobod"
    qashqadaryo_tumanlari['inline_keyboard'][0][0]['callback_data'] = "course:dehqonobod"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='kasbi'))
async def chortoq(call: CallbackQuery):
    Kasbi.remove(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][0][1]['text'] = "❌ Kasbi"
    qashqadaryo_tumanlari['inline_keyboard'][0][1]['callback_data'] = "course:kasb"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='kasb'))
async def chortoq(call: CallbackQuery):
    Kasbi.add(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][0][1]['text'] = "✅ Kasbi"
    qashqadaryo_tumanlari['inline_keyboard'][0][1]['callback_data'] = "course:kasbi"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='kitob'))
async def chortoq(call: CallbackQuery):
    Kitob.remove(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][0][2]['text'] = "❌ Kitob"
    qashqadaryo_tumanlari['inline_keyboard'][0][2]['callback_data'] = "course:kitoblar"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='kitoblar'))
async def chortoq(call: CallbackQuery):
    Kitob.add(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][0][2]['text'] = "✅ Kitob"
    qashqadaryo_tumanlari['inline_keyboard'][0][2]['callback_data'] = "course:kitob"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='koson'))
async def chortoq(call: CallbackQuery):
    Koson.remove(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][0][3]['text'] = "❌ Koson"
    qashqadaryo_tumanlari['inline_keyboard'][0][3]['callback_data'] = "course:koso"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='koso'))
async def chortoq(call: CallbackQuery):
    Koson.add(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][0][3]['text'] = "✅ Koson"
    qashqadaryo_tumanlari['inline_keyboard'][0][3]['callback_data'] = "course:koson"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='kokdala'))
async def chortoq(call: CallbackQuery):
    Koʻkdala.remove(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][1][0]['text'] = "❌ Ko'kdala"
    qashqadaryo_tumanlari['inline_keyboard'][1][0]['callback_data'] = "course:kokda"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='kokda'))
async def chortoq(call: CallbackQuery):
    Koʻkdala.add(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][1][0]['text'] = "✅ Ko'kdala"
    qashqadaryo_tumanlari['inline_keyboard'][1][0]['callback_data'] = "course:kokdala"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='mirishkor'))
async def chortoq(call: CallbackQuery):
    Mirishkor.remove(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][1][1]['text'] = "❌ Mirishkor"
    qashqadaryo_tumanlari['inline_keyboard'][1][1]['callback_data'] = "course:mirish"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='mirish'))
async def chortoq(call: CallbackQuery):
    Mirishkor.add(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][1][1]['text'] = "✅ Mirishkor"
    qashqadaryo_tumanlari['inline_keyboard'][1][1]['callback_data'] = "course:mirishkor"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='muborak'))
async def chortoq(call: CallbackQuery):
    Muborak.remove(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][1][2]['text'] = "❌ Muborak"
    qashqadaryo_tumanlari['inline_keyboard'][1][2]['callback_data'] = "course:mubor"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='mubor'))
async def chortoq(call: CallbackQuery):
    Muborak.add(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][1][2]['text'] = "✅ Muborak"
    qashqadaryo_tumanlari['inline_keyboard'][1][2]['callback_data'] = "course:muborak"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)



@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='nishon'))
async def chortoq(call: CallbackQuery):
    Nishon.remove(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][1][3]['text'] = "❌ Nishon"
    qashqadaryo_tumanlari['inline_keyboard'][1][3]['callback_data'] = "course:nisho"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='nisho'))
async def chortoq(call: CallbackQuery):
    Nishon.add(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][1][3]['text'] = "✅ Nishon"
    qashqadaryo_tumanlari['inline_keyboard'][1][3]['callback_data'] = "course:nishon"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)



@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='qamashi'))
async def chortoq(call: CallbackQuery):
    Qamashi.remove(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][2][0]['text'] = "❌ Qamashi"
    qashqadaryo_tumanlari['inline_keyboard'][2][0]['callback_data'] = "course:qamas"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='qamas'))
async def chortoq(call: CallbackQuery):
    Qamashi.add(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][2][0]['text'] = "✅ Qamashi"
    qashqadaryo_tumanlari['inline_keyboard'][2][0]['callback_data'] = "course:qamashi"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)



@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='qarshi'))
async def chortoq(call: CallbackQuery):
    Qarshi.remove(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][2][1]['text'] = "❌ Qarshi"
    qashqadaryo_tumanlari['inline_keyboard'][2][1]['callback_data'] = "course:qars"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='qars'))
async def chortoq(call: CallbackQuery):
    Qarshi.add(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][2][1]['text'] = "✅ Qarshi"
    qashqadaryo_tumanlari['inline_keyboard'][2][1]['callback_data'] = "course:qarshi"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='yakkabog'))
async def chortoq(call: CallbackQuery):
    Yakkabogʻ.remove(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][2][2]['text'] = "❌ Yakkabog'"
    qashqadaryo_tumanlari['inline_keyboard'][2][2]['callback_data'] = "course:yak"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='yak'))
async def chortoq(call: CallbackQuery):
    Yakkabogʻ.add(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][2][2]['text'] = "✅ Yakkabog'"
    qashqadaryo_tumanlari['inline_keyboard'][2][2]['callback_data'] = "course:yakkabog"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)



@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='guzor'))
async def chortoq(call: CallbackQuery):
    Gʻuzor.remove(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][2][3]['text'] = "❌ Guzor'"
    qashqadaryo_tumanlari['inline_keyboard'][2][3]['callback_data'] = "course:guz"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='guz'))
async def chortoq(call: CallbackQuery):
    Gʻuzor.add(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][2][3]['text'] = "✅ Guzor'"
    qashqadaryo_tumanlari['inline_keyboard'][2][3]['callback_data'] = "course:guzor"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='shahrisabz'))
async def chortoq(call: CallbackQuery):
    Shahrisabz.remove(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][3][0]['text'] = "❌ Shahrisabz'"
    qashqadaryo_tumanlari['inline_keyboard'][3][0]['callback_data'] = "course:shahri"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='shahri'))
async def chortoq(call: CallbackQuery):
    Shahrisabz.add(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][3][0]['text'] = "✅ Shahrisabz'"
    qashqadaryo_tumanlari['inline_keyboard'][3][0]['callback_data'] = "course:shahrisabz"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)


@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='chiroqchi'))
async def chortoq(call: CallbackQuery):
    Chiroqchi.remove(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][3][1]['text'] = "❌ Chiroqchi'"
    qashqadaryo_tumanlari['inline_keyboard'][3][1]['callback_data'] = "course:chiroq"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)

@dp.callback_query_handler(qashqadaryo_callback.filter(item_name='chiroq'))
async def chortoq(call: CallbackQuery):
    Chiroqchi.add(call.message.chat.id)

    qashqadaryo_tumanlari['inline_keyboard'][3][1]['text'] = "✅ Chiroqchi'"
    qashqadaryo_tumanlari['inline_keyboard'][3][1]['callback_data'] = "course:chiroqchi"
    await call.message.edit_reply_markup(qashqadaryo_tumanlari)