from loader import dp, db
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
    await db.add_driver_info(viloyat="Namangan", tuman="chortoq", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Namangan", tuman="chust", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Namangan", tuman="kosonsoy", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Namangan", tuman="mingbuloq", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Namangan", tuman="namangan shaxar", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Namangan", tuman="norin", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Namangan", tuman="pop", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Namangan", tuman="toraqo'rg'on", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Namangan", tuman="uchqo'rgo'n", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Namangan", tuman="uychi", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Namangan", tuman="yangi qo'rg'on", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Namangan", tuman="davlatobod", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Namangan", tuman="yangi namangan", telegram_id=call.from_user.id)

    await call.message.answer("Namangan viloyati tumanlari ", reply_markup=namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='chortoq'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="chortoq", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][0][0]['text'] = "❌ Chortoq"
    namangan['inline_keyboard'][0][0]['callback_data'] = "course:chor"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='chor'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Namangan", tuman="chortoq", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][0][0]['text'] = "✅ Chortoq"
    namangan['inline_keyboard'][0][0]['callback_data'] = "course:chortoq"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='chust'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="chust", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][0][1]['text'] = "❌ Chust"
    namangan['inline_keyboard'][0][1]['callback_data'] = "course:chus"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='chus'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Namangan", tuman="chust", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][0][1]['text'] = "✅ Chust"
    namangan['inline_keyboard'][0][1]['callback_data'] = "course:chust"
    await call.message.edit_reply_markup(namangan)



@dp.callback_query_handler(namangan_callback.filter(item_name='kosonsoy'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="kosonsoy", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][0][2]['text'] = "❌ Kosonsoy"
    namangan['inline_keyboard'][0][2]['callback_data'] = "course:kos"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='kos'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Namangan", tuman="kosonsoy", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][0][2]['text'] = "✅ Kosonsoy"
    namangan['inline_keyboard'][0][2]['callback_data'] = "course:kosonsoy"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='mingbuloq'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="namangan shaxar", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][0][3]['text'] = "❌ Mingbuloq"
    namangan['inline_keyboard'][0][3]['callback_data'] = "course:ming"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='ming'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Namangan", tuman="mingbuloq", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][0][3]['text'] = "✅ Mingbuloq"
    namangan['inline_keyboard'][0][3]['callback_data'] = "course:mingbuloq"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='namangan shaxar'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="namangan shaxar", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][1][0]['text'] = "❌ Namangan shahar"
    namangan['inline_keyboard'][1][0]['callback_data'] = "course:nam"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='nam'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Namangan", tuman="namangan shaxar", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][1][0]['text'] = "✅ Namangan shahar"
    namangan['inline_keyboard'][1][0]['callback_data'] = "course:namangan shaxar"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='norin'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="norin", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][1][1]['text'] = "❌ Norin"
    namangan['inline_keyboard'][1][1]['callback_data'] = "course:nor"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='nor'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Namangan", tuman="norin", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][1][1]['text'] = "✅ Norin"
    namangan['inline_keyboard'][1][1]['callback_data'] = "course:norin"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='pop'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="pop", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][1][2]['text'] = "❌ Pop"
    namangan['inline_keyboard'][1][2]['callback_data'] = "course:po"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='po'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Namangan", tuman="pop", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][1][2]['text'] = "✅ Pop"
    namangan['inline_keyboard'][1][2]['callback_data'] = "course:pop"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='toraqorgon'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="toraqo'rgo'n", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][1][3]['text'] = "❌ To'raqo'rg'on"
    namangan['inline_keyboard'][1][3]['callback_data'] = "course:tora"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='tora'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Namangan", tuman="toraqo'rgo'n", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][1][3]['text'] = "✅ To'raqo'rg'on"
    namangan['inline_keyboard'][1][3]['callback_data'] = "course:toraqorgon"
    await call.message.edit_reply_markup(namangan)



@dp.callback_query_handler(namangan_callback.filter(item_name='uchqorgon'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="uchqo'rg'on", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][2][0]['text'] = "❌ Uchqo'rg'on"
    namangan['inline_keyboard'][2][0]['callback_data'] = "course:uchqor"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='uchqor'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Namangan", tuman="uchqo'rg'on", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][2][0]['text'] = "✅ Uchqo'rg'on"
    namangan['inline_keyboard'][2][0]['callback_data'] = "course:uchqorgon"
    await call.message.edit_reply_markup(namangan)



@dp.callback_query_handler(namangan_callback.filter(item_name='uychi'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="uychi", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][2][1]['text'] = "❌ Uychi"
    namangan['inline_keyboard'][2][1]['callback_data'] = "course:uy"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='uy'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Namangan", tuman="uychi", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][2][1]['text'] = "✅ Uychi"
    namangan['inline_keyboard'][2][1]['callback_data'] = "course:uychi"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='yangi qorgon'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="yangi qo'g'on", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][2][2]['text'] = "❌ Yangiqo'rg'on"
    namangan['inline_keyboard'][2][2]['callback_data'] = "course:yqorgon"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='yqorgon'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Namangan", tuman="yangi qo'rg'on", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][2][2]['text'] = "✅ Yangiqo'rg'on"
    namangan['inline_keyboard'][2][2]['callback_data'] = "course:yangi qorgon"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='davlatobod'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="davlatobod", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][2][3]['text'] = "❌ Davlatobod"
    namangan['inline_keyboard'][2][3]['callback_data'] = "course:davlato"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='davlato'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Namangan", tuman="davlatobod", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][2][3]['text'] = "✅ Davlatobod"
    namangan['inline_keyboard'][2][3]['callback_data'] = "course:davlatobod"
    await call.message.edit_reply_markup(namangan)


@dp.callback_query_handler(namangan_callback.filter(item_name='yangi namangan'))
async def chortoq(call: CallbackQuery):
    await db.delete_driver_info(tuman="yangi namangan", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][3][0]['text'] = "❌ Yangi Namangan"
    namangan['inline_keyboard'][3][0]['callback_data'] = "course:namanyan"
    await call.message.edit_reply_markup(namangan)

@dp.callback_query_handler(namangan_callback.filter(item_name='namanyan'))
async def chortoq(call: CallbackQuery):
    await db.add_driver_info(viloyat="Namangan", tuman="yangi namangan", telegram_id=call.from_user.id)
    namangan['inline_keyboard'][3][0]['text'] = "✅ Yangi Namangan"
    namangan['inline_keyboard'][3][0]['callback_data'] = "course:yangi namangan"
    await call.message.edit_reply_markup(namangan)

