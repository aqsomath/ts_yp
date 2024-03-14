from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery,  InlineKeyboardMarkup, InlineKeyboardButton
import aiogram
from keyboards.inline.yolovchi.kirish import  umumiy_menu_1
from loader import dp, db, bot
from states.haydovchi_pochta_states import Reys_pochta_andijon


@dp.callback_query_handler(state=Reys_pochta_andijon.qoshimcha_tuman)
async def qoshimcha_tuman(call: CallbackQuery, state: FSMContext):

    if call.data == "boshmenu":
            await call.message.answer("Ma'lumotlarni tog'rilab qaytadan kiriting", reply_markup=umumiy_menu_1)
            await call.message.delete()
            await state.finish()
    if call.data == "qaytish":
        viloyat = {
            "Andijon": "andijon",
            "Namangan": "namangan",
            "Farg'ona": "farg'ona",
            "Buxoro": "buxoro",
            "Toshkent": "toshkent",
            "Sirdaryo": "sirdaryo",
            "Surxondaryo": "surxondaryo",
            "Qashqadaryo": "qashqadaryo",
            "Xorazm": "xorazm",
            "Navoiy": "navoiy",
            "Jizzax": "jizzax",
            "Samarqand": "samarqand",
            "Qoraqalpog'iston": "qoraqalpoq",
            "Keyingisi": "Olinmaydi",
            "Tanlab bo'ldim": "tanladim",
            "Ortga": "ortga",
            "Bosh menu": "boshmenu",
        }

        viloyatlar_yol = InlineKeyboardMarkup(row_width=3)
        for key, value in viloyat.items():
            viloyatlar_yol.insert(InlineKeyboardButton(text=key, callback_data=value))
        await call.message.answer("Qo'shimcha qaysi viloyatlarning qaysi tumaniga borasiz ? ",
                                  reply_markup=viloyatlar_yol)
        await Reys_pochta_andijon.odam_vil.set()
        await call.message.delete()
    list_1 = []
    jami = await db.select_all_qoshimcha_tumanlar()
    for i in jami:
        if i[2] == call.from_user.id:
            list_1.append(i[1])
    if call.data in list_1:
        await db.delete_qoshimcha_tumanlar(telegram_id=call.from_user.id, tuman=call.data)
    else:
        await db.add_qoshimcha_tumanlar(telegram_id=call.from_user.id, tuman=call.data)
    jamii = await db.select_all_qoshimcha_tumanlar()
    list = []
    for i in jamii:
        if i[2] == call.from_user.id:
            list.append(i[1])
            if "qaytish" in list:
                list.remove("qaytish")
            if "tanladim" in list:
                list.remove("tanladim")
    await state.update_data({"qoshimcha_tumanlar": list})
    buxoro = {}
    if "buxoro shaxar" in list:
        buxoro["✅Buxoro shahar"] = "buxoro shaxar"
    else:
        buxoro["Buxoro shahar"] = "buxoro shaxar"
    if "Buxoro tuman" in list:
        buxoro["✅Buxoro tuman"] = "Buxoro tuman"
    else:
        buxoro["Buxoro tuman"] = "Buxoro tuman"
    if "olot" in list:
        buxoro["✅Olot"] = "olot"
    else:
        buxoro["Olot"] = "olot"
    if "g'ijduvon" in list:
        buxoro["✅Gʻijduvon"] = "g'ijduvon"
    else:
        buxoro["Gʻijduvon"] = "g'ijduvon"
    if "jondor" in list:
        buxoro["✅Jondor"] = 'jondor'
    else:
        buxoro["Jondor"] = 'jondor'
    if "kogon shahar" in list:
        buxoro["✅Kogon shahar"] = 'kogon shahar'
    else:
        buxoro["Kogon shahar"] = 'kogon shahar'
    if "kogon" in list:
        buxoro["✅Kogon tuman"] = 'kogon tuman'
    else:
        buxoro["Kogon tuman"] = 'kogon tuman'
    if "qorako'l" in list:
        buxoro["✅Qorakoʻl"] = "qorako'l"
    else:
        buxoro["Qorakoʻl"] = 'qorako\'l'
    if "qorovulbozor" in list:
        buxoro["✅Qorovulbozor"] = "qorovulbozor"
    else:
        buxoro["Qorovulbozor"] = 'qorovulbozor'
    if "peshku" in list:
        buxoro["✅Peshku"] = "peshku"
    else:
        buxoro["Peshku"] = "peshku"
    if "romitan" in list:
        buxoro["✅Romitan"] = "romitan"
    else:
        buxoro["Romitan"] = 'romitan'
    if "shofirkon" in list:
        buxoro["✅Shofirkon"] = "shofirkon"
    else:
        buxoro["Shofirkon"] = "shofirkon"
    if "vobkent" in list:
        buxoro["✅Vobkent"] = "vobkent"
    else:
        buxoro["Vobkent"] = "vobkent"
    shaxsiy_buxoro = InlineKeyboardMarkup(row_width=3)
    for key, value in buxoro.items():
        shaxsiy_buxoro.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_buxoro.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
    shaxsiy_buxoro.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_buxoro.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))

    shaxsiy_fargona = str(call.from_user.id)
    fargona = {}
    if "fergana city" in list:
        fargona["✅Fargʻona shahri"] = "fergana city"
    else:
        fargona["Fargʻona shahri"] = 'fergana city'
    if "fergana" in list:
        fargona["✅Fargʻona tuman"] = "fergana"
    else:
        fargona["Fargʻona tuman"] = 'fergana'
    if "oltiariq" in list:
        fargona["✅Oltiariq"] = "oltiariq"
    else:
        fargona["Oltiariq"] = "oltiariq"
    if "bog'dod" in list:
        fargona["✅Bagʻdod"] = "bog'dod"
    else:
        fargona["Bagʻdod"] = "bog'dod"
    if "beshariq" in list:
        fargona["✅Beshariq"] = "beshariq"
    else:
        fargona["Beshariq"] = "beshariq"
    if "buvayda" in list:
        fargona["✅Buvayda"] = 'buvayda'
    else:
        fargona["Buvayda"] = 'buvayda'
    if "dangara" in list:
        fargona["✅Dangʻara"] = 'dangara'
    else:
        fargona["Dangʻara"] = 'dangara'
    if "furqat" in list:
        fargona["✅Furqat"] = "furqat"
    else:
        fargona["Furqat"] = 'furqat'
    if "qo'shtepa" in list:
        fargona["✅Qoʻshtepa"] = "qo'shtepa"
    else:
        fargona["Qoʻshtepa"] = "qo'shtepa"
    if "quva" in list:
        fargona["✅Quva"] = "quva"
    else:
        fargona["Quva"] = 'quva'
    if "rishton" in list:
        fargona["✅Rishton"] = "rishton"
    else:
        fargona["Rishton"] = "rishton"
    if "sox" in list:
        fargona["✅Soʻx"] = "sox"
    else:
        fargona["Soʻx"] = "sox"
    if "toshloq" in list:
        fargona["✅Toshloq"] = "toshloq"
    else:
        fargona["Toshloq"] = "toshloq"
    if "o'zbekiston" in list:
        fargona["✅Oʻzbekiston"] = "o'zbekiston"
    else:
        fargona["Oʻzbekiston"] = "o'zbekiston"
    if "uchko'prik" in list:
        fargona["✅Uchkoʻprik"] = "uchko'prik"
    else:
        fargona["Uchkoʻprik"] = "uchko'prik"
    if "yozyovon" in list:
        fargona["✅Yozyovon"] = "yozyovon"
    else:
        fargona["Yozyovon"] = "yozyovon"
    if "quvasoy shahri" in list:
        fargona["✅Quvasoy shahri"] = "quvasoy shahri"
    else:
        fargona["Quvasoy shahri"] = "quvasoy shahri"
    if "margilon shahri" in list:
        fargona["✅Marg'ilon shahri"] = "margilon shahri"
    else:
        fargona["Marg'ilon shahri"] = "margilon shahri"
    if "qoqon" in list:
        fargona["✅Qo'qon shahri"] = "qoqon"
    else:
        fargona["Qo'qon shahri"] = "qoqon"
    shaxsiy_fargona = InlineKeyboardMarkup(row_width=3)
    for key, value in fargona.items():
        shaxsiy_fargona.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_fargona.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
    shaxsiy_fargona.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_fargona.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))

    shaxsiy_andijon = str(call.from_user.id)
    andijon = {}
    if "andijon shaxar" in list:
        andijon["✅Andijon shaxar"] = 'andijon shaxar'
    else:
        andijon["Andijon shaxar"] = 'andijon shaxar'
    if "Andijon" in list:
        andijon["✅Andijon tuman"] = "Andijon"
    else:
        andijon["Andijon tuman"] = 'Andijon'
    if "ulug'nor" in list:
        andijon["✅Ulug'nor"] = "ulug'nor"
    else:
        andijon["Ulug'nor"] = "ulug'nor"
    if "asaka" in list:
        andijon["✅Asaka"] = "asaka"
    else:
        andijon["Asaka"] = "asaka"
    if "paxtaobod" in list:

        andijon["✅Paxtaobod"] = 'paxtaobod'
    else:
        andijon["Paxtaobod"] = 'paxtaobod'
    if "shaxrixon" in list:

        andijon["✅Shaxrixon"] = 'shaxrixon'
    else:
        andijon["Shaxrixon"] = 'shaxrixon'
    if "marhamat" in list:

        andijon["✅Marhamat"] = "marhamat"
    else:
        andijon["Marhamat"] = 'marhamat'
    if "xonabod shahar" in list:
        andijon["✅Xonabod shahar"] = "xonabod shahar"
    else:
        andijon["Xonabod shahar"] = 'xonabod shahar'
    if "xonabod" in list:
        andijon["✅Xonabod"] = "xonabod"
    else:
        andijon["Xonabod"] = 'xonabod'
    if "oltinko'l" in list:

        andijon["✅Oltinko'l"] = "oltinko'l"
    else:
        andijon["Oltinko'l"] = "oltinko'l"
    if "baliqchi" in list:

        andijon["✅Baliqchi"] = "baliqchi"
    else:
        andijon["Baliqchi"] = 'baliqchi'
    if "bo'ston" in list:

        andijon["✅Bo'ston"] = "bo'ston"
    else:
        andijon["Bo'ston"] = "bo'ston"
    if "buloqboshi" in list:

        andijon["✅Buloqboshi"] = "buloqboshi"
    else:
        andijon["Buloqboshi"] = "buloqboshi"
    if "izboskan" in list:

        andijon["✅Izboskan"] = "izboskan"
    else:
        andijon["Izboskan"] = "izboskan"
    if "jalaquduq" in list:

        andijon["✅Jalaquduq"] = "jalaquduq"
    else:
        andijon["Jalaquduq"] = "jalaquduq"
    if "xo'jabod" in list:

        andijon["✅Xo'jabod"] = "xo'jabod"
    else:
        andijon["Xo'jabod"] = "xo'jabod"
    if "qo'rg'ontepa" in list:

        andijon["✅Qo'rg'ontepa"] = "qo'rg'ontepa"
    else:
        andijon["Qo'rg'ontepa"] = "qo'rg'ontepa"
    shaxsiy_tugma = InlineKeyboardMarkup(row_width=3)
    for key, value in andijon.items():
        shaxsiy_tugma.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_tugma.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
    shaxsiy_tugma.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_tugma.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))

    namangan = {}
    if "namangan shaxar" in list:
        namangan["✅Namangan shaxar"] = 'namangan shaxar'
    else:
        namangan["Namangan shaxar"] = 'namangan shaxar'
    if "namangan tuman" in list:
        namangan["✅Namangan tuman"] = 'namangan tuman'
    else:
        namangan["Namangan tuman"] = 'namangan tuman'
    if "chortoq" in list:
        namangan["✅Chortoq"] = "chortoq"
    else:
        namangan["Chortoq"] = "chortoq"
    if "chust" in list:
        namangan["✅Chust"] = 'chust'
    else:
        namangan["Chust"] = 'chust'
    if "kosonsoy" in list:
        namangan["✅Kosonsoy"] = "kosonsoy"
    else:
        namangan["Kosonsoy"] = "kosonsoy"
    if "mingbuloq" in list:
        namangan["✅Mingbuloq"] = 'mingbuloq'
    else:
        namangan["Mingbuloq"] = 'mingbuloq'
    if "norin" in list:
        namangan["✅Norin"] = "norin"
    else:
        namangan["Norin"] = 'norin'
    if "pop" in list:
        namangan["✅Pop"] = "pop"
    else:
        namangan["Pop"] = 'pop'
    if "toraqorgon" in list:
        namangan["✅To'raqo'rg'on"] = "toraqorgon"
    else:
        namangan["To'raqo'rg'on"] = "toraqorgon"
    if "uchqorgon" in list:
        namangan["✅Uchqo'rg'on"] = "uchqorgon"
    else:
        namangan["Uchqo'rg'on"] = 'uchqorgon'
    if "uychi" in list:
        namangan["✅Uychi"] = "uychi"
    else:
        namangan["Uychi"] = "uychi"
    if "yangi qorgon" in list:
        namangan["✅Yangiqo'rg'on"] = "yangi qorgon"
    else:
        namangan["Yangiqo'rg'on"] = "yangi qorgon"
    if "yangi namangan" in list:
        namangan["✅Yangi Namangan"] = "yangi namangan"
    else:
        namangan["Yangi Namangan"] = "yangi namangan"
    shaxsiy_namangan = InlineKeyboardMarkup(row_width=3)
    for key, value in namangan.items():
        shaxsiy_namangan.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_namangan.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
    shaxsiy_namangan.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_namangan.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))

    toshkent = {}
    if "Toshkent shahar" in list:
        toshkent["✅Toshkent shahar"] = "Toshkent shahar"
    else:
        toshkent["Toshkent shahar"] = "Toshkent shahar"
    if "Bektemir" in list:
        toshkent["✅Bektemir tumani"] = "Bektemir"
    else:
        toshkent["Bektemir tumani"] = "Bektemir"
    if "Mirzo Ulug‘bek tumani" in list:
        toshkent["✅Mirzo Ulug‘bek tumani"] = "Mirzo Ulug‘bek tumani"
    else:
        toshkent["Mirzo Ulug‘bek tumani"] = "Mirzo Ulug‘bek tumani"
    if "Mirobod tumani" in list:
        toshkent["✅Mirobod tumani"] = "Mirobod tumani"
    else:
        toshkent["Mirobod tumani"] = "Mirobod tumani"
    if "Olmazor tumani" in list:
        toshkent["✅Olmazor tumani"] = 'Olmazor tumani'
    else:
        toshkent["Olmazor tumani"] = 'Olmazor tumani'
    if "Sirg‘ali tumani" in list:
        toshkent["✅Sirg‘ali tumani"] = 'Sirg‘ali tumani'
    else:
        toshkent["Sirg‘ali tumani"] = 'Sirg‘ali tumani'
    if "Uchtepa tumani" in list:
        toshkent["✅Uchtepa tumani"] = "Uchtepa tumani"
    else:
        toshkent["Uchtepa tumani"] = "Uchtepa tumani"
    if "Chilonzor tumani" in list:
        toshkent["✅Chilonzor tumani"] = "Chilonzor tumani"
    else:
        toshkent["Chilonzor tumani"] = 'Chilonzor tumani'
    if "Shayxontohur tumani" in list:
        toshkent["✅Shayxontohur tumani"] = "Shayxontohur tumani"
    else:
        toshkent["Shayxontohur tumani"] = "Shayxontohur tumani"
    if "Yunusobod tumani" in list:
        toshkent["✅Yunusobod tumani"] = "Yunusobod tumani"
    else:
        toshkent["Yunusobod tumani"] = 'Yunusobod tumani'
    if "Yakkasaroy tumani" in list:
        toshkent["✅Yakkasaroy tumani"] = "Yakkasaroy tumani"
    else:
        toshkent["Yakkasaroy tumani"] = "Yakkasaroy tumani"
    if "Yashnobod tumani" in list:
        toshkent["✅Yashnobod tumani"] = "Yashnobod tumani"
    else:
        toshkent["Yashnobod tumani"] = "Yashnobod tumani"
    if "bekobod" in list:
        toshkent["✅Bekobod tuman"] = "bekobod"
    else:
        toshkent["Bekobod tuman"] = "bekobod"
    if "bekobod_shahar" in list:
        toshkent["✅Bekobod shahar"] = "bekobod_shahar"
    else:
        toshkent["Bekobod shahar"] = "bekobod_shahar"
    if "bostonliq" in list:
        toshkent["✅Boʻstonliq tuman"] = 'bostonliq'
    else:
        toshkent["Boʻstonliq tuman"] = 'bostonliq'
    if "boka" in list:
        toshkent["✅Boʻka"] = "boka"
    else:
        toshkent["Boʻka"] = "boka"
    if "chinoz" in list:
        toshkent["✅Chinoz"] = 'chinoz'
    else:
        toshkent["Chinoz"] = 'chinoz'
    if "qibray" in list:
        toshkent["✅Qibray"] = 'qibray'
    else:
        toshkent["Qibray"] = 'qibray'
    if "ohangaron" in list:
        toshkent["✅Ohangaron tuman"] = "ohangaron"
    else:
        toshkent["Ohangaron tuman"] = 'ohangaron'
    if "ohangaron shahar" in list:
        toshkent["✅Ohangaron shahri"] = "ohangaron shahar"
    else:
        toshkent["Ohangaron shahri"] = 'ohangaron shahar'
    if "oqqorgon" in list:
        toshkent["✅Oqqoʻrgʻon"] = "oqqorgon"
    else:
        toshkent["Oqqoʻrgʻon"] = 'oqqorgon'
    if "parkent" in list:
        toshkent["✅Parkent"] = "parkent"
    else:
        toshkent["Parkent"] = "parkent"
    if "piskent" in list:
        toshkent["✅Piskent"] = "piskent"
    else:
        toshkent["Piskent"] = 'piskent'
    if "quyichirchiq" in list:
        toshkent["✅Quyi Chirchiq"] = "quyichirchiq"
    else:
        toshkent["Quyi Chirchiq"] = "quyichirchiq"
    if "ortachirchiq" in list:
        toshkent["✅Oʻrta Chirchiq"] = "ortachirchiq"
    else:
        toshkent["Oʻrta Chirchiq"] = "ortachirchiq"
    if "yangiyol" in list:
        toshkent["✅Yangiyoʻl"] = "yangiyol"
    else:
        toshkent["Yangiyoʻl"] = "yangiyol"
    if "yangiyol shahri" in list:
        toshkent["✅Yangiyoʻl shahri"] = "yangiyol shahri"
    else:
        toshkent["Yangiyoʻl shahri"] = "yangiyol shahri"
    if "yuqorichirchiq" in list:
        toshkent["✅Yuqori Chirchiq"] = "yuqorichirchiq"
    else:
        toshkent["Yuqori Chirchiq"] = "yuqorichirchiq"
    if "zangiota" in list:
        toshkent["✅Zangiota"] = "zangiota"
    else:
        toshkent["Zangiota"] = "zangiota"
    if "olmaliq" in list:
        toshkent["✅Olmaliq shahri"] = "olmaliq"
    else:
        toshkent["Olmaliq shahri"] = "olmaliq"
    if "nurafshon" in list:
        toshkent["✅Nurafshon shahri"] = "nurafshon"
    else:
        toshkent["Nurafshon shahri"] = "nurafshon"
    if "angren shahar" in list:
        toshkent["✅Angren shahar"] = "angren shahar"
    else:
        toshkent["Angren shahr"] = "angren shahar"
    if "angren" in list:
        toshkent["✅Angren"] = "angren"
    else:
        toshkent["Angren"] = "angren"
    if "chirchiq shahri" in list:
        toshkent["✅Chirchiq shahri"] = "chirchiq shahri"
    else:
        toshkent["Chirchiq shahri"] = "chirchiq shahri"
    if "qoyliq" in list:
        toshkent["✅Qo'yliq"] = "qoyliq"
    else:
        toshkent["Qo'yliq"] = "qoyliq"
    shaxsiy_toshkent = InlineKeyboardMarkup(row_width=3)
    for key, value in toshkent.items():
        shaxsiy_toshkent.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_toshkent.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
    shaxsiy_toshkent.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_toshkent.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))

    sirdaryo = {}
    if "sirdaryo shahar" in list:
        sirdaryo["✅Sirdaryo shahar"] = "sirdaryo shahar"
    else:
        sirdaryo["Sirdaryo shahar"] = "sirdaryo shahar"
    if "sirdaryo tuman" in list:
        sirdaryo["✅Sirdaryo tuman"] = "sirdaryo tuman"
    else:
        sirdaryo["Sirdaryo tuman"] = "sirdaryo tuman"
    if "oqoltin" in list:
        sirdaryo["✅Oqoltin"] = "oqoltin"
    else:
        sirdaryo["Oqoltin"] = "oqoltin"
    if "Shirin shahri" in list:
        sirdaryo["✅Shirin shahri"] = "Shirin shahri"
    else:
        sirdaryo["Shirin shahri"] = "Shirin shahri"
    if "Yangiyer shahri" in list:
        sirdaryo["✅Yangiyer shahri"] = "Yangiyer shahri"
    else:
        sirdaryo["Yangiyer shahri"] = "Yangiyer shahri"
    if "oqoltin" in list:
        sirdaryo["✅Oqoltin"] = "oqoltin"
    else:
        sirdaryo["Oqoltin"] = "oqoltin"
    if "boyovut" in list:
        sirdaryo["✅Boyovut"] = 'boyovut'
    else:
        sirdaryo["Boyovut"] = 'boyovut'
    if "guliston tuman" in list:
        sirdaryo["✅Guliston tuman"] = "guliston tuman"
    else:
        sirdaryo["Guliston tuman"] = "guliston tuman"
    if "guliston shahar" in list:
        sirdaryo["✅Guliston shahar"] = "guliston shahar"
    else:
        sirdaryo["Guliston shahar"] = "guliston shahar"
    if "xovos" in list:
        sirdaryo["✅Xovos"] = 'xovos'
    else:
        sirdaryo["Xovos"] = 'xovos'
    if "mirzaobod" in list:
        sirdaryo["✅Mirzaobod"] = 'mirzaobod'
    else:
        sirdaryo["Mirzaobod"] = 'mirzaobod'
    if "sayxunobod" in list:
        sirdaryo["✅Sayxunobod"] = "sayxunobod"
    else:
        sirdaryo["Sayxunobod"] = 'sayxunobod'
    if "sardoba" in list:
        sirdaryo["✅Sardoba"] = "sardoba"
    else:
        sirdaryo["Sardoba"] = 'sardoba'

    shaxsiy_sirdaryo = InlineKeyboardMarkup(row_width=3)
    for key, value in sirdaryo.items():
        shaxsiy_sirdaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_sirdaryo.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
    shaxsiy_sirdaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_sirdaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))

    surxondaryo = {}
    if "termiz shahar" in list:
        surxondaryo["✅Termiz shahar"] = "termiz shahar"
    else:
        surxondaryo["Termiz shahar"] = "termiz shahar"
    if "angor" in list:
        surxondaryo["✅Angor"] = "angor"
    else:
        surxondaryo["Angor"] = "angor"
    if "boysun" in list:
        surxondaryo["✅Boysun"] = "boysun"
    else:
        surxondaryo["Boysun"] = "boysun"
    if "denov" in list:
        surxondaryo["✅Denov"] = 'denov'
    else:
        surxondaryo["Denov"] = 'denov'
    if "jarqorgon" in list:
        surxondaryo["✅Jarqoʻrgʻon"] = "jarqorgon"
    else:
        surxondaryo["Jarqoʻrgʻon"] = 'jarqorgon'
    if "furqat" in list:
        surxondaryo["✅Furqat"] = "furqat"
    else:
        surxondaryo["Furqat"] = 'furqat'
    if "qiziriq" in list:
        surxondaryo["✅Qiziriq"] = "qiziriq"
    else:
        surxondaryo["Qiziriq"] = "qiziriq"
    if "qumqorgon" in list:
        surxondaryo["✅Qumqoʻrgʻon"] = "qumqorgon"
    else:
        surxondaryo["Qumqoʻrgʻon"] = 'qumqorgon'
    if "muzrabod" in list:
        surxondaryo["✅Muzrabod"] = "muzrabod"
    else:
        surxondaryo["Muzrabod"] = "muzrabod"
    if "oltinsoy" in list:
        surxondaryo["✅Oltinsoy"] = "oltinsoy"
    else:
        surxondaryo["Oltinsoy"] = "oltinsoy"
    if "sariosiyo" in list:
        surxondaryo["✅Sariosiyo"] = "sariosiyo"
    else:
        surxondaryo["Sariosiyo"] = "sariosiyo"
    if "sherobod" in list:
        surxondaryo["✅Sherobod"] = "sherobod"
    else:
        surxondaryo["Sherobod"] = "sherobod"
    if "shorchi" in list:
        surxondaryo["✅Shoʻrchi"] = "shorchi"
    else:
        surxondaryo["Shoʻrchi"] = "shorchi"
    if "termiz tuman" in list:
        surxondaryo["✅Termiz tuman"] = "termiz tuman"
    else:
        surxondaryo["Termiz tuman"] = "termiz tuman"
    if "uzun" in list:
        surxondaryo["✅Uzun"] = "uzun"
    else:
        surxondaryo["Uzun"] = "uzun"
    shaxsiy_surxondaryo = InlineKeyboardMarkup(row_width=3)
    for key, value in surxondaryo.items():
        shaxsiy_surxondaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_surxondaryo.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
    shaxsiy_surxondaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_surxondaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))

    qashqadaryo = {}
    if "qarshi shahar" in list:
        qashqadaryo["✅Qarshi shahar"] = "qarshi shahar"
    else:
        qashqadaryo["Qarshi shahar"] = "qarshi shahar"
    if "dehqonobod" in list:
        qashqadaryo["✅Dehqonobod"] = "dehqonobod"
    else:
        qashqadaryo["Dehqonobod"] = "dehqonobod"
    if "kasbi" in list:
        qashqadaryo["✅Kasbi"] = "kasbi"
    else:
        qashqadaryo["Kasbi"] = "kasbi"
    if "kitob" in list:
        qashqadaryo["✅Kitob"] = "kitob"
    else:
        qashqadaryo["Kitob"] = "kitob"
    if "koson" in list:
        qashqadaryo["✅Koson"] = 'koson'
    else:
        qashqadaryo["Koson"] = 'koson'
    if "kokdala" in list:
        qashqadaryo["✅Koʻkdala"] = 'kokdala'
    else:
        qashqadaryo["Koʻkdala"] = 'kokdala'
    if "mirishkor" in list:
        qashqadaryo["✅Mirishkor"] = "mirishkor"
    else:
        qashqadaryo["Mirishkor"] = 'mirishkor'
    if "muborak" in list:
        qashqadaryo["✅Muborak"] = "muborak"
    else:
        qashqadaryo["Muborak"] = 'muborak'
    if "nishon" in list:
        qashqadaryo["✅Nishon"] = "nishon"
    else:
        qashqadaryo["Nishon"] = "nishon"
    if "qamashi" in list:
        qashqadaryo["✅Qamashi"] = "qamashi"
    else:
        qashqadaryo["Qamashi"] = 'qamashi'
    if "qarshi" in list:
        qashqadaryo["✅Qarshi"] = "qarshi"
    else:
        qashqadaryo["Qarshi"] = "qarshi"
    if "yakkabog" in list:
        qashqadaryo["✅Yakkabogʻ"] = "yakkabog"
    else:
        qashqadaryo["Yakkabogʻ"] = "yakkabog"
    if "guzor" in list:
        qashqadaryo["✅Gʻuzor"] = "guzor"
    else:
        qashqadaryo["Gʻuzor"] = "guzor"
    if "shahrisabz" in list:
        qashqadaryo["✅Shahrisabz"] = "shahrisabz"
    else:
        qashqadaryo["Shahrisabz"] = "shahrisabz"
    if "shahrisabz shahar" in list:
        qashqadaryo["✅Shahrisabz shahar"] = "shahrisabz shahar"
    else:
        qashqadaryo["Shahrisabz shahar"] = "shahrisabz shahar"
    if "chiroqchi" in list:
        qashqadaryo["✅Chiroqchi"] = "chiroqchi"
    else:
        qashqadaryo["Chiroqchi"] = "chiroqchi"

    shaxsiy_qashqadaryo = InlineKeyboardMarkup(row_width=3)
    for key, value in qashqadaryo.items():
        shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
    shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_qashqadaryo.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))

    navoiy = {}
    if "Navoiy shahri" in list:
        navoiy["✅Navoiy shahri"] = "Navoiy shahri"
    else:
        navoiy["Navoiy shahri"] = "Navoiy shahri"
    if "Zarafshon shahri" in list:
        navoiy["✅Zarafshon shahri"] = "Zarafshon shahri"
    else:
        navoiy["Zarafshon shahri"] = "Zarafshon shahri"
    if "konimex" in list:
        navoiy["✅Konimex"] = "konimex"
    else:
        navoiy["Konimex"] = "konimex"
    if "karmana" in list:
        navoiy["✅Karmana"] = "karmana"
    else:
        navoiy["Karmana"] = "karmana"
    if "qiziltepa" in list:
        navoiy["✅Qiziltepa"] = "qiziltepa"
    else:
        navoiy["Qiziltepa"] = "qiziltepa"
    if "xatirchi" in list:
        navoiy["✅Xatirchi"] = 'xatirchi'
    else:
        navoiy["Xatirchi"] = 'xatirchi'
    if "navbahor" in list:
        navoiy["✅Navbahor"] = 'navbahor'
    else:
        navoiy["Navbahor"] = 'navbahor'
    if "nurota" in list:
        navoiy["✅Nurota"] = "nurota"
    else:
        navoiy["Nurota"] = "nurota"
    if "tomdi" in list:
        navoiy["✅Tomdi"] = "tomdi"
    else:
        navoiy["Tomdi"] = 'tomdi'
    if "uchquduq" in list:
        navoiy["✅Uchquduq"] = "uchquduq"
    else:
        navoiy["Uchquduq"] = "uchquduq"

    shaxsiy_navoiy = InlineKeyboardMarkup(row_width=3)
    for key, value in navoiy.items():
        shaxsiy_navoiy.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_navoiy.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
    shaxsiy_navoiy.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_navoiy.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))

    xorazm = {}
    if "urganch shahar" in list:
        xorazm["✅Urganch shahar"] = "urganch shahar"
    else:
        xorazm["Urganch shahar"] = "urganch shahar"
    if "bog'ot" in list:
        xorazm["✅Bogʻot"] = "bog'ot"
    else:
        xorazm["Bogʻot"] = "bog'ot"
    if "gurlan" in list:
        xorazm["✅Gurlan"] = "gurlan"
    else:
        xorazm["Gurlan"] = "gurlan"
    if "xonqa" in list:
        xorazm["✅Xonqa"] = "xonqa"
    else:
        xorazm["Xonqa"] = "xonqa"
    if "hazorasp" in list:
        xorazm["✅Hazorasp"] = 'hazorasp'
    else:
        xorazm["Hazorasp"] = 'hazorasp'
    if "xiva" in list:
        xorazm["✅Xiva"] = 'xiva'
    else:
        xorazm["Xiva"] = 'xiva'
    if "xiva shahar" in list:
        xorazm["✅Xiva shahar"] = 'xiva shahar'
    else:
        xorazm["Xiva shahar"] = 'xiva shahar'
    if "qoshko'prik" in list:
        xorazm["✅Qoʻshkoʻpir"] = "qoshko'prik"
    else:
        xorazm["Qoʻshkoʻpir"] = "qoshko'prik"
    if "shovot" in list:
        xorazm["✅Shovot"] = "shovot"
    else:
        xorazm["Shovot"] = 'shovot'
    if "urganch" in list:
        xorazm["✅Urganch tuman"] = "urganch"
    else:
        xorazm["Urganch tuman"] = "urganch"
    if "yangiariq" in list:
        xorazm["✅Yangiariq"] = "yangiariq"
    else:
        xorazm["Yangiariq"] = 'yangiariq'
    if "yangibozor" in list:
        xorazm["✅Yangibozor"] = "yangibozor"
    else:
        xorazm["Yangibozor"] = "yangibozor"
    if "tuproqqal'a" in list:
        xorazm["✅Tupproqqalʼa"] = "tuproqqal'a"
    else:
        xorazm["Tupproqqalʼa"] = "tuproqqal'a"

    shaxsiy_xorazm = InlineKeyboardMarkup(row_width=3)
    for key, value in xorazm.items():
        shaxsiy_xorazm.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_xorazm.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
    shaxsiy_xorazm.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_xorazm.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))

    jizzax = {}
    if "Jizzax shahri" in list:
        jizzax["✅Jizzax shahri"] = "Jizzax shahri"
    else:
        jizzax["Jizzax shahri"] = "Jizzax shahri"
    if "arnasoy" in list:
        jizzax["✅Arnasoy"] = "arnasoy"
    else:
        jizzax["Arnasoy"] = "arnasoy"
    if "baxmal" in list:
        jizzax["✅Baxmal"] = "baxmal"
    else:
        jizzax["Baxmal"] = "baxmal"
    if "do'stlik" in list:
        jizzax["✅Doʻstlik"] = "do'stlik"
    else:
        jizzax["Doʻstlik"] = "do'stlik"
    if "forish" in list:
        jizzax["✅Forish"] = 'forish'
    else:
        jizzax["Forish"] = 'forish'
    if "g'allarol" in list:
        jizzax["✅Koʻkdala"] = "g'allarol"
    else:
        jizzax["Koʻkdala"] = "g'allarol"
    if "sharof rashidov" in list:
        jizzax["✅Sharof Rashidov"] = "sharof rashidov"
    else:
        jizzax["Sharof Rashidov"] = 'sharof rashidov'
    if "mirzachol" in list:
        jizzax["✅Mirzachoʻl"] = "mirzachol"
    else:
        jizzax["Mirzachoʻl"] = 'mirzachol'
    if "paxtakor" in list:
        jizzax["✅Paxtakor"] = "paxtakor"
    else:
        jizzax["Paxtakor"] = "paxtakor"
    if "yangi obod" in list:
        jizzax["✅Yangiobod"] = "yangi obod"
    else:
        jizzax["Yangiobod"] = 'yangi obod'
    if "zomin" in list:
        jizzax["✅Zomin"] = "zomin"
    else:
        jizzax["Zomin"] = "zomin"
    if "zafarobod" in list:
        jizzax["✅Zafarobod"] = "zafarobod"
    else:
        jizzax["Zafarobod"] = "zafarobod"
    if "zarbdor" in list:
        jizzax["✅Zarbdor"] = "zarbdor"
    else:
        jizzax["Zarbdor"] = "zarbdor"
    shaxsiy_jizzax = InlineKeyboardMarkup(row_width=3)
    for key, value in jizzax.items():
        shaxsiy_jizzax.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_jizzax.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
    shaxsiy_jizzax.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_jizzax.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))

    samarqand = {}
    if "samarqand shahar" in list:
        samarqand["✅Samarqand shahar"] = "samarqand shahar"
    else:
        samarqand["Samarqand shahar"] = "samarqand shahar"
    if "samarqand tuman" in list:
        samarqand["✅Samarqand tuman"] = "samarqand tuman"
    else:
        samarqand["Samarqand tuman"] = "samarqand tuman"
    if "bulungur" in list:
        samarqand["✅Bulungʻur"] = "bulungur"
    else:
        samarqand["Bulungʻur"] = "bulungur"
    if "ishtixon" in list:
        samarqand["✅Ishtixon"] = "ishtixon"
    else:
        samarqand["Ishtixon"] = "ishtixon"
    if "jomboy" in list:
        samarqand["✅Jomboy"] = "jomboy"
    else:
        samarqand["Jomboy"] = "jomboy"
    if "kattaqorgon" in list:
        samarqand["✅Kattaqoʻrgʻon"] = 'kattaqorgon'
    else:
        samarqand["Kattaqoʻrgʻon"] = 'kattaqorgon'
    if "Kattaqoʻrgʻon shahar" in list:
        samarqand["✅Kattaqoʻrgʻon shahar"] = 'Kattaqoʻrgʻon shahar '
    else:
        samarqand["Kattaqoʻrgʻon shahar"] = 'Kattaqoʻrgʻon shahar'
    if "qoshrabot" in list:
        samarqand["✅Qoʻshrabot"] = "qoshrabot"
    else:
        samarqand["Qoʻshrabot"] = "qoshrabot"
    if "narpay" in list:
        samarqand["✅Narpay"] = "narpay"
    else:
        samarqand["Narpay"] = 'narpay'
    if "nurobod" in list:
        samarqand["✅Nurobod"] = "nurobod"
    else:
        samarqand["Nurobod"] = 'nurobod'
    if "oqdaryo" in list:
        samarqand["✅Oqdaryo"] = "oqdaryo"
    else:
        samarqand["Oqdaryo"] = "oqdaryo"
    if "paxtachi" in list:
        samarqand["✅Paxtachi"] = "paxtachi"
    else:
        samarqand["Paxtachi"] = 'paxtachi'
    if "payariq" in list:
        samarqand["✅Payariq"] = "payariq"
    else:
        samarqand["Payariq"] = "payariq"
    if "pastdargom" in list:
        samarqand["✅Pastdargʻom"] = "pastdargom"
    else:
        samarqand["Pastdargʻom"] = "pastdargom"
    if "toyloq" in list:
        samarqand["✅Toyloq"] = "toyloq"
    else:
        samarqand["Toyloq"] = "toyloq"
    shaxsiy_samarqand = InlineKeyboardMarkup(row_width=3)
    for key, value in samarqand.items():
        shaxsiy_samarqand.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_samarqand.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
    shaxsiy_samarqand.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_samarqand.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))

    qoraqalpoq = {}
    if "Nukus shahri" in list:
        qoraqalpoq["✅Nukus shahri"] = "Nukus shahri"
    else:
        qoraqalpoq["Nukus shahri"] = "Nukus shahri"
    if "Amudaryo tumani" in list:
        qoraqalpoq["✅Amudaryo tumani"] = 'Amudaryo tumani'
    else:
        qoraqalpoq["Amudaryo tumani"] = 'Amudaryo tumani'
    if "Beruniy tumani" in list:
        qoraqalpoq["✅Beruniy tumani"] = "Beruniy tumani"
    else:
        qoraqalpoq["Beruniy tumani"] = "Beruniy tumani"
    if "Kegeyli tumani" in list:
        qoraqalpoq["✅Kegeyli tumani"] = 'Kegeyli tumani'
    else:
        qoraqalpoq["Kegeyli tumani"] = 'Kegeyli tumani'
    if "Qanliko‘l tumani" in list:
        qoraqalpoq["✅Qanliko‘l tumani"] = 'Qanliko‘l tumani'
    else:
        qoraqalpoq["Qanliko‘l tumani"] = 'Qanliko‘l tumani'
    if "Qorao‘zak tumani" in list:
        qoraqalpoq["✅Qorao‘zak tumani"] = "Qorao‘zak tumani"
    else:
        qoraqalpoq["Qorao‘zak tumani"] = 'Qorao‘zak tumani'
    if "Qo‘ng‘irot tumani" in list:
        qoraqalpoq["✅Qo‘ng‘irot tumani"] = "Qo‘ng‘irot tumani"
    else:
        qoraqalpoq["Qo‘ng‘irot tumani"] = 'Qo‘ng‘irot tumani'
    if "Mo‘ynoq tumani" in list:
        qoraqalpoq["✅Mo‘ynoq tumani"] = "Mo‘ynoq tumani"
    else:
        qoraqalpoq["Mo‘ynoq tumani"] = "Mo‘ynoq tumani"
    if "Nukus tumani" in list:
        qoraqalpoq["✅Nukus tumani"] = 'Nukus tumani'
    else:
        qoraqalpoq["Nukus tumani"] = 'Nukus tumani'
    if "Taxiatosh tumani" in list:
        qoraqalpoq["✅Taxiatosh tumani"] = "Taxiatosh tumani"
    else:
        qoraqalpoq["Taxiatosh tumani"] = 'Taxiatosh tumani'
    if "Taxtako‘pir tumani" in list:
        qoraqalpoq["✅Taxtako‘pir tumani"] = "Taxtako‘pir tumani"
    else:
        qoraqalpoq["Taxtako‘pir tumani"] = 'Taxtako‘pir tumani'
    if "To‘rtko‘l tumani" in list:
        qoraqalpoq["✅To‘rtko‘l tumani"] = "To‘rtko‘l tumani"
    else:
        qoraqalpoq["To‘rtko‘l tumani"] = "To‘rtko‘l tumani"
    if "Xo‘jayli tumani" in list:
        qoraqalpoq["✅Xo‘jayli tumani"] = "Xo‘jayli tumani"
    else:
        qoraqalpoq["Xo‘jayli tumani"] = "Xo‘jayli tumani"
    if "Chimboy tumani" in list:
        qoraqalpoq["✅Chimboy tumani"] = "Chimboy tumani"
    else:
        qoraqalpoq["Chimboy tumani"] = "Chimboy tumani"
    if "Sho‘manoy tumani" in list:
        qoraqalpoq["✅Sho‘manoy tumani"] = "Sho‘manoy tumani"
    else:
        qoraqalpoq["Sho‘manoy tumani"] = "Sho‘manoy tumani"
    if "Ellikqal’a tumani" in list:
        qoraqalpoq["✅Ellikqal’a tumani"] = "Ellikqal’a tumani"
    else:
        qoraqalpoq["Ellikqal’a tumani"] = "Ellikqal’a tumani"

    shaxsiy_qoraqalpoq = InlineKeyboardMarkup(row_width=3)
    for key, value in qoraqalpoq.items():
        shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text=key, callback_data=value))
    shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Tanlab bo'ldim", callback_data="tanladim"))
    shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Ortga", callback_data="qaytish"))
    shaxsiy_qoraqalpoq.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
    if call.data == 'tanladim':

        jamii = await db.select_all_qoshimcha_tumanlar()
        list = []
        for i in jamii:
            if i[2] == call.from_user.id:
                list.append(i[1])
        for a in list:
            await db.delete_qoshimcha_tumanlar(telegram_id=call.from_user.id, tuman=a)
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Nexia', callback_data='Nexia'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Kobalt', callback_data='Kobalt'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Damas', callback_data='Damas'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Gentra', callback_data='Gentra'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Tracker', callback_data='Tracker'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Onix', callback_data='Onix'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Monza', callback_data='Monza'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Elektro car', callback_data='Elektro car'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Turini kiritish', callback_data='qoldayozish'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        await call.message.answer("Mahsinangiz qanday ? :   ", reply_markup=markup)
        await call.message.delete()
        await Reys_pochta_andijon.xa_yoq.set()
    if call.data == 'Olinmaydi':
        markup = aiogram.types.InlineKeyboardMarkup(row_width=3)
        markup.insert(aiogram.types.InlineKeyboardButton(text='Nexia', callback_data='Nexia'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Kobalt', callback_data='Kobalt'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Damas', callback_data='Damas'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Gentra', callback_data='Gentra'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Tracker', callback_data='Tracker'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Onix', callback_data='Onix'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Monza', callback_data='Monza'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Elektro car', callback_data='Elektro car'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Keyingisi', callback_data='Keyingisi'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Turini kiritish', callback_data='qoldayozish'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Ortga', callback_data='ortga'))
        markup.insert(aiogram.types.InlineKeyboardButton(text='Bosh menu', callback_data='boshmenu'))
        await call.message.answer("Mahsinangiz qanday ? :   ", reply_markup=markup)
        await call.message.delete()
        await Reys_pochta_andijon.xa_yoq.set()

    for key, value in andijon.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_tugma)
            await Reys_pochta_andijon.qoshimcha_tuman.set()
    for key, value in namangan.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_namangan)
            await Reys_pochta_andijon.qoshimcha_tuman.set()
    for key, value in fargona.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_fargona)
            await Reys_pochta_andijon.qoshimcha_tuman.set()
    for key, value in buxoro.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_buxoro)
            await Reys_pochta_andijon.qoshimcha_tuman.set()
    for key, value in toshkent.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_toshkent)
            await Reys_pochta_andijon.qoshimcha_tuman.set()
    for key, value in surxondaryo.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_surxondaryo)
            await Reys_pochta_andijon.qoshimcha_tuman.set()
    for key, value in sirdaryo.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_sirdaryo)
            await Reys_pochta_andijon.qoshimcha_tuman.set()

    for key, value in qashqadaryo.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_qashqadaryo)
            await Reys_pochta_andijon.qoshimcha_tuman.set()
    for key, value in xorazm.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_xorazm)
            await Reys_pochta_andijon.qoshimcha_tuman.set()

    for key, value in navoiy.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_navoiy)
            await Reys_pochta_andijon.qoshimcha_tuman.set()

    for key, value in jizzax.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_jizzax)
            await Reys_pochta_andijon.qoshimcha_tuman.set()

    for key, value in samarqand.items():
        if call.data == value:
            await call.message.edit_reply_markup(shaxsiy_samarqand)
            await Reys_pochta_andijon.qoshimcha_tuman.set()

    for key, value in qoraqalpoq.items():
            if call.data == value:
                await call.message.edit_reply_markup(shaxsiy_qoraqalpoq)
                await Reys_pochta_andijon.qoshimcha_tuman.set()



