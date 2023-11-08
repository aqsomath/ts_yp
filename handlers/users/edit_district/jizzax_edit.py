from loader import dp
from aiogram.types import CallbackQuery
from keyboards.inline.yolovchi.callback_data import  viloyatlar_callback,jizzax_callback
from keyboards.inline.yolovchi.jizztuman import jizzax_tumanlari
Arnasoy={*()}
Baxmal={*()}
Doʻstlik={*()}
Forish={*()}
Gʻallaorol={*()}
SharofRashidov={*()}
Mirzachoʻl={*()}
Paxtakor={*()}
Yangiobod={*()}
Zomin={*()}
Zafarobod={*()}
Zarbdor={*()}
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='zzax'))
async def jizzax_edit(call: CallbackQuery):
    await call.message.answer("Jizzax viloyati tumanlari ", reply_markup=jizzax_tumanlari)
    Arnasoy.add(call.message.chat.id)
    Baxmal.add(call.message.chat.id)
    Doʻstlik.add(call.message.chat.id)
    Forish.add(call.message.chat.id)
    Gʻallaorol.add(call.message.chat.id)
    SharofRashidov.add(call.message.chat.id)
    Mirzachoʻl.add(call.message.chat.id)
    Paxtakor.add(call.message.chat.id)
    Yangiobod.add(call.message.chat.id)
    Zomin.add(call.message.chat.id)
    Zafarobod.add(call.message.chat.id)
    Zarbdor.add(call.message.chat.id)

@dp.callback_query_handler(jizzax_callback.filter(item_name='arnasoy'))
async def chortoq(call: CallbackQuery):
    Arnasoy.remove(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][0][0]['text'] = "❌ Arnasoy"
    jizzax_tumanlari['inline_keyboard'][0][0]['callback_data'] = "course:arna"
    await call.message.edit_reply_markup(jizzax_tumanlari)

@dp.callback_query_handler(jizzax_callback.filter(item_name='arna'))
async def chortoq(call: CallbackQuery):
    Arnasoy.add(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][0][0]['text'] = "✅ Arnasoy"
    jizzax_tumanlari['inline_keyboard'][0][0]['callback_data'] = "course:arnasoy"
    await call.message.edit_reply_markup(jizzax_tumanlari)


@dp.callback_query_handler(jizzax_callback.filter(item_name='baxmal'))
async def chortoq(call: CallbackQuery):
    Baxmal.remove(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][0][1]['text'] = "❌ Baxmal"
    jizzax_tumanlari['inline_keyboard'][0][1]['callback_data'] = "course:baxm"
    await call.message.edit_reply_markup(jizzax_tumanlari)

@dp.callback_query_handler(jizzax_callback.filter(item_name='baxm'))
async def chortoq(call: CallbackQuery):
    Baxmal.add(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][0][1]['text'] = "✅ Baxmal"
    jizzax_tumanlari['inline_keyboard'][0][1]['callback_data'] = "course:baxmal"
    await call.message.edit_reply_markup(jizzax_tumanlari)


@dp.callback_query_handler(jizzax_callback.filter(item_name='dostlik'))
async def chortoq(call: CallbackQuery):
    Doʻstlik.remove(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][0][2]['text'] = "❌ Do'stlik"
    jizzax_tumanlari['inline_keyboard'][0][2]['callback_data'] = "course:dostli"
    await call.message.edit_reply_markup(jizzax_tumanlari)

@dp.callback_query_handler(jizzax_callback.filter(item_name='dostli'))
async def chortoq(call: CallbackQuery):
    Doʻstlik.add(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][0][2]['text'] = "✅ Do'stlik"
    jizzax_tumanlari['inline_keyboard'][0][2]['callback_data'] = "course:dostlik"
    await call.message.edit_reply_markup(jizzax_tumanlari)



@dp.callback_query_handler(jizzax_callback.filter(item_name='forish'))
async def chortoq(call: CallbackQuery):
    Forish.remove(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][0][3]['text'] = "❌ Forish"
    jizzax_tumanlari['inline_keyboard'][0][3]['callback_data'] = "course:forsh"
    await call.message.edit_reply_markup(jizzax_tumanlari)

@dp.callback_query_handler(jizzax_callback.filter(item_name='forsh'))
async def chortoq(call: CallbackQuery):
    Forish.add(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][0][3]['text'] = "✅ Forish"
    jizzax_tumanlari['inline_keyboard'][0][3]['callback_data'] = "course:forish"
    await call.message.edit_reply_markup(jizzax_tumanlari)



@dp.callback_query_handler(jizzax_callback.filter(item_name='gallarol'))
async def chortoq(call: CallbackQuery):
    Gʻallaorol.remove(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][1][0]['text'] = "❌ G'allarol"
    jizzax_tumanlari['inline_keyboard'][1][0]['callback_data'] = "course:galla"
    await call.message.edit_reply_markup(jizzax_tumanlari)

@dp.callback_query_handler(jizzax_callback.filter(item_name='galla'))
async def chortoq(call: CallbackQuery):
    Gʻallaorol.add(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][1][0]['text'] = "✅ G'allarol"
    jizzax_tumanlari['inline_keyboard'][1][0]['callback_data'] = "course:gallarol"
    await call.message.edit_reply_markup(jizzax_tumanlari)


@dp.callback_query_handler(jizzax_callback.filter(item_name='sharof rashidov'))
async def chortoq(call: CallbackQuery):
    SharofRashidov.remove(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][1][1]['text'] = "❌ Sharof Rashidov"
    jizzax_tumanlari['inline_keyboard'][1][1]['callback_data'] = "course:sharo"
    await call.message.edit_reply_markup(jizzax_tumanlari)

@dp.callback_query_handler(jizzax_callback.filter(item_name='sharo'))
async def chortoq(call: CallbackQuery):
    SharofRashidov.add(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][1][1]['text'] = "✅ Sharof rashidov"
    jizzax_tumanlari['inline_keyboard'][1][1]['callback_data'] = "course:sharof Rashidov"
    await call.message.edit_reply_markup(jizzax_tumanlari)


@dp.callback_query_handler(jizzax_callback.filter(item_name='mirzachol'))
async def chortoq(call: CallbackQuery):
    Mirzachoʻl.remove(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][1][2]['text'] = "❌ Mirzacho'l"
    jizzax_tumanlari['inline_keyboard'][1][2]['callback_data'] = "course:mirzacho"
    await call.message.edit_reply_markup(jizzax_tumanlari)


@dp.callback_query_handler(jizzax_callback.filter(item_name='mirzacho'))
async def chortoq(call: CallbackQuery):
    Mirzachoʻl.add(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][1][2]['text'] = "✅ Mirzacho'l"
    jizzax_tumanlari['inline_keyboard'][1][2]['callback_data'] = "course:mirzachol"
    await call.message.edit_reply_markup(jizzax_tumanlari)


@dp.callback_query_handler(jizzax_callback.filter(item_name='paxtakor'))
async def chortoq(call: CallbackQuery):
    Paxtakor.remove(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][1][3]['text'] = "❌ Paxtakor"
    jizzax_tumanlari['inline_keyboard'][1][3]['callback_data'] = "course:paxtako"
    await call.message.edit_reply_markup(jizzax_tumanlari)


@dp.callback_query_handler(jizzax_callback.filter(item_name='paxtako'))
async def chortoq(call: CallbackQuery):
    Paxtakor.add(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][1][3]['text'] = "✅ Paxtakor"
    jizzax_tumanlari['inline_keyboard'][1][3]['callback_data'] = "course:paxtakor"
    await call.message.edit_reply_markup(jizzax_tumanlari)


@dp.callback_query_handler(jizzax_callback.filter(item_name='yangi obod'))
async def chortoq(call: CallbackQuery):
    Yangiobod.remove(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][2][0]['text'] = "❌ Yangi obod"
    jizzax_tumanlari['inline_keyboard'][2][0]['callback_data'] = "course:yango_"
    await call.message.edit_reply_markup(jizzax_tumanlari)


@dp.callback_query_handler(jizzax_callback.filter(item_name='yango_'))
async def chortoq(call: CallbackQuery):
    Yangiobod.add(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][2][0]['text'] = "✅ Yangi obod"
    jizzax_tumanlari['inline_keyboard'][2][0]['callback_data'] = "course:yangi obod"
    await call.message.edit_reply_markup(jizzax_tumanlari)


@dp.callback_query_handler(jizzax_callback.filter(item_name='zomin'))
async def chortoq(call: CallbackQuery):
    Zomin.remove(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][2][1]['text'] = "❌ Zomin"
    jizzax_tumanlari['inline_keyboard'][2][1]['callback_data'] = "course:zooom"
    await call.message.edit_reply_markup(jizzax_tumanlari)


@dp.callback_query_handler(jizzax_callback.filter(item_name='zooom'))
async def chortoq(call: CallbackQuery):
    Zomin.add(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][2][1]['text'] = "✅ Zomin"
    jizzax_tumanlari['inline_keyboard'][2][1]['callback_data'] = "course:zomin"
    await call.message.edit_reply_markup(jizzax_tumanlari)


@dp.callback_query_handler(jizzax_callback.filter(item_name='zafarobod'))
async def chortoq(call: CallbackQuery):
    Zafarobod.remove(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][2][2]['text'] = "❌ Zafarobod"
    jizzax_tumanlari['inline_keyboard'][2][2]['callback_data'] = "course:zafaro"
    await call.message.edit_reply_markup(jizzax_tumanlari)


@dp.callback_query_handler(jizzax_callback.filter(item_name='zafaro'))
async def chortoq(call: CallbackQuery):
    Zafarobod.add(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][2][2]['text'] = "✅ Zafarobod"
    jizzax_tumanlari['inline_keyboard'][2][2]['callback_data'] = "course:zafarobod"
    await call.message.edit_reply_markup(jizzax_tumanlari)


@dp.callback_query_handler(jizzax_callback.filter(item_name='zarbdor'))
async def chortoq(call: CallbackQuery):
    Zarbdor.remove(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][2][3]['text'] = "❌ Zarbdor"
    jizzax_tumanlari['inline_keyboard'][2][3]['callback_data'] = "course:zarbdo"
    await call.message.edit_reply_markup(jizzax_tumanlari)


@dp.callback_query_handler(jizzax_callback.filter(item_name='zarbdo'))
async def chortoq(call: CallbackQuery):
    Zarbdor.add(call.message.chat.id)

    jizzax_tumanlari['inline_keyboard'][2][3]['text'] = "✅ Zarbdor"
    jizzax_tumanlari['inline_keyboard'][2][3]['callback_data'] = "course:zarbdor"
    await call.message.edit_reply_markup(jizzax_tumanlari)