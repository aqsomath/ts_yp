from loader import dp
from aiogram.types import CallbackQuery
from keyboards.inline.yolovchi.callback_data import  viloyatlar_callback, namangan_callback
from keyboards.inline.yolovchi.namtuman import namangan
Chortoq={*()}
Chust={*()}
Kosonsoy={*()}
Mingbuloq={*()}
Namanganshaxar={*()}
Norin={*()}
Pop={*()}
Toraqorgon={*()}
Uchqorgon={*()}
Uychi={*()}
Yangiqorgon={*()}
Davlatobod={*()}
YangiNamangan={*()}
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='gann'))
async def namangan_edit(call: CallbackQuery):
    await call.message.answer("Namangan viloyati tumanlari ", reply_markup=namangan)
    Chortoq.add(call.message.chat.id)
    Chust.add(call.message.chat.id)
    Kosonsoy.add(call.message.chat.id)
    Mingbuloq.add(call.message.chat.id)
    Namanganshaxar.add(call.message.chat.id)
    Norin.add(call.message.chat.id)
    Pop.add(call.message.chat.id)
    Toraqorgon.add(call.message.chat.id)
    Uchqorgon.add(call.message.chat.id)
    Uychi.add(call.message.chat.id)
    Yangiqorgon.add(call.message.chat.id)
    Davlatobod.add(call.message.chat.id)
    YangiNamangan.add(call.message.chat.id)

@dp.callback_query_handler(namangan_callback.filter(item_name='chortoq'))
async def chortoq(call: CallbackQuery):
    Chortoq.remove(call.message.chat.id)

    namangan['inline_keyboard'][0][0]['text'] = "❌ Chortoq"
    namangan['inline_keyboard'][0][0]['callback_data'] = "course:chor"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='chor'))
async def chortoq(call: CallbackQuery):
    Chortoq.add(call.message.chat.id)

    namangan['inline_keyboard'][0][0]['text'] = "✅ Chortoq"
    namangan['inline_keyboard'][0][0]['callback_data'] = "course:chortoq"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='chust'))
async def chortoq(call: CallbackQuery):
    Chust.add(call.message.chat.id)

    namangan['inline_keyboard'][0][1]['text'] = "❌ Chust"
    namangan['inline_keyboard'][0][1]['callback_data'] = "course:chus"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='chus'))
async def chortoq(call: CallbackQuery):
    Chust.remove(call.message.chat.id)

    namangan['inline_keyboard'][0][1]['text'] = "✅ Chust"
    namangan['inline_keyboard'][0][1]['callback_data'] = "course:chust"
    await call.message.edit_reply_markup(namangan)



@dp.callback_query_handler(namangan_callback.filter(item_name='kosonsoy'))
async def chortoq(call: CallbackQuery):
    Kosonsoy.remove(call.message.chat.id)

    namangan['inline_keyboard'][0][2]['text'] = "❌ Kosonsoy"
    namangan['inline_keyboard'][0][2]['callback_data'] = "course:kos"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='kos'))
async def chortoq(call: CallbackQuery):
    Kosonsoy.add(call.message.chat.id)

    namangan['inline_keyboard'][0][2]['text'] = "✅ Kosonsoy"
    namangan['inline_keyboard'][0][2]['callback_data'] = "course:kosonsoy"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='mingbuloq'))
async def chortoq(call: CallbackQuery):
    Mingbuloq.remove(call.message.chat.id)

    namangan['inline_keyboard'][0][3]['text'] = "❌ Mingbuloq"
    namangan['inline_keyboard'][0][3]['callback_data'] = "course:ming"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='ming'))
async def chortoq(call: CallbackQuery):
    Mingbuloq.add(call.message.chat.id)

    namangan['inline_keyboard'][0][3]['text'] = "✅ Mingbuloq"
    namangan['inline_keyboard'][0][3]['callback_data'] = "course:mingbuloq"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='namangan shaxar'))
async def chortoq(call: CallbackQuery):
    Namanganshaxar.remove(call.message.chat.id)

    namangan['inline_keyboard'][1][0]['text'] = "❌ Namangan shahar"
    namangan['inline_keyboard'][1][0]['callback_data'] = "course:nam"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='nam'))
async def chortoq(call: CallbackQuery):
    Namanganshaxar.add(call.message.chat.id)

    namangan['inline_keyboard'][1][0]['text'] = "✅ Namangan shahar"
    namangan['inline_keyboard'][1][0]['callback_data'] = "course:namangan shaxar"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='norin'))
async def chortoq(call: CallbackQuery):
    Norin.remove(call.message.chat.id)

    namangan['inline_keyboard'][1][1]['text'] = "❌ Norin"
    namangan['inline_keyboard'][1][1]['callback_data'] = "course:nor"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='nor'))
async def chortoq(call: CallbackQuery):
    Norin.add(call.message.chat.id)

    namangan['inline_keyboard'][1][1]['text'] = "✅ Norin"
    namangan['inline_keyboard'][1][1]['callback_data'] = "course:norin"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='pop'))
async def chortoq(call: CallbackQuery):
    Pop.remove(call.message.chat.id)

    namangan['inline_keyboard'][1][2]['text'] = "❌ Pop"
    namangan['inline_keyboard'][1][2]['callback_data'] = "course:po"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='po'))
async def chortoq(call: CallbackQuery):
    Pop.add(call.message.chat.id)

    namangan['inline_keyboard'][1][2]['text'] = "✅ Pop"
    namangan['inline_keyboard'][1][2]['callback_data'] = "course:pop"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='toraqorgon'))
async def chortoq(call: CallbackQuery):
    Toraqorgon.remove(call.message.chat.id)

    namangan['inline_keyboard'][1][3]['text'] = "❌ To'raqo'rg'on"
    namangan['inline_keyboard'][1][3]['callback_data'] = "course:tora"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='tora'))
async def chortoq(call: CallbackQuery):
    Toraqorgon.add(call.message.chat.id)

    namangan['inline_keyboard'][1][3]['text'] = "✅ To'raqo'rg'on"
    namangan['inline_keyboard'][1][3]['callback_data'] = "course:toraqorgon"
    await call.message.edit_reply_markup(namangan)



@dp.callback_query_handler(namangan_callback.filter(item_name='uchqorgon'))
async def chortoq(call: CallbackQuery):
    Uchqorgon.remove(call.message.chat.id)

    namangan['inline_keyboard'][2][0]['text'] = "❌ Uchqo'rg'on"
    namangan['inline_keyboard'][2][0]['callback_data'] = "course:uchqor"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='uchqor'))
async def chortoq(call: CallbackQuery):
    Uchqorgon.add(call.message.chat.id)

    namangan['inline_keyboard'][2][0]['text'] = "✅ Uchqo'rg'on"
    namangan['inline_keyboard'][2][0]['callback_data'] = "course:uchqorgon"
    await call.message.edit_reply_markup(namangan)



@dp.callback_query_handler(namangan_callback.filter(item_name='uychi'))
async def chortoq(call: CallbackQuery):
    Uychi.remove(call.message.chat.id)

    namangan['inline_keyboard'][2][1]['text'] = "❌ Uychi"
    namangan['inline_keyboard'][2][1]['callback_data'] = "course:uy"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='uy'))
async def chortoq(call: CallbackQuery):
    Uychi.add(call.message.chat.id)

    namangan['inline_keyboard'][2][1]['text'] = "✅ Uychi"
    namangan['inline_keyboard'][2][1]['callback_data'] = "course:uychi"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='yangi qorgon'))
async def chortoq(call: CallbackQuery):
    Yangiqorgon.remove(call.message.chat.id)

    namangan['inline_keyboard'][2][2]['text'] = "❌ Yangiqo'rg'on"
    namangan['inline_keyboard'][2][2]['callback_data'] = "course:yqorgon"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='yqorgon'))
async def chortoq(call: CallbackQuery):
    Yangiqorgon.add(call.message.chat.id)

    namangan['inline_keyboard'][2][2]['text'] = "✅ Yangiqo'rg'on"
    namangan['inline_keyboard'][2][2]['callback_data'] = "course:yangi qorgon"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='davlatobod'))
async def chortoq(call: CallbackQuery):
    Davlatobod.remove(call.message.chat.id)

    namangan['inline_keyboard'][2][3]['text'] = "❌ Davlatobod"
    namangan['inline_keyboard'][2][3]['callback_data'] = "course:davlato"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='davlato'))
async def chortoq(call: CallbackQuery):
    Davlatobod.add(call.message.chat.id)

    namangan['inline_keyboard'][2][3]['text'] = "✅ Davlatobod"
    namangan['inline_keyboard'][2][3]['callback_data'] = "course:davlatobod"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='yangi namangan'))
async def chortoq(call: CallbackQuery):
    YangiNamangan.remove(call.message.chat.id)

    namangan['inline_keyboard'][3][0]['text'] = "❌ Yangi Namangan"
    namangan['inline_keyboard'][3][0]['callback_data'] = "course:namanyan"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='namanyan'))
async def chortoq(call: CallbackQuery):
    YangiNamangan.add(call.message.chat.id)

    namangan['inline_keyboard'][3][0]['text'] = "✅ Yangi Namangan"
    namangan['inline_keyboard'][3][0]['callback_data'] = "course:yangi namangan"
    await call.message.edit_reply_markup(namangan)

