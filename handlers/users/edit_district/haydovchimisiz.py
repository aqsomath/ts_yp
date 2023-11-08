from aiogram.types import CallbackQuery

from keyboards.inline.yolovchi.andtuman import andijon_old
from keyboards.inline.yolovchi.callback_data import kirish_callback, viloyatlar_callback, andijon_callback
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp
Andijon = {*()}
Ulugnor ={*()}
Andijonshaxar ={*()}
Asaka ={*()}
Baliqchi ={*()}
Boston ={*()}
Buloqboshi ={*()}
Izboskan ={*()}
Jalaquduq ={*()}
Xojabod ={*()}
Qorgontepa ={*()}
Marhamat ={*()}
Oltinkol ={*()}
Paxtabod ={*()}
Shaxrixon ={*()}
Xonabod ={*()}
@dp.callback_query_handler(kirish_callback.filter(item_name='haydovchi'))
async def haydovchi(call:CallbackQuery):

    await call.message.answer("Salom haydovchi\nSiz qaysi viloyat haydovchisisiz ?", reply_markup=viloyatlar)
#
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='jonn'))
async def andijontuman(call:CallbackQuery):
    Andijon.add(call.message.chat.id)
    Ulugnor.add(call.message.chat.id)
    Jalaquduq.add(call.message.chat.id)
    Xonabod.add(call.message.chat.id)
    Paxtabod.add(call.message.chat.id)
    Oltinkol.add(call.message.chat.id)
    Baliqchi.add(call.message.chat.id)
    Buloqboshi.add(call.message.chat.id)
    Shaxrixon.add(call.message.chat.id)
    Andijonshaxar.add(call.message.chat.id)
    Xojabod.add(call.message.chat.id)
    Qorgontepa.add(call.message.chat.id)
    Marhamat.add(call.message.chat.id)
    Boston.add(call.message.chat.id)
    Asaka.add(call.message.chat.id)
    Izboskan.add(call.message.chat.id)
    await call.message.answer("Andijon tumanlari", reply_markup=andijon_old)
@dp.callback_query_handler(andijon_callback.filter(item_name='ulugnor'))
async def edit(call:CallbackQuery):
    Ulugnor.remove(call.message.chat.id)
    andijon_old['inline_keyboard'][0][0]['text'] = "❌ Ulug'nor"
    andijon_old['inline_keyboard'][0][0]['callback_data'] = "course:ulug"
    await call.message.edit_reply_markup(andijon_old)
@dp.callback_query_handler(andijon_callback.filter(item_name='ulug'))
async def edit(call:CallbackQuery):
    Ulugnor.add(call.message.chat.id)
    andijon_old['inline_keyboard'][0][0]['text'] = "✅ Ulug'nor"
    andijon_old['inline_keyboard'][0][0]['callback_data'] = "course:ulugnor"
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='shaxar'))
async def edit(call:CallbackQuery):
    Andijonshaxar.remove(call.message.chat.id)

    andijon_old['inline_keyboard'][0][1]['text'] = "❌ Andijon shahar"
    andijon_old['inline_keyboard'][0][1]['callback_data'] = "course:shahar"

    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='shahar'))
async def edit(call:CallbackQuery):
    Andijonshaxar.add(call.message.chat.id)
    andijon_old['inline_keyboard'][0][1]['text'] = "✅ Andijon shahar"
    andijon_old['inline_keyboard'][0][1]['callback_data'] = "course:shaxar"
    await call.message.edit_reply_markup(andijon_old)


@dp.callback_query_handler(andijon_callback.filter(item_name='asaka'))
async def edit(call:CallbackQuery):
    Asaka.remove(call.message.chat.id)
    andijon_old['inline_keyboard'][0][2]['text'] = "❌ Asaka"
    andijon_old['inline_keyboard'][0][2]['callback_data'] = "course:asak"

    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='asak'))
async def edit(call:CallbackQuery):
    Asaka.add(call.message.chat.id)
    andijon_old['inline_keyboard'][0][2]['text'] = "✅ Asaka"
    andijon_old['inline_keyboard'][0][2]['callback_data'] = "course:asaka"
    await call.message.edit_reply_markup(andijon_old)


@dp.callback_query_handler(andijon_callback.filter(item_name='baliqchi'))
async def edit(call:CallbackQuery):
    Baliqchi.remove(call.message.chat.id)
    andijon_old['inline_keyboard'][1][0]['text'] = "❌ Baliqchi"
    andijon_old['inline_keyboard'][1][0]['callback_data'] = "course:baliq"
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='baliq'))
async def edit(call:CallbackQuery):
    Baliqchi.add(call.message.chat.id)
    andijon_old['inline_keyboard'][1][0]['text'] = "✅ Baliqchi"
    andijon_old['inline_keyboard'][1][0]['callback_data'] = "course:baliqchi"
    await call.message.edit_reply_markup(andijon_old)


@dp.callback_query_handler(andijon_callback.filter(item_name='boz'))
async def edit(call:CallbackQuery):
    Boston.remove(call.message.chat.id)
    andijon_old['inline_keyboard'][1][1]['text'] = "❌ Bo'ston"
    andijon_old['inline_keyboard'][1][1]['callback_data'] = "course:boston"

    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='boston'))
async def edit(call:CallbackQuery):
    Boston.add(call.message.chat.id)
    andijon_old['inline_keyboard'][1][1]['text'] = "✅ Bo'ston"
    andijon_old['inline_keyboard'][1][1]['callback_data'] = "course:boz"
    await call.message.edit_reply_markup(andijon_old)



@dp.callback_query_handler(andijon_callback.filter(item_name='buloqboshi'))
async def edit(call:CallbackQuery):
    Buloqboshi.remove(call.message.chat.id)
    andijon_old['inline_keyboard'][1][2]['text'] = "❌ Buloqboshi"
    andijon_old['inline_keyboard'][1][2]['callback_data'] = "course:buloq"

    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='buloq'))
async def edit(call:CallbackQuery):
    Buloqboshi.add(call.message.chat.id)
    andijon_old['inline_keyboard'][1][2]['text'] = "✅ Buloqboshi"
    andijon_old['inline_keyboard'][1][2]['callback_data'] = "course:buloqboshi"
    await call.message.edit_reply_markup(andijon_old)


@dp.callback_query_handler(andijon_callback.filter(item_name='izboskan'))
async def edit(call:CallbackQuery):
    Izboskan.remove(call.message.chat.id)

    andijon_old['inline_keyboard'][2][0]['text'] = "❌ Izboskan"
    andijon_old['inline_keyboard'][2][0]['callback_data'] = "course:izbos"

    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='izbos'))
async def edit(call:CallbackQuery):
    Izboskan.add(call.message.chat.id)

    andijon_old['inline_keyboard'][2][0]['text'] = "✅ Izboskan"
    andijon_old['inline_keyboard'][2][0]['callback_data'] = "course:izboskan"
    await call.message.edit_reply_markup(andijon_old)


@dp.callback_query_handler(andijon_callback.filter(item_name='jalaquduq'))
async def edit(call:CallbackQuery):
    Jalaquduq.remove(call.message.chat.id)

    andijon_old['inline_keyboard'][2][1]['text'] = "❌ Jalaquduq"
    andijon_old['inline_keyboard'][2][1]['callback_data'] = "course:jala"

    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='jala'))
async def edit(call:CallbackQuery):
    Jalaquduq.add(call.message.chat.id)

    andijon_old['inline_keyboard'][2][1]['text'] = "✅ Jalaquduq"
    andijon_old['inline_keyboard'][2][1]['callback_data'] = "course:jalaquduq"
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='xojabod'))
async def edit(call:CallbackQuery):
    Xojabod.remove(call.message.chat.id)

    andijon_old['inline_keyboard'][2][2]['text'] = "❌ Xo'jabod"
    andijon_old['inline_keyboard'][2][2]['callback_data'] = "course:xoja"

    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='xoja'))
async def edit(call:CallbackQuery):
    Xojabod.add(call.message.chat.id)

    andijon_old['inline_keyboard'][2][2]['text'] = "✅ Xo'jabod"
    andijon_old['inline_keyboard'][2][2]['callback_data'] = "course:xojabod"
    await call.message.edit_reply_markup(andijon_old)



@dp.callback_query_handler(andijon_callback.filter(item_name='qorgontepa'))
async def edit(call:CallbackQuery):
    Qorgontepa.remove(call.message.chat.id)

    andijon_old['inline_keyboard'][3][0]['text'] = "❌ Qo'rg'ontepa"
    andijon_old['inline_keyboard'][3][0]['callback_data'] = "course:qorgon"

    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='qorgon'))
async def edit(call:CallbackQuery):
    Qorgontepa.add(call.message.chat.id)

    andijon_old['inline_keyboard'][3][0]['text'] = "✅ Qo'rg'ontepa"
    andijon_old['inline_keyboard'][3][0]['callback_data'] = "course:qorgontepa"
    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='marhamat'))
async def edit(call:CallbackQuery):
    Marhamat.remove(call.message.chat.id)

    andijon_old['inline_keyboard'][3][1]['text'] = "❌ Marhamat"
    andijon_old['inline_keyboard'][3][1]['callback_data'] = "course:marham"

    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='marham'))
async def edit(call:CallbackQuery):
    Marhamat.add(call.message.chat.id)

    andijon_old['inline_keyboard'][3][1]['text'] = "✅ Marhamat"
    andijon_old['inline_keyboard'][3][1]['callback_data'] = "course:marhamat"
    await call.message.edit_reply_markup(andijon_old)


@dp.callback_query_handler(andijon_callback.filter(item_name='oltinkol'))
async def edit(call:CallbackQuery):
    Oltinkol.remove(call.message.chat.id)

    andijon_old['inline_keyboard'][3][2]['text'] = "❌ Oltinko'l"
    andijon_old['inline_keyboard'][3][2]['callback_data'] = "course:oltin"

    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='oltin'))
async def edit(call:CallbackQuery):
    Oltinkol.add(call.message.chat.id)

    andijon_old['inline_keyboard'][3][2]['text'] = "✅ Oltinko'l"
    andijon_old['inline_keyboard'][3][2]['callback_data'] = "course:oltinkol"
    await call.message.edit_reply_markup(andijon_old)


@dp.callback_query_handler(andijon_callback.filter(item_name='paxtaobod'))
async def edit(call:CallbackQuery):
    Paxtabod.remove(call.message.chat.id)

    andijon_old['inline_keyboard'][4][0]['text'] = "❌ Paxtaobod"
    andijon_old['inline_keyboard'][4][0]['callback_data'] = "course:paxta"

    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='paxta'))
async def edit(call:CallbackQuery):
    Paxtabod.add(call.message.chat.id)

    andijon_old['inline_keyboard'][4][0]['text'] = "✅ Paxtaobod"
    andijon_old['inline_keyboard'][4][0]['callback_data'] = "course:paxtaobod"
    await call.message.edit_reply_markup(andijon_old)



@dp.callback_query_handler(andijon_callback.filter(item_name='shaxrixon'))
async def edit(call:CallbackQuery):
    Shaxrixon.remove(call.message.chat.id)

    andijon_old['inline_keyboard'][4][1]['text'] = "❌ Shaxrixon"
    andijon_old['inline_keyboard'][4][1]['callback_data'] = "course:shaxri"

    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='shaxri'))
async def edit(call:CallbackQuery):
    Shaxrixon.add(call.message.chat.id)
    andijon_old['inline_keyboard'][4][1]['text'] = "✅ Shaxrixon"
    andijon_old['inline_keyboard'][4][1]['callback_data'] = "course:shaxrixon"
    await call.message.edit_reply_markup(andijon_old)



@dp.callback_query_handler(andijon_callback.filter(item_name='xonabod'))
async def edit(call:CallbackQuery):
    Xonabod.remove(call.message.chat.id)
    andijon_old['inline_keyboard'][4][2]['text'] = "❌ Xonabod"
    andijon_old['inline_keyboard'][4][2]['callback_data'] = "course:xona"

    await call.message.edit_reply_markup(andijon_old)

@dp.callback_query_handler(andijon_callback.filter(item_name='xona'))
async def edit(call:CallbackQuery):
    Xonabod.add(call.message.chat.id)
    andijon_old['inline_keyboard'][4][2]['text'] = "✅ Xonabod"
    andijon_old['inline_keyboard'][4][2]['callback_data'] = "course:xonabod"
    await call.message.edit_reply_markup(andijon_old)