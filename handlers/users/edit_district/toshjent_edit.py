from aiogram.types import CallbackQuery

from keyboards.inline.yolovchi.callback_data import viloyatlar_callback, toshkent_callback
from keyboards.inline.yolovchi.toshtuman import toshkent_viloyati_tumanlari
from loader import dp

Bekobod={*()}
Bostonliq={*()}
Boka={*()}
Chinoz={*()}
Qibray={*()}
Ohangaron={*()}
Oqqorgon={*()}
Parkent={*()}
Piskent={*()}
QuyiChirchiq={*()}
OrtaChirchiq={*()}
Yangiyol={*()}
YuqoriChirchiq={*()}
Zangiota={*()}
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='kentt'))
async def toshkenttuman(call:CallbackQuery):
    await call.message.answer("Toshkent tumanlari", reply_markup=toshkent_viloyati_tumanlari)
    Bekobod.add(call.message.chat.id)
    Bostonliq.add(call.message.chat.id)
    Boka.add(call.message.chat.id)
    Chinoz.add(call.message.chat.id)
    Qibray.add(call.message.chat.id)
    Ohangaron.add(call.message.chat.id)
    Oqqorgon.add(call.message.chat.id)
    Parkent.add(call.message.chat.id)
    Piskent.add(call.message.chat.id)
    QuyiChirchiq.add(call.message.chat.id)
    OrtaChirchiq.add(call.message.chat.id)
    YuqoriChirchiq.add(call.message.chat.id)
    Zangiota.add(call.message.chat.id)

@dp.callback_query_handler(toshkent_callback.filter(item_name='bekobod'))
async def toshkenttuman(call:CallbackQuery):
    Bekobod.remove(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][0][0]['text'] = "❌ Bekobod"
    toshkent_viloyati_tumanlari['inline_keyboard'][0][0]['callback_data'] = "course:beko"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)

@dp.callback_query_handler(toshkent_callback.filter(item_name='beko'))
async def toshkenttuman(call:CallbackQuery):
    Bekobod.add(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][0][0]['text'] = "✅ Bekobod"
    toshkent_viloyati_tumanlari['inline_keyboard'][0][0]['callback_data'] = "course:bekobod"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)


@dp.callback_query_handler(toshkent_callback.filter(item_name='bostonliq'))
async def toshkenttuman(call:CallbackQuery):
    Bostonliq.remove(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][0][1]['text'] = "❌ Bo'stonliq"
    toshkent_viloyati_tumanlari['inline_keyboard'][0][1]['callback_data'] = "course:bost"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)

@dp.callback_query_handler(toshkent_callback.filter(item_name='bost'))
async def toshkenttuman(call:CallbackQuery):
    Bostonliq.add(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][0][1]['text'] = "✅ Bo'stonliq"
    toshkent_viloyati_tumanlari['inline_keyboard'][0][1]['callback_data'] = "course:bostonliq"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)


@dp.callback_query_handler(toshkent_callback.filter(item_name='boka'))
async def toshkenttuman(call:CallbackQuery):
    Boka.remove(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][0][2]['text'] = "❌ Bo'ka"
    toshkent_viloyati_tumanlari['inline_keyboard'][0][2]['callback_data'] = "course:bok"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)

@dp.callback_query_handler(toshkent_callback.filter(item_name='bok'))
async def toshkenttuman(call:CallbackQuery):
    Boka.add(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][0][2]['text'] = "✅ Bo'ka"
    toshkent_viloyati_tumanlari['inline_keyboard'][0][2]['callback_data'] = "course:boka"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)


@dp.callback_query_handler(toshkent_callback.filter(item_name='chinoz'))
async def toshkenttuman(call:CallbackQuery):
    Chinoz.remove(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][0][3]['text'] = "❌Chinoz"
    toshkent_viloyati_tumanlari['inline_keyboard'][0][3]['callback_data'] = "course:chin"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)

@dp.callback_query_handler(toshkent_callback.filter(item_name='chin'))
async def toshkenttuman(call:CallbackQuery):
    Chinoz.add(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][0][3]['text'] = "✅ Chinoz"
    toshkent_viloyati_tumanlari['inline_keyboard'][0][3]['callback_data'] = "course:chinoz"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)


@dp.callback_query_handler(toshkent_callback.filter(item_name='qibray'))
async def toshkenttuman(call:CallbackQuery):
    Qibray.remove(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][1][0]['text'] = "❌Qibray"
    toshkent_viloyati_tumanlari['inline_keyboard'][1][0]['callback_data'] = "course:qizr"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)

@dp.callback_query_handler(toshkent_callback.filter(item_name='qizr'))
async def toshkenttuman(call:CallbackQuery):
    Qibray.add(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][1][0]['text'] = "✅ Qibray"
    toshkent_viloyati_tumanlari['inline_keyboard'][1][0]['callback_data'] = "course:qibray"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)


@dp.callback_query_handler(toshkent_callback.filter(item_name='ohangaron'))
async def toshkenttuman(call:CallbackQuery):
    Ohangaron.remove(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][1][1]['text'] = "❌Ohangaron"
    toshkent_viloyati_tumanlari['inline_keyboard'][1][1]['callback_data'] = "course:ohang"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)

@dp.callback_query_handler(toshkent_callback.filter(item_name='ohang'))
async def toshkenttuman(call:CallbackQuery):
    Ohangaron.add(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][1][1]['text'] = "✅ Ohangaron"
    toshkent_viloyati_tumanlari['inline_keyboard'][1][1]['callback_data'] = "course:ohangaron"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)


@dp.callback_query_handler(toshkent_callback.filter(item_name='oqqorgon'))
async def toshkenttuman(call:CallbackQuery):
    Oqqorgon.remove(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][1][2]['text'] = "❌Oqqo'rg'on"
    toshkent_viloyati_tumanlari['inline_keyboard'][1][2]['callback_data'] = "course:oqq"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)

@dp.callback_query_handler(toshkent_callback.filter(item_name='oqq'))
async def toshkenttuman(call:CallbackQuery):
    Oqqorgon.add(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][1][2]['text'] = "✅ Oqq'rg'on"
    toshkent_viloyati_tumanlari['inline_keyboard'][1][2]['callback_data'] = "course:oqqorgon"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)


@dp.callback_query_handler(toshkent_callback.filter(item_name='parkent'))
async def toshkenttuman(call:CallbackQuery):
    Parkent.remove(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][1][3]['text'] = "❌Parkent"
    toshkent_viloyati_tumanlari['inline_keyboard'][1][3]['callback_data'] = "course:park"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)

@dp.callback_query_handler(toshkent_callback.filter(item_name='park'))
async def toshkenttuman(call:CallbackQuery):
    Parkent.add(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][1][3]['text'] = "✅ Parkent"
    toshkent_viloyati_tumanlari['inline_keyboard'][1][3]['callback_data'] = "course:parkent"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)


@dp.callback_query_handler(toshkent_callback.filter(item_name='piskent'))
async def toshkenttuman(call:CallbackQuery):
    Piskent.remove(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][2][0]['text'] = "❌ Piskent"
    toshkent_viloyati_tumanlari['inline_keyboard'][2][0]['callback_data'] = "course:piske"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)

@dp.callback_query_handler(toshkent_callback.filter(item_name='piske'))
async def toshkenttuman(call:CallbackQuery):
    Piskent.add(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][2][0]['text'] = "✅ Piskent"
    toshkent_viloyati_tumanlari['inline_keyboard'][2][0]['callback_data'] = "course:piskent"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)


@dp.callback_query_handler(toshkent_callback.filter(item_name='quyichirchiq'))
async def toshkenttuman(call:CallbackQuery):
    QuyiChirchiq.remove(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][2][1]['text'] = "❌ Quyichirchiq"
    toshkent_viloyati_tumanlari['inline_keyboard'][2][1]['callback_data'] = "course:quyi"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)

@dp.callback_query_handler(toshkent_callback.filter(item_name='quyi'))
async def toshkenttuman(call:CallbackQuery):
    QuyiChirchiq.add(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][2][1]['text'] = "✅ Quyichirchiq"
    toshkent_viloyati_tumanlari['inline_keyboard'][2][1]['callback_data'] = "course:quyichirchiq"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)


@dp.callback_query_handler(toshkent_callback.filter(item_name='ortachirchiq'))
async def toshkenttuman(call:CallbackQuery):
    OrtaChirchiq.remove(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][2][2]['text'] = "❌ O'rtachirchiq"
    toshkent_viloyati_tumanlari['inline_keyboard'][2][2]['callback_data'] = "course:ortchiq"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)

@dp.callback_query_handler(toshkent_callback.filter(item_name='ortchiq'))
async def toshkenttuman(call:CallbackQuery):
    OrtaChirchiq.add(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][2][2]['text'] = "✅ O'rtachirchiq"
    toshkent_viloyati_tumanlari['inline_keyboard'][2][2]['callback_data'] = "course:ortachirchiq"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)


@dp.callback_query_handler(toshkent_callback.filter(item_name='yangiyol'))
async def toshkenttuman(call:CallbackQuery):
    Yangiyol.remove(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][2][3]['text'] = "❌ Yangiyo'l"
    toshkent_viloyati_tumanlari['inline_keyboard'][2][3]['callback_data'] = "course:yangyol"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)

@dp.callback_query_handler(toshkent_callback.filter(item_name='yangyol'))
async def toshkenttuman(call:CallbackQuery):
    Yangiyol.add(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][2][3]['text'] = "✅ Yangiyo'l"
    toshkent_viloyati_tumanlari['inline_keyboard'][2][3]['callback_data'] = "course:yangiyol"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)


@dp.callback_query_handler(toshkent_callback.filter(item_name='yuqorichirchiq'))
async def toshkenttuman(call:CallbackQuery):
    OrtaChirchiq.remove(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][3][0]['text'] = "❌ Yuqori chirchiq"
    toshkent_viloyati_tumanlari['inline_keyboard'][3][0]['callback_data'] = "course:chirch"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)

@dp.callback_query_handler(toshkent_callback.filter(item_name='chirch'))
async def toshkenttuman(call:CallbackQuery):
    OrtaChirchiq.add(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][3][0]['text'] = "✅ Yuqori chirchiq"
    toshkent_viloyati_tumanlari['inline_keyboard'][3][0]['callback_data'] = "course:yuqorichirchiq"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)


@dp.callback_query_handler(toshkent_callback.filter(item_name='zangiota'))
async def toshkenttuman(call:CallbackQuery):
    Zangiota.remove(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][3][1]['text'] = "❌ Zangiota"
    toshkent_viloyati_tumanlari['inline_keyboard'][3][1]['callback_data'] = "course:zangi"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)

@dp.callback_query_handler(toshkent_callback.filter(item_name='zangi'))
async def toshkenttuman(call:CallbackQuery):
    Zangiota.add(call.message.chat.id)

    toshkent_viloyati_tumanlari['inline_keyboard'][3][1]['text'] = "✅ Zangiota"
    toshkent_viloyati_tumanlari['inline_keyboard'][3][1]['callback_data'] = "course:zangiota"
    await call.message.edit_reply_markup(toshkent_viloyati_tumanlari)




