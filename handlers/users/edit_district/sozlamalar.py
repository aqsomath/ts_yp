from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboards.inline.yolovchi.callback_data import kirish_callback, viloyatlar_callback,menu_callback
from keyboards.inline.yolovchi.viloyatlar import viloyatlar
from loader import dp,db


class SozlamalarStates(StatesGroup):
    kirish=State()
    viloyat_filter=State()
    haydovchi_tur=State()
    my_info=State()
    tarifni_almashtirish=State()
    tarifni_tanlash=State()

haydovchilar_royxati = []
@dp.callback_query_handler(kirish_callback.filter(item_name='haydovchi6656'))
async def haydovchif(call:CallbackQuery):
        haydovchilar_royxati.append(call.from_user.id)
        await db.haydovchi_set(haydovchi=True, telegram_id=call.from_user.id)
        await db.yolovchi_set(yolovchi=False, telegram_id=call.from_user.id)
        await db.add_haydovchi(username=call.from_user.username, telegram_id=call.from_user.id, balans=0)

        await db.add_driver(tashiman_odam="odam", tashiman_pochta='pochta', tashiman_yuk='yuk',
                            sayohatchi_tashiman='sayohat',
                            telegram_id=call.from_user.id)
        #QORAQALPOQ
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Nukus shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Amudaryo tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Beruniy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Kegeyli tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Qanliko'l tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Qorao'zak tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Qo'ng'irot tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Mo'ynoq tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Nukus tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Taxiatosh tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Taxtako'pir tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="To'rtko'l tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Xo'jayli tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Chimboy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Sho'manoy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qoraqalpog'iston", tuman="Ellikqal'a tumani", telegram_id=call.from_user.id)
        #TOSHKENT SHAHAR
        await db.add_driver_info(viloyat="Toshkent shahar", tuman="Toshkent shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent shahar", tuman="Bektemir tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent shahar", tuman="Mirzo Ulug'bek tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent shahar", tuman="Mirobod tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent shahar", tuman="Olmazor tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent shahar", tuman="Sirg'ali tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent shahar", tuman="Uchtepa tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent shahar", tuman="Chilonzor tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent shahar", tuman="Shayxontohur tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent shahar", tuman="Yunusobod tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent shahar", tuman="Yakkasaroy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent shahar", tuman="Yashnobod tumani", telegram_id=call.from_user.id)
        # XORAZM
        await db.add_driver_info(viloyat="Xorazm", tuman="bog'ot tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Xorazm", tuman="gurlan tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Xorazm", tuman="xonqa tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Xorazm", tuman="hazorasp tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Xorazm", tuman="xiva tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Xorazm", tuman="xiva shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Xorazm", tuman="qoshko'prik tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Xorazm", tuman="shovot tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Xorazm", tuman="urganch tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Xorazm", tuman="urganch shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Xorazm", tuman="yangiariq tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Xorazm", tuman="yangibozor tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Xorazm", tuman="tuproqqal'a tumani", telegram_id=call.from_user.id)
        # TOSHKENT
        await db.add_driver_info(viloyat="Toshkent", tuman="toshkent tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="angren shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="nurafshon shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="bekobod shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="olmaliq shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="chirchiq shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="bekobod tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="bostonliq tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="boka tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="chinoz tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="qibray tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="ohangaron shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="ohangaron tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="oqqorgon tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="parkent tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="piskent tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="quyichirchiq tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="ortachirchiq tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="yangiyol shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="yangiyol tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="yuqorichirchiq tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="zangiota tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Toshkent", tuman="qoyliq", telegram_id=call.from_user.id)
        # SURXONDARYO
        await db.add_driver_info(viloyat="Surxondaryo", tuman="angor tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Surxondaryo", tuman="bandixon tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Surxondaryo", tuman="boysun tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Surxondaryo", tuman="denov tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Surxondaryo", tuman="jarqorgon tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Surxondaryo", tuman="qiziriq tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Surxondaryo", tuman="qumqorgon tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Surxondaryo", tuman="muzrabod tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Surxondaryo", tuman="oltinsoy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Surxondaryo", tuman="sariosiyo tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Surxondaryo", tuman="sherobod tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Surxondaryo", tuman="shorchi tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Surxondaryo", tuman="termiz tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Surxondaryo", tuman="termiz shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Surxondaryo", tuman="uzun tumani", telegram_id=call.from_user.id)
        # SIRDARYO
        await db.add_driver_info(viloyat="Sirdaryo", tuman="oqoltin tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Sirdaryo", tuman="boyovut tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Sirdaryo", tuman="guliston shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Sirdaryo", tuman="guliston tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Sirdaryo", tuman="shirin shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Sirdaryo", tuman="yangiyer shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Sirdaryo", tuman="xovos tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Sirdaryo", tuman="mirzaobod tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Sirdaryo", tuman="sardoba tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Sirdaryo", tuman="sayxunobod tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Sirdaryo", tuman="sirdaryo shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Sirdaryo", tuman="sirdaryo tumani", telegram_id=call.from_user.id)
        # SAMARQAND
        await db.add_driver_info(viloyat="Samarqand", tuman="bulungur tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="ishtixon tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="jomboy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="kattaqorgon shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="kattaqorgon tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="qoshrabot tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="narpay tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="nurobod tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="oqdaryo tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="paxtachi tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="payariq tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="pastdargom tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="samarqand shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="samarqand tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Samarqand", tuman="toyloq tumani", telegram_id=call.from_user.id)
        # QASHQADARYO
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="dehqonobod tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="kasbi tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="kitob tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="koson tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="kokdala tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="mirishkor tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="muborak tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="nishon tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="qamashi tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="qarshi shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="qarshi tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="yakkabog tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="guzor tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="shahrisabz tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="shahrisabz shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Qashqadaryo", tuman="chiroqchi tumani", telegram_id=call.from_user.id)
        # NAVOIY
        await db.add_driver_info(viloyat="Navoiy", tuman="navoiy shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="zarafshon shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="konimex tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="karmana tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="qiziltepa tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="xatirchi tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="navbahor tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="nurota tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="tomdi tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Navoiy", tuman="uchquduq tumani", telegram_id=call.from_user.id)
        # NAMANGAN
        await db.add_driver_info(viloyat="Namangan", tuman="chortoq tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="chust tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="kosonsoy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="mingbuloq tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="namangan shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="namangan tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="norin tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="pop tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="toraqo'rg'on tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="uchqo'rgo'n tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="uychi tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="yangi qo'rg'on tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Namangan", tuman="yangi namangan tumani", telegram_id=call.from_user.id)
        # JIZZAX
        await db.add_driver_info(viloyat="Jizzax", tuman="jizzax shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="arnasoy tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="baxmal tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="do'stlik tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="forish tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="g'allarol tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="sharof rashidov tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="mirzachol tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="paxtakor tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="yangi obod tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="zomin tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="zafarobod tumani", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Jizzax", tuman="zarbdor tumani", telegram_id=call.from_user.id)

        # ANDIJON
        await db.add_driver_info(viloyat="Andijon", tuman="ulug'nor tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Andijon", tuman="andijon shaxar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Andijon", tuman="andijon tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Andijon", tuman="asaka tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Andijon", tuman="paxtaobod tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Andijon", tuman="shaxrixon tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Andijon", tuman="marhamat tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Andijon", tuman="xonabod shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Andijon", tuman="oltinko'l tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Andijon", tuman="baliqchi tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Andijon", tuman="bo'ston tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Andijon", tuman="buloqboshi tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Andijon", tuman="izboskan tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Andijon", tuman="jalaquduq tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Andijon", tuman="xo'jabod tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Andijon", tuman="qo'rg'ontepa tuman", telegram_id=call.from_user.id)
        # FAEG'ONA
        await db.add_driver_info(viloyat="Farg'ona", tuman="o'zbekiston tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="uchko'prik tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="yozyovon tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="toshloq tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="sox tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="rishton tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="quva tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="oltiariq tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="farg'ona tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="furqat tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="qo'shtepa tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="dangara tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="buvayda tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="beshariq tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="bog'dod tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="qo'qon shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="quvasoy shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="marg'ilon shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Farg'ona", tuman="farg'ona shahar", telegram_id=call.from_user.id)
        # BUXORO
        await db.add_driver_info(viloyat="Buxoro", tuman="olot tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Buxoro", tuman="buxoro shaxar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Buxoro", tuman="buxoro tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Buxoro", tuman="g'ijduvon tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Buxoro", tuman="jondor tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Buxoro", tuman="kogon tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Buxoro", tuman="kogon shahar", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Buxoro", tuman="qorako'l tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Buxoro", tuman="qorovulbozor tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Buxoro", tuman="peshku tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Buxoro", tuman="romitan tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Buxoro", tuman="shofirkon tuman", telegram_id=call.from_user.id)
        await db.add_driver_info(viloyat="Buxoro", tuman="vobkent tuman", telegram_id=call.from_user.id)
        driver={
        "Haydovchi reys belgilash":'yolovchikerak',
        "Tayyor yo'lovchi": 'tayyoryolovchi',
        "Yuk kerak":'yukkerak',
        "Tayyor yuk": "tayyoryuk",
        "Pochta kerak":'pochtakerak',
        "Tayyor pochta": "tayyorpochta",
        "Sayohatchilar kerak":'sayohatgayolovchi',
        "Tayyor sayohatchi":"tayyorsayohatchi",
        "Mening buyurtmalarim": "meningbuyurtmalarim",
        "Admin bilan bog'lanish": "adminbilanboglanish",
        "Sozlamalar":"nastroyki",
        "Yo'lovchi bo'lib davom etish": "yolovchibolibdavometish"

        }
        markup = InlineKeyboardMarkup(row_width=2)
        for key,value in driver.items():
            markup.insert(InlineKeyboardButton(text=key, callback_data=menu_callback.new(item_name=value)))
        await call.message.answer("Salom haydovchi\nSizga kerakli xizmat turini tanlang !", reply_markup=markup)
        await call.message.delete()

@dp.callback_query_handler(menu_callback.filter(item_name='nastroyki'))
async def sozlamalar(call:CallbackQuery):
    marrk = InlineKeyboardMarkup(row_width=2)
    marrk.insert(InlineKeyboardButton(text='Filtrlash', callback_data='filtrlash'))
    marrk.insert(InlineKeyboardButton(text="Mening ma'lumotlarim", callback_data='meningmalumotlarim'))
    marrk.insert(InlineKeyboardButton(text='Ortga ', callback_data='headmenu'))
    marrk.insert(InlineKeyboardButton(text='Bosh menu ', callback_data='headmenu'))
    await call.message.answer("Sozlamalar bo'limi ",reply_markup=marrk)
    await SozlamalarStates.kirish.set()
    await call.message.delete()

@dp.message_handler(commands='filter')
async def sozlamalar(message:Message):
    marrk = InlineKeyboardMarkup(row_width=2)
    marrk.insert(InlineKeyboardButton(text='Filtrlash', callback_data='filtrlash'))
    marrk.insert(InlineKeyboardButton(text="Mening ma'lumotlarim", callback_data='meningmalumotlarim'))
    marrk.insert(InlineKeyboardButton(text='Ortga ', callback_data='headmenu'))
    marrk.insert(InlineKeyboardButton(text='Bosh menu ', callback_data='headmenu'))
    await message.answer("Sozlamalar bo'limi ", reply_markup=marrk)
    await SozlamalarStates.kirish.set()
    await message.delete()


@dp.callback_query_handler(text=["headmenu"],state=SozlamalarStates.kirish)
async def ortga_qarab_qoch(call:CallbackQuery,state:FSMContext):
    
        driver = {
            "Haydovchi reys belgilash": 'yolovchikerak',
            "Tayyor yo'lovchi": 'tayyoryolovchi',
            "Yuk kerak": 'yukkerak',
            "Tayyor yuk": "tayyoryuk",
            "Pochta kerak": 'pochtakerak',
            "Tayyor pochta": "tayyorpochta",
            "Sayohatchilar kerak": 'sayohatgayolovchi',
            "Tayyor sayohatchi": "tayyorsayohatchi",
            "Mening buyurtmalarim": "meningbuyurtmalarim",
            "Admin bilan bog'lanish": "adminbilanboglanish",
            "Sozlamalar": "nastroyki",
            "Yo'lovchi bo'lib davom etish": "yolovchibolibdavometish"

        }
        markup = InlineKeyboardMarkup(row_width=2)
        for key, value in driver.items():
            markup.insert(InlineKeyboardButton(text=key, callback_data=menu_callback.new(item_name=value)))
        await call.message.answer("Salom haydovchi\nSizga kerakli xizmat turini tanlang !", reply_markup=markup)
        await call.message.delete()
        await state.finish()
@dp.callback_query_handler(text="filtrlash",state=SozlamalarStates.kirish)
async def katta_filtr(call:CallbackQuery,state:FSMContext):
    
        mark=InlineKeyboardMarkup(row_width=2)
        mark.insert(InlineKeyboardButton(text="Haydovchi filter",callback_data="haydovchifilter"))
        mark.insert(InlineKeyboardButton(text="Viloyat filter",callback_data="viloyatfilter"))
        mark.insert(InlineKeyboardButton(text=" Ortga",callback_data="ortga"))
        mark.insert(InlineKeyboardButton(text="Bosh menu",callback_data="boshmenu"))
        await call.message.answer("O'zingizga mos qilib sozlang.", reply_markup=mark)
        await call.message.delete()

@dp.callback_query_handler(text="ortga",state=SozlamalarStates.kirish)
async def ortga(call:CallbackQuery,state:FSMContext):
    
        marrk = InlineKeyboardMarkup(row_width=2)
        marrk.insert(InlineKeyboardButton(text='Filtrlash', callback_data='filtrlash'))
        marrk.insert(InlineKeyboardButton(text="Mening ma'lumotlarim", callback_data='meningmalumotlarim'))
        marrk.insert(InlineKeyboardButton(text='Ortga ', callback_data='headmenu'))
        marrk.insert(InlineKeyboardButton(text='Bosh menu ', callback_data='headmenu'))
        await call.message.answer("Sozlamalar bo'limi ", reply_markup=marrk)
        await SozlamalarStates.kirish.set()
        await call.message.delete()
@dp.callback_query_handler(text="haydovchifilter",state=SozlamalarStates.kirish)
async def haydovchi_filter(call:CallbackQuery,state:FSMContext):
    

        tur={}
        odam=[]
        yuk=[]
        pochta=[]
        sayohat=[]
        drivers=await db.select_all_driver()
        for i in drivers:
            if i[4]==call.from_user.id:
                odam.append(i[1])
                yuk.append(i[2])
                pochta.append(i[3])
                sayohat.append(i[5])
        if "odam" in odam:
            tur["✅Odam tashiman"]="odam"
        else:
            tur["Odam tashiman"] = "odam"
        if "yuk" in yuk:
            tur["✅Yuk tashiman"] = "yuk"
        else:
            tur["Yuk tashiman"] = "yuk"
        if "pochta" in pochta:
            tur["✅Pochta tashiman"] = "pochta"
        else:
            tur["Pochta tashiman"] = "pochta"
        if "sayohat" in sayohat:
            tur["✅Sayohatchi tashiman"] = "sayohat"
        else:
            tur["Sayohatchi tashiman"] = "sayohat"
        tur["Ortga"]='ortga'
        tur["Bosh menu"]='boshmenu'
        haydovchi_tur=InlineKeyboardMarkup(row_width=2)
        for key,value in tur.items():
            haydovchi_tur.insert(InlineKeyboardButton(text=key,callback_data=value))
        print(drivers)
        await call.message.answer("Siz aynan nima tashisiz ?",reply_markup=haydovchi_tur)
        await SozlamalarStates.haydovchi_tur.set()
        await call.message.delete()

@dp.callback_query_handler(state=SozlamalarStates.haydovchi_tur)
async def nimatashiman(call:CallbackQuery,state:FSMContext):
    

        if call.data=="odam":
            await db.add_driver(tashiman_odam="odam",tashiman_pochta=None,tashiman_yuk=None,sayohatchi_tashiman=None,telegram_id=call.from_user.id)
            tur = {}
            odam = []
            yuk = []
            pochta = []
            sayohat = []
            drivers = await db.select_all_driver()
            for i in drivers:
                if i[4] == call.from_user.id:
                    odam.append(i[1])
                    yuk.append(i[2])
                    pochta.append(i[3])
                    sayohat.append(i[5])
            if "odam" in odam:
                tur["✅Odam tashiman"] = "fdadfas"
            else:
                tur["Odam tashiman"] = "odam"
            if "yuk" in yuk:
                tur["✅Yuk tashiman"] = "eredsdcasdasd"
            else:
                tur["Yuk tashiman"] = "yuk"
            if "pochta" in pochta:
                tur["✅Pochta tashiman"] = "pferfsasdadedwocht"
            else:
                tur["Pochta tashiman"] = "pochta"
            if "sayohat" in sayohat:
                tur["✅Sayohatchi tashiman"] = "brgtbgfdfverfsdcsd"
            else:
                tur["Sayohatchi tashiman"] = "sayohat"
            tur["Ortga"] = 'ortga'
            tur["Bosh menu"] = 'boshmenu'
            haydovchi_tur = InlineKeyboardMarkup(row_width=2)
            for key, value in tur.items():
                haydovchi_tur.insert(InlineKeyboardButton(text=key, callback_data=value))
            print(drivers)
            await call.message.edit_reply_markup(haydovchi_tur)
            await SozlamalarStates.haydovchi_tur.set()

        if call.data=="yuk":
                await db.add_driver(tashiman_odam=None,tashiman_pochta=None,tashiman_yuk="yuk",sayohatchi_tashiman=None,telegram_id=call.from_user.id)
                tur = {}
                odam = []
                yuk = []
                pochta = []
                sayohat = []
                drivers = await db.select_all_driver()
                for i in drivers:
                    if i[4] == call.from_user.id:
                        odam.append(i[1])
                        yuk.append(i[2])
                        pochta.append(i[3])
                        sayohat.append(i[5])
                if "odam" in odam:
                    tur["✅Odam tashiman"] = "fdadfas"
                else:
                    tur["Odam tashiman"] = "odam"
                if "yuk" in yuk:
                    tur["✅Yuk tashiman"] = "eredsdcasdasd"
                else:
                    tur["Yuk tashiman"] = "yuk"
                if "pochta" in pochta:
                    tur["✅Pochta tashiman"] = "pferfsasdadedwocht"
                else:
                    tur["Pochta tashiman"] = "pochta"
                if "sayohat" in sayohat:
                    tur["✅Sayohatchi tashiman"] = "brgtbgfdfverfsdcsd"
                else:
                    tur["Sayohatchi tashiman"] = "sayohat"
                tur["Ortga"] = 'ortga'
                tur["Bosh menu"] = 'boshmenu'
                haydovchi_tur = InlineKeyboardMarkup(row_width=2)
                for key, value in tur.items():
                    haydovchi_tur.insert(InlineKeyboardButton(text=key, callback_data=value))
                print(drivers)
                await call.message.edit_reply_markup(haydovchi_tur)
                await SozlamalarStates.haydovchi_tur.set()

        if call.data=="pochta":
                await db.add_driver(tashiman_odam=None,tashiman_pochta='pochta',tashiman_yuk=None,sayohatchi_tashiman=None,telegram_id=call.from_user.id)
                tur = {}
                odam = []
                yuk = []
                pochta = []
                sayohat = []
                drivers = await db.select_all_driver()
                for i in drivers:
                    if i[4] == call.from_user.id:
                        odam.append(i[1])
                        yuk.append(i[2])
                        pochta.append(i[3])
                        sayohat.append(i[5])
                if "odam" in odam:
                    tur["✅Odam tashiman"] = "fdadfas"
                else:
                    tur["Odam tashiman"] = "odam"
                if "yuk" in yuk:
                    tur["✅Yuk tashiman"] = "eredsdcasdasd"
                else:
                    tur["Yuk tashiman"] = "yuk"
                if "pochta" in pochta:
                    tur["✅Pochta tashiman"] = "pferfsasdadedwocht"
                else:
                    tur["Pochta tashiman"] = "pochta"
                if "sayohat" in sayohat:
                    tur["✅Sayohatchi tashiman"] = "brgtbgfdfverfsdcsd"
                else:
                    tur["Sayohatchi tashiman"] = "sayohat"
                tur["Ortga"] = 'ortga'
                tur["Bosh menu"] = 'boshmenu'
                haydovchi_tur = InlineKeyboardMarkup(row_width=2)
                for key, value in tur.items():
                    haydovchi_tur.insert(InlineKeyboardButton(text=key, callback_data=value))
                print(drivers)
                await call.message.edit_reply_markup(haydovchi_tur)
                await SozlamalarStates.haydovchi_tur.set()
        if call.data=="sayohat":
                await db.add_driver(tashiman_odam=None,tashiman_pochta=None,tashiman_yuk=None,sayohatchi_tashiman='sayohat',telegram_id=call.from_user.id)
                tur = {}
                odam = []
                yuk = []
                pochta = []
                sayohat = []
                drivers = await db.select_all_driver()
                for i in drivers:
                    if i[4] == call.from_user.id:
                        odam.append(i[1])
                        yuk.append(i[2])
                        pochta.append(i[3])
                        sayohat.append(i[5])
                if "odam" in odam:
                    tur["✅Odam tashiman"] = "fdadfas"
                else:
                    tur["Odam tashiman"] = "odam"
                if "yuk" in yuk:
                    tur["✅Yuk tashiman"] = "eredsdcasdasd"
                else:
                    tur["Yuk tashiman"] = "yuk"
                if "pochta" in pochta:
                    tur["✅Pochta tashiman"] = "pferfsasdadedwocht"
                else:
                    tur["Pochta tashiman"] = "pochta"
                if "sayohat" in sayohat:
                    tur["✅Sayohatchi tashiman"] = "brgtbgfdfverfsdcsd"
                else:
                    tur["Sayohatchi tashiman"] = "sayohat"
                tur["Ortga"] = 'ortga'
                tur["Bosh menu"] = 'boshmenu'
                haydovchi_tur = InlineKeyboardMarkup(row_width=2)
                for key, value in tur.items():
                    haydovchi_tur.insert(InlineKeyboardButton(text=key, callback_data=value))
                print(drivers)
                await call.message.edit_reply_markup(haydovchi_tur)
                await SozlamalarStates.haydovchi_tur.set()







        if call.data=="fdadfas":
            await db.delete_driver(tashiman_odam="odam",telegram_id=call.from_user.id)
            tur = {}
            odam = []
            yuk = []
            pochta = []
            sayohat = []
            drivers = await db.select_all_driver()
            for i in drivers:
                if i[4] == call.from_user.id:
                    odam.append(i[1])
                    yuk.append(i[2])
                    pochta.append(i[3])
                    sayohat.append(i[5])
            if "odam" in odam:
                tur["✅Odam tashiman"] = "fdadfas"
            else:
                tur["Odam tashiman"] = "odam"
            if "yuk" in yuk:
                tur["✅Yuk tashiman"] = "eredsdcasdasd"
            else:
                tur["Yuk tashiman"] = "yuk"
            if "pochta" in pochta:
                tur["✅Pochta tashiman"] = "pferfsasdadedwocht"
            else:
                tur["Pochta tashiman"] = "pochta"
            if "sayohat" in sayohat:
                tur["✅Sayohatchi tashiman"] = "brgtbgfdfverfsdcsd"
            else:
                tur["Sayohatchi tashiman"] = "sayohat"
            tur["Ortga"] = 'ortga'
            tur["Bosh menu"] = 'boshmenu'
            haydovchi_tur = InlineKeyboardMarkup(row_width=2)
            for key, value in tur.items():
                haydovchi_tur.insert(InlineKeyboardButton(text=key, callback_data=value))
            print(drivers)
            await call.message.edit_reply_markup(haydovchi_tur)
            await SozlamalarStates.haydovchi_tur.set()

        if call.data=="eredsdcasdasd":
                await db.delete_driver(tashiman_yuk="yuk",telegram_id=call.from_user.id)
                tur = {}
                odam = []
                yuk = []
                pochta = []
                sayohat = []
                drivers = await db.select_all_driver()
                for i in drivers:
                    if i[4] == call.from_user.id:
                        odam.append(i[1])
                        yuk.append(i[2])
                        pochta.append(i[3])
                        sayohat.append(i[5])
                if "odam" in odam:
                    tur["✅Odam tashiman"] = "fdadfas"
                else:
                    tur["Odam tashiman"] = "odam"
                if "yuk" in yuk:
                    tur["✅Yuk tashiman"] = "eredsdcasdasd"
                else:
                    tur["Yuk tashiman"] = "yuk"
                if "pochta" in pochta:
                    tur["✅Pochta tashiman"] = "pferfsasdadedwocht"
                else:
                    tur["Pochta tashiman"] = "pochta"
                if "sayohat" in sayohat:
                    tur["✅Sayohatchi tashiman"] = "brgtbgfdfverfsdcsd"
                else:
                    tur["Sayohatchi tashiman"] = "sayohat"
                tur["Ortga"] = 'ortga'
                tur["Bosh menu"] = 'boshmenu'
                haydovchi_tur = InlineKeyboardMarkup(row_width=2)
                for key, value in tur.items():
                    haydovchi_tur.insert(InlineKeyboardButton(text=key, callback_data=value))
                print(drivers)
                await call.message.edit_reply_markup(haydovchi_tur)
                await SozlamalarStates.haydovchi_tur.set()

        if call.data=="pferfsasdadedwocht":
                await db.delete_driver(tashiman_pochta='pochta',telegram_id=call.from_user.id)
                tur = {}
                odam = []
                yuk = []
                pochta = []
                sayohat = []
                drivers = await db.select_all_driver()
                for i in drivers:
                    if i[4] == call.from_user.id:
                        odam.append(i[1])
                        yuk.append(i[2])
                        pochta.append(i[3])
                        sayohat.append(i[5])
                if "odam" in odam:
                    tur["✅Odam tashiman"] = "fdadfas"
                else:
                    tur["Odam tashiman"] = "odam"
                if "yuk" in yuk:
                    tur["✅Yuk tashiman"] = "eredsdcasdasd"
                else:
                    tur["Yuk tashiman"] = "yuk"
                if "pochta" in pochta:
                    tur["✅Pochta tashiman"] = "pferfsasdadedwocht"
                else:
                    tur["Pochta tashiman"] = "pochta"
                if "sayohat" in sayohat:
                    tur["✅Sayohatchi tashiman"] = "brgtbgfdfverfsdcsd"
                else:
                    tur["Sayohatchi tashiman"] = "sayohat"
                tur["Ortga"] = 'ortga'
                tur["Bosh menu"] = 'boshmenu'
                haydovchi_tur = InlineKeyboardMarkup(row_width=2)
                for key, value in tur.items():
                    haydovchi_tur.insert(InlineKeyboardButton(text=key, callback_data=value))
                print(drivers)
                await call.message.edit_reply_markup(haydovchi_tur)
                await SozlamalarStates.haydovchi_tur.set()
        if call.data=="brgtbgfdfverfsdcsd":
                await db.delete_driver(sayohatchi_tashiman='sayohat',telegram_id=call.from_user.id)
                tur = {}
                odam = []
                yuk = []
                pochta = []
                sayohat = []
                drivers = await db.select_all_driver()
                for i in drivers:
                    if i[4] == call.from_user.id:
                        odam.append(i[1])
                        yuk.append(i[2])
                        pochta.append(i[3])
                        sayohat.append(i[5])
                if "odam" in odam:
                    tur["✅Odam tashiman"] = "fdadfas"
                else:
                    tur["Odam tashiman"] = "odam"
                if "yuk" in yuk:
                    tur["✅Yuk tashiman"] = "eredsdcasdasd"
                else:
                    tur["Yuk tashiman"] = "yuk"
                if "pochta" in pochta:
                    tur["✅Pochta tashiman"] = "pferfsasdadedwocht"
                else:
                    tur["Pochta tashiman"] = "pochta"
                if "sayohat" in sayohat:
                    tur["✅Sayohatchi tashiman"] = "brgtbgfdfverfsdcsd"
                else:
                    tur["Sayohatchi tashiman"] = "sayohat"
                tur["Ortga"] = 'ortga'
                tur["Bosh menu"] = 'boshmenu'
                haydovchi_tur = InlineKeyboardMarkup(row_width=2)
                for key, value in tur.items():
                    haydovchi_tur.insert(InlineKeyboardButton(text=key, callback_data=value))
                print(drivers)
                await call.message.edit_reply_markup(haydovchi_tur)
                await SozlamalarStates.haydovchi_tur.set()
        if call.data=="boshmenu":
            driver = {
                "Haydovchi reys belgilash": 'yolovchikerak',
                "Tayyor yo'lovchi": 'tayyoryolovchi',
                "Yuk kerak": 'yukkerak',
                "Tayyor yuk": "tayyoryuk",
                "Pochta kerak": 'pochtakerak',
                "Tayyor pochta": "tayyorpochta",
                "Sayohatchilar kerak": 'sayohatgayolovchi',
                "Tayyor sayohatchi": "tayyorsayohatchi",
                "Mening buyurtmalarim": "meningbuyurtmalarim",
                "Admin bilan bog'lanish": "adminbilanboglanish",
                "Sozlamalar": "nastroyki",
                "Yo'lovchi bo'lib davom etish": "yolovchibolibdavometish"

            }
            markup = InlineKeyboardMarkup(row_width=2)
            for key, value in driver.items():
                markup.insert(InlineKeyboardButton(text=key, callback_data=menu_callback.new(item_name=value)))
            await call.message.answer("Salom haydovchi\nSizga kerakli xizmat turini tanlang !", reply_markup=markup)
            await call.message.delete()
            await state.finish()
        if call.data=="ortga":
                mark = InlineKeyboardMarkup(row_width=2)
                mark.insert(InlineKeyboardButton(text="Haydovchi filter", callback_data="haydovchifilter"))
                mark.insert(InlineKeyboardButton(text="Viloyat filter", callback_data="viloyatfilter"))
                mark.insert(InlineKeyboardButton(text=" Ortga", callback_data="ortga"))
                mark.insert(InlineKeyboardButton(text="Bosh menu", callback_data="boshmenu"))
                await call.message.answer("O'zingizga mos qilib sozlang.", reply_markup=mark)
                await SozlamalarStates.kirish.set()
                await call.message.delete()
@dp.callback_query_handler(text="viloyatfilter",state=SozlamalarStates.kirish)
async def viloyat_filter(call:CallbackQuery,state:FSMContext):
    
        await call.message.answer("Siz qaysi viloyat haydovchisisiz ?", reply_markup=viloyatlar)
        await SozlamalarStates.viloyat_filter.set()
        await call.message.delete()
@dp.callback_query_handler(viloyatlar_callback.filter(item_name='nazad'),state=SozlamalarStates.viloyat_filter)
async def katta_filtr(call:CallbackQuery,state:FSMContext):
    
        mark=InlineKeyboardMarkup(row_width=2)
        mark.insert(InlineKeyboardButton(text="Haydovchi filter",callback_data="haydovchifilter"))
        mark.insert(InlineKeyboardButton(text="Viloyat filter",callback_data="viloyatfilter"))
        mark.insert(InlineKeyboardButton(text=" Ortga",callback_data="ortga"))
        mark.insert(InlineKeyboardButton(text="Bosh menu",callback_data="boshmenu"))
        await call.message.answer("O'zingizga mos qilib sozlang.", reply_markup=mark)
        await call.message.delete()
        await SozlamalarStates.kirish.set()
@dp.callback_query_handler(text="meningmalumotlarim",state=SozlamalarStates.kirish)
async def my_report(call:CallbackQuery,state:FSMContext):
    try:
        driver = await db.select_user(telegram_id=call.from_user.id)
        balans = driver[7]
        msg=(f"<b>Sizning ma'lumotlaringiz </b>\n\n"
             f"Haydovchi nomi :\n{call.from_user.full_name}\n\n"
             f"Haydovchi ID :\n{driver[0]}\n"
             f"Haydovchi telegram ID :\n{driver[3]} \n"
             f"Balans :{balans} \n"
            )
        markup=InlineKeyboardMarkup(row_width=2)
        markup.insert(InlineKeyboardButton(text="Balansni to'ldirish", callback_data="balansnitoldirish"))
        markup.insert(InlineKeyboardButton(text="Tarifni almashtirish", callback_data="tarifnialmashtirish"))
        markup.insert(InlineKeyboardButton(text="Ortga",callback_data="ortga"))
        markup.insert(InlineKeyboardButton(text="Bosh menu",callback_data="boshmenu"))
        await call.message.answer(msg,reply_markup=markup)
        await SozlamalarStates.my_info.set()
        await call.message.delete()
    except TypeError:
        await call.message.answer("Uzr bu bo'lim faqat haydovchilar uchun. Siz haydovchilar ro'yxatida yo'qsiz.")
        await call.message.delete()
        await state.finish()
@dp.callback_query_handler(text="balansnitoldirish",state=SozlamalarStates.my_info)
async def balans_toldirish(call:CallbackQuery,state:FSMContext):
    await call.message.answer(f"Admin bilan bog'lanib balansingizni to'ldiring :\n"
                              f"Telefon : +998 94 100 79 74\n"
                              f"Telegram : <a href='tg://user?id={343103355}'>Admin</a> ")
    await state.finish()


@dp.callback_query_handler(text="tarifnialmashtirish",state=SozlamalarStates.my_info)
async def balans_toldirish(call:CallbackQuery,state:FSMContext):
    one = await db.select_tarif(tarif_name='first')
    msg_1 = f"Kuniga {one[3]}ta qabul qilish, oyiga - > {one[2]}"
    two = await db.select_tarif(tarif_name='second')
    msg_2 = f"Kuniga {two[3]}ta qabul qilish, oyiga - > {two[2]}"
    three = await db.select_tarif(tarif_name='third')
    msg_3 = f"Kuniga {three[3]}ta qabul qilish, oyiga - > {three[2]}"
    markup = InlineKeyboardMarkup(row_width=2)
    markup.insert(InlineKeyboardButton(text="1 - tarif", callback_data="changebirinchitarif"))
    markup.insert(InlineKeyboardButton(text="2 - tarif ", callback_data="changeikkinchitarif"))
    markup.insert(InlineKeyboardButton(text="3 - tarif", callback_data="changeuchinchitarif"))
    await call.message.answer("Qaysi tarifga ulanmoqchisiz\n"
                              f"<b>1 - tarif </b>\n{msg_1}\n"
                              f"<b>2 - tarif </b>\n{msg_2}\n"
                              f"<b>3 - tarif </b>\n{msg_3}\n",
                              reply_markup=markup)
    await call.message.delete()
    await SozlamalarStates.tarifni_almashtirish.set()


