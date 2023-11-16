from aiogram.types import CallbackQuery

from keyboards.inline.yolovchi.callback_data import viloyatlar_callback,surxon_callback
from keyboards.inline.yolovchi.surtuman import surxondaryo_tuman
from loader import dp, db

Angor={*()}
Bandixon={*()}
Boysun={*()}
Denov={*()}
Jarqorgon={*()}
Qiziriq={*()}
Qumqorgon={*()}
Muzrabod={*()}
Oltinsoy={*()}
Sariosiyo={*()}
Sherobod={*()}
Shorchi={*()}
Termiz={*()}
Uzun={*()}

@dp.callback_query_handler(viloyatlar_callback.filter(item_name='xonn'))
async def surxontuman(call:CallbackQuery):
    await db.add_driver_info(viloyat="Surxondaryo", tuman="angor", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Surxondaryo", tuman="bandixon", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Surxondaryo", tuman="boysun", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Surxondaryo", tuman="denov", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Surxondaryo", tuman="jarqorgon", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Surxondaryo", tuman="qiziriq", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Surxondaryo", tuman="qumqorgon", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Surxondaryo", tuman="muzrabod", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Surxondaryo", tuman="oltinsoy", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Surxondaryo", tuman="sariosiyo", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Surxondaryo", tuman="sherobod", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Surxondaryo", tuman="shorchi", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Surxondaryo", tuman="termiz", telegram_id=call.from_user.id)
    await db.add_driver_info(viloyat="Surxondaryo", tuman="uzun", telegram_id=call.from_user.id)
    await call.message.answer("Surxondaryo tumanlari", reply_markup=surxondaryo_tuman)


@dp.callback_query_handler(surxon_callback.filter(item_name='angor'))
async def toshkenttuman(call:CallbackQuery):
    await db.delete_driver_info(tuman="angor", telegram_id=call.from_user.id)
    surxondaryo_tuman['inline_keyboard'][0][0]['text'] = "❌ Angor"
    surxondaryo_tuman['inline_keyboard'][0][0]['callback_data'] = "course:ango"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='ango'))
async def toshkenttuman(call:CallbackQuery):
    await db.add_driver_info(viloyat="Surxondaryo", tuman="angor", telegram_id=call.from_user.id)
    surxondaryo_tuman['inline_keyboard'][0][0]['text'] = "✅ Angor"
    surxondaryo_tuman['inline_keyboard'][0][0]['callback_data'] = "course:angor"
    await call.message.edit_reply_markup(surxondaryo_tuman)


@dp.callback_query_handler(surxon_callback.filter(item_name='bandixon'))
async def toshkenttuman(call:CallbackQuery):
    await db.delete_driver_info(tuman="bandixon", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][0][1]['text'] = "❌ Bandixon"
    surxondaryo_tuman['inline_keyboard'][0][1]['callback_data'] = "course:bandi"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='bandi'))
async def toshkenttuman(call:CallbackQuery):
    await db.add_driver_info(viloyat="Surxondaryo", tuman="bandixon", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][0][1]['text'] = "✅ Bandixon"
    surxondaryo_tuman['inline_keyboard'][0][1]['callback_data'] = "course:bandixon"
    await call.message.edit_reply_markup(surxondaryo_tuman)


@dp.callback_query_handler(surxon_callback.filter(item_name='boysun'))
async def toshkenttuman(call:CallbackQuery):
    await db.delete_driver_info(tuman="boysun", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][0][2]['text'] = "❌ Boysun"
    surxondaryo_tuman['inline_keyboard'][0][2]['callback_data'] = "course:boysu"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='boysu'))
async def toshkenttuman(call:CallbackQuery):
    await db.add_driver_info(viloyat="Surxondaryo", tuman="boysun", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][0][2]['text'] = "✅ Boysun"
    surxondaryo_tuman['inline_keyboard'][0][2]['callback_data'] = "course:boysun"
    await call.message.edit_reply_markup(surxondaryo_tuman)


@dp.callback_query_handler(surxon_callback.filter(item_name='denov'))
async def toshkenttuman(call:CallbackQuery):
    await db.delete_driver_info(tuman="denov", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][0][3]['text'] = "❌ Denov"
    surxondaryo_tuman['inline_keyboard'][0][3]['callback_data'] = "course:denoo"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='denoo'))
async def toshkenttuman(call:CallbackQuery):
    await db.add_driver_info(viloyat="Surxondaryo", tuman="denov", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][0][3]['text'] = "✅ Denov"
    surxondaryo_tuman['inline_keyboard'][0][3]['callback_data'] = "course:denov"
    await call.message.edit_reply_markup(surxondaryo_tuman)


@dp.callback_query_handler(surxon_callback.filter(item_name='jarqorgon'))
async def toshkenttuman(call:CallbackQuery):
    await db.delete_driver_info(tuman="jarqorgon", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][1][0]['text'] = "❌ Jarqo'rg'on"
    surxondaryo_tuman['inline_keyboard'][1][0]['callback_data'] = "course:jaar"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='jaar'))
async def toshkenttuman(call:CallbackQuery):
    await db.add_driver_info(viloyat="Surxondaryo", tuman="jarqorgon", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][1][0]['text'] = "✅ Jarqo'rg'on"
    surxondaryo_tuman['inline_keyboard'][1][0]['callback_data'] = "course:jarqorgon"
    await call.message.edit_reply_markup(surxondaryo_tuman)


@dp.callback_query_handler(surxon_callback.filter(item_name='qiziriq'))
async def toshkenttuman(call:CallbackQuery):
    await db.delete_driver_info(tuman="qiziriq", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][1][1]['text'] = "❌ Qiziriq"
    surxondaryo_tuman['inline_keyboard'][1][1]['callback_data'] = "course:qizir"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='qizir'))
async def toshkenttuman(call:CallbackQuery):
    await db.add_driver_info(viloyat="Surxondaryo", tuman="qiziriq", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][1][1]['text'] = "✅ Qiziriq"
    surxondaryo_tuman['inline_keyboard'][1][1]['callback_data'] = "course:qiziriq"
    await call.message.edit_reply_markup(surxondaryo_tuman)


@dp.callback_query_handler(surxon_callback.filter(item_name='qumqorgon'))
async def toshkenttuman(call:CallbackQuery):
    await db.delete_driver_info(tuman="qumqorgon", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][1][2]['text'] = "❌ Qumqo'rg'on"
    surxondaryo_tuman['inline_keyboard'][1][2]['callback_data'] = "course:qumqor"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='qumqor'))
async def toshkenttuman(call:CallbackQuery):
    await db.add_driver_info(viloyat="Surxondaryo", tuman="qumqorgon", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][1][2]['text'] = "✅ Qumqo'rg'on"
    surxondaryo_tuman['inline_keyboard'][1][2]['callback_data'] = "course:qumqorgon"
    await call.message.edit_reply_markup(surxondaryo_tuman)


@dp.callback_query_handler(surxon_callback.filter(item_name='muzrabod'))
async def toshkenttuman(call:CallbackQuery):
    await db.delete_driver_info(tuman="muzrabod", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][1][3]['text'] = "❌ Muzrabod"
    surxondaryo_tuman['inline_keyboard'][1][3]['callback_data'] = "course:muzra"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='muzra'))
async def toshkenttuman(call:CallbackQuery):
    await db.add_driver_info(viloyat="Surxondaryo", tuman="muzrabod", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][1][3]['text'] = "✅ Muzrabod"
    surxondaryo_tuman['inline_keyboard'][1][3]['callback_data'] = "course:muzrabod"
    await call.message.edit_reply_markup(surxondaryo_tuman)



@dp.callback_query_handler(surxon_callback.filter(item_name='oltinsoy'))
async def toshkenttuman(call:CallbackQuery):
    await db.delete_driver_info(tuman="oltinsoy", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][2][0]['text'] = "❌ Oltinsoy"
    surxondaryo_tuman['inline_keyboard'][2][0]['callback_data'] = "course:oltinso"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='oltinso'))
async def toshkenttuman(call:CallbackQuery):
    await db.add_driver_info(viloyat="Surxondaryo", tuman="oltinsoy", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][2][0]['text'] = "✅ Oltinsoy"
    surxondaryo_tuman['inline_keyboard'][2][0]['callback_data'] = "course:oltinsoy"
    await call.message.edit_reply_markup(surxondaryo_tuman)



@dp.callback_query_handler(surxon_callback.filter(item_name='sariosiyo'))
async def toshkenttuman(call:CallbackQuery):
    await db.delete_driver_info(tuman="sariosiyo", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][2][1]['text'] = "❌ Sariosiyo"
    surxondaryo_tuman['inline_keyboard'][2][1]['callback_data'] = "course:sari"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='sari'))
async def toshkenttuman(call:CallbackQuery):
    await db.add_driver_info(viloyat="Surxondaryo", tuman="sariosiyo", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][2][1]['text'] = "✅ Sariosiyo"
    surxondaryo_tuman['inline_keyboard'][2][1]['callback_data'] = "course:sariosiyo"
    await call.message.edit_reply_markup(surxondaryo_tuman)


@dp.callback_query_handler(surxon_callback.filter(item_name='sherobod'))
async def toshkenttuman(call:CallbackQuery):
    await db.delete_driver_info(tuman="sherobod", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][2][2]['text'] = "❌ Sherobod"
    surxondaryo_tuman['inline_keyboard'][2][2]['callback_data'] = "course:shero"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='shero'))
async def toshkenttuman(call:CallbackQuery):
    await db.add_driver_info(viloyat="Surxondaryo", tuman="sherobod", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][2][2]['text'] = "✅ Sherobod"
    surxondaryo_tuman['inline_keyboard'][2][2]['callback_data'] = "course:sherobod"
    await call.message.edit_reply_markup(surxondaryo_tuman)



@dp.callback_query_handler(surxon_callback.filter(item_name='shorchi'))
async def toshkenttuman(call:CallbackQuery):
    await db.delete_driver_info(tuman="shorchi", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][2][3]['text'] = "❌ Sho'rchi"
    surxondaryo_tuman['inline_keyboard'][2][3]['callback_data'] = "course:shroc"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='shroc'))
async def toshkenttuman(call:CallbackQuery):
    await db.add_driver_info(viloyat="Surxondaryo", tuman="shorchi", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][2][3]['text'] = "✅ Sho'rchi"
    surxondaryo_tuman['inline_keyboard'][2][3]['callback_data'] = "course:shorchi"
    await call.message.edit_reply_markup(surxondaryo_tuman)



@dp.callback_query_handler(surxon_callback.filter(item_name='termiz'))
async def toshkenttuman(call:CallbackQuery):
    await db.delete_driver_info(tuman="termiz", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][3][0]['text'] = "❌ Termiz"
    surxondaryo_tuman['inline_keyboard'][3][0]['callback_data'] = "course:termi"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='termi'))
async def toshkenttuman(call:CallbackQuery):
    await db.add_driver_info(viloyat="Surxondaryo", tuman="termiz", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][3][0]['text'] = "✅ Termiz"
    surxondaryo_tuman['inline_keyboard'][3][0]['callback_data'] = "course:termiz"
    await call.message.edit_reply_markup(surxondaryo_tuman)



@dp.callback_query_handler(surxon_callback.filter(item_name='uzun'))
async def toshkenttuman(call:CallbackQuery):
    await db.delete_driver_info(tuman="uzun", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][3][1]['text'] = "❌ Uzun"
    surxondaryo_tuman['inline_keyboard'][3][1]['callback_data'] = "course:uzu"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='uzu'))
async def toshkenttuman(call:CallbackQuery):
    await db.add_driver_info(viloyat="Surxondaryo", tuman="uzun", telegram_id=call.from_user.id)

    surxondaryo_tuman['inline_keyboard'][3][1]['text'] = "✅ Uzun"
    surxondaryo_tuman['inline_keyboard'][3][1]['callback_data'] = "course:uzun"
    await call.message.edit_reply_markup(surxondaryo_tuman)