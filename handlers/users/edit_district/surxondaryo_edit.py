from aiogram.types import CallbackQuery

from keyboards.inline.yolovchi.callback_data import viloyatlar_callback,surxon_callback
from keyboards.inline.yolovchi.surtuman import surxondaryo_tuman
from loader import dp

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
    await call.message.answer("Surxondaryo tumanlari", reply_markup=surxondaryo_tuman)
    Angor.add(call.message.chat.id)
    Bandixon.add(call.message.chat.id)
    Boysun.add(call.message.chat.id)
    Denov.add(call.message.chat.id)
    Jarqorgon.add(call.message.chat.id)
    Qiziriq.add(call.message.chat.id)
    Qumqorgon.add(call.message.chat.id)
    Muzrabod.add(call.message.chat.id)
    Oltinsoy.add(call.message.chat.id)
    Sariosiyo.add(call.message.chat.id)
    Sherobod.add(call.message.chat.id)
    Shorchi.add(call.message.chat.id)
    Termiz.add(call.message.chat.id)
    Uzun.add(call.message.chat.id)

@dp.callback_query_handler(surxon_callback.filter(item_name='angor'))
async def toshkenttuman(call:CallbackQuery):
    Angor.remove(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][0][0]['text'] = "❌ Angor"
    surxondaryo_tuman['inline_keyboard'][0][0]['callback_data'] = "course:ango"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='ango'))
async def toshkenttuman(call:CallbackQuery):
    Angor.add(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][0][0]['text'] = "✅ Angor"
    surxondaryo_tuman['inline_keyboard'][0][0]['callback_data'] = "course:angor"
    await call.message.edit_reply_markup(surxondaryo_tuman)


@dp.callback_query_handler(surxon_callback.filter(item_name='bandixon'))
async def toshkenttuman(call:CallbackQuery):
    Bandixon.remove(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][0][1]['text'] = "❌ Bandixon"
    surxondaryo_tuman['inline_keyboard'][0][1]['callback_data'] = "course:bandi"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='bandi'))
async def toshkenttuman(call:CallbackQuery):
    Bandixon.add(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][0][1]['text'] = "✅ Bandixon"
    surxondaryo_tuman['inline_keyboard'][0][1]['callback_data'] = "course:bandixon"
    await call.message.edit_reply_markup(surxondaryo_tuman)


@dp.callback_query_handler(surxon_callback.filter(item_name='boysun'))
async def toshkenttuman(call:CallbackQuery):
    Boysun.remove(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][0][2]['text'] = "❌ Boysun"
    surxondaryo_tuman['inline_keyboard'][0][2]['callback_data'] = "course:boysu"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='boysu'))
async def toshkenttuman(call:CallbackQuery):
    Boysun.add(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][0][2]['text'] = "✅ Boysun"
    surxondaryo_tuman['inline_keyboard'][0][2]['callback_data'] = "course:boysun"
    await call.message.edit_reply_markup(surxondaryo_tuman)


@dp.callback_query_handler(surxon_callback.filter(item_name='denov'))
async def toshkenttuman(call:CallbackQuery):
    Denov.remove(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][0][3]['text'] = "❌ Denov"
    surxondaryo_tuman['inline_keyboard'][0][3]['callback_data'] = "course:denoo"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='denoo'))
async def toshkenttuman(call:CallbackQuery):
    Denov.add(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][0][3]['text'] = "✅ Denov"
    surxondaryo_tuman['inline_keyboard'][0][3]['callback_data'] = "course:denov"
    await call.message.edit_reply_markup(surxondaryo_tuman)


@dp.callback_query_handler(surxon_callback.filter(item_name='jarqorgon'))
async def toshkenttuman(call:CallbackQuery):
    Jarqorgon.remove(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][1][0]['text'] = "❌ Jarqo'rg'on"
    surxondaryo_tuman['inline_keyboard'][1][0]['callback_data'] = "course:jaar"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='jaar'))
async def toshkenttuman(call:CallbackQuery):
    Jarqorgon.add(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][1][0]['text'] = "✅ Jarqo'rg'on"
    surxondaryo_tuman['inline_keyboard'][1][0]['callback_data'] = "course:jarqorgon"
    await call.message.edit_reply_markup(surxondaryo_tuman)


@dp.callback_query_handler(surxon_callback.filter(item_name='qiziriq'))
async def toshkenttuman(call:CallbackQuery):
    Qiziriq.remove(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][1][1]['text'] = "❌ Qiziriq"
    surxondaryo_tuman['inline_keyboard'][1][1]['callback_data'] = "course:qizir"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='qizir'))
async def toshkenttuman(call:CallbackQuery):
    Qiziriq.add(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][1][1]['text'] = "✅ Qiziriq"
    surxondaryo_tuman['inline_keyboard'][1][1]['callback_data'] = "course:qiziriq"
    await call.message.edit_reply_markup(surxondaryo_tuman)


@dp.callback_query_handler(surxon_callback.filter(item_name='qumqorgon'))
async def toshkenttuman(call:CallbackQuery):
    Qumqorgon.remove(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][1][2]['text'] = "❌ Qumqo'rg'on"
    surxondaryo_tuman['inline_keyboard'][1][2]['callback_data'] = "course:qumqor"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='qumqor'))
async def toshkenttuman(call:CallbackQuery):
    Qumqorgon.add(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][1][2]['text'] = "✅ Qumqo'rg'on"
    surxondaryo_tuman['inline_keyboard'][1][2]['callback_data'] = "course:qumqorgon"
    await call.message.edit_reply_markup(surxondaryo_tuman)


@dp.callback_query_handler(surxon_callback.filter(item_name='muzrabod'))
async def toshkenttuman(call:CallbackQuery):
    Muzrabod.remove(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][1][3]['text'] = "❌ Muzrabod"
    surxondaryo_tuman['inline_keyboard'][1][3]['callback_data'] = "course:muzra"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='muzra'))
async def toshkenttuman(call:CallbackQuery):
    Muzrabod.add(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][1][3]['text'] = "✅ Muzrabod"
    surxondaryo_tuman['inline_keyboard'][1][3]['callback_data'] = "course:muzrabod"
    await call.message.edit_reply_markup(surxondaryo_tuman)



@dp.callback_query_handler(surxon_callback.filter(item_name='oltinsoy'))
async def toshkenttuman(call:CallbackQuery):
    Oltinsoy.remove(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][2][0]['text'] = "❌ Oltinsoy"
    surxondaryo_tuman['inline_keyboard'][2][0]['callback_data'] = "course:oltinso"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='oltinso'))
async def toshkenttuman(call:CallbackQuery):
    Oltinsoy.add(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][2][0]['text'] = "✅ Oltinsoy"
    surxondaryo_tuman['inline_keyboard'][2][0]['callback_data'] = "course:oltinsoy"
    await call.message.edit_reply_markup(surxondaryo_tuman)



@dp.callback_query_handler(surxon_callback.filter(item_name='sariosiyo'))
async def toshkenttuman(call:CallbackQuery):
    Sariosiyo.remove(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][2][1]['text'] = "❌ Sariosiyo"
    surxondaryo_tuman['inline_keyboard'][2][1]['callback_data'] = "course:sari"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='sari'))
async def toshkenttuman(call:CallbackQuery):
    Sariosiyo.add(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][2][1]['text'] = "✅ Sariosiyo"
    surxondaryo_tuman['inline_keyboard'][2][1]['callback_data'] = "course:sariosiyo"
    await call.message.edit_reply_markup(surxondaryo_tuman)


@dp.callback_query_handler(surxon_callback.filter(item_name='sherobod'))
async def toshkenttuman(call:CallbackQuery):
    Sherobod.remove(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][2][2]['text'] = "❌ Sherobod"
    surxondaryo_tuman['inline_keyboard'][2][2]['callback_data'] = "course:shero"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='shero'))
async def toshkenttuman(call:CallbackQuery):
    Sherobod.add(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][2][2]['text'] = "✅ Sherobod"
    surxondaryo_tuman['inline_keyboard'][2][2]['callback_data'] = "course:sherobod"
    await call.message.edit_reply_markup(surxondaryo_tuman)



@dp.callback_query_handler(surxon_callback.filter(item_name='shorchi'))
async def toshkenttuman(call:CallbackQuery):
    Shorchi.remove(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][2][3]['text'] = "❌ Sho'rchi"
    surxondaryo_tuman['inline_keyboard'][2][3]['callback_data'] = "course:shroc"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='shroc'))
async def toshkenttuman(call:CallbackQuery):
    Shorchi.add(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][2][3]['text'] = "✅ Sho'rchi"
    surxondaryo_tuman['inline_keyboard'][2][3]['callback_data'] = "course:shorchi"
    await call.message.edit_reply_markup(surxondaryo_tuman)



@dp.callback_query_handler(surxon_callback.filter(item_name='termiz'))
async def toshkenttuman(call:CallbackQuery):
    Termiz.remove(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][3][0]['text'] = "❌ Termiz"
    surxondaryo_tuman['inline_keyboard'][3][0]['callback_data'] = "course:termi"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='termi'))
async def toshkenttuman(call:CallbackQuery):
    Termiz.add(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][3][0]['text'] = "✅ Termiz"
    surxondaryo_tuman['inline_keyboard'][3][0]['callback_data'] = "course:termiz"
    await call.message.edit_reply_markup(surxondaryo_tuman)



@dp.callback_query_handler(surxon_callback.filter(item_name='uzun'))
async def toshkenttuman(call:CallbackQuery):
    Uzun.remove(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][3][1]['text'] = "❌ Uzun"
    surxondaryo_tuman['inline_keyboard'][3][1]['callback_data'] = "course:uzu"
    await call.message.edit_reply_markup(surxondaryo_tuman)

@dp.callback_query_handler(surxon_callback.filter(item_name='uzu'))
async def toshkenttuman(call:CallbackQuery):
    Uzun.add(call.message.chat.id)

    surxondaryo_tuman['inline_keyboard'][3][1]['text'] = "✅ Uzun"
    surxondaryo_tuman['inline_keyboard'][3][1]['callback_data'] = "course:uzun"
    await call.message.edit_reply_markup(surxondaryo_tuman)