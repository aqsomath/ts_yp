from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from keyboards.inline.yolovchi.callback_data import viloyatlar_callback

viloyat = {
    "Andijon":"jonn",
    "Namangan":"gann",
    "Farg'ona":"onaa",
    "Buxoro":"oroo",
    "Toshkent":"kentt",
    "Sirdaryo":"ryoo",
    "Surxondaryo":"xonn",
    "Qashqadaryo":"qadaryyy",
    "Xorazm":"azmm",
    "Navoiy":"voyy",
    "Jizzax":"zzax",
    "Samarqand":"marqa",
    "Toshkent shahar":"kent shahar",
    "Qoraqalpog'iston":"qoraqalpoq",
    "Ortga":"nazad",
}
viloyatlar = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat.items():
    viloyatlar.insert(InlineKeyboardButton(text=key, callback_data=viloyatlar_callback.new(item_name=value)))


vili_callback=CallbackData("vili","item_name")
viloyat = {
    "Andijon":"andijon",
    "Namangan":"namangan",
    "Farg'ona":"farg'ona",
    "Buxoro":"buxoro",
    "Toshkent":"toshkent",
    "Sirdaryo":"sirdaryo",
    "Surxondaryo":"surxondaryo",
    "Qashqadaryo":"qashqadaryo",
    "Xorazm":"xorazm",
    "Navoiy":"navoiy",
    "Jizzax":"jizzax",
    "Samarqand":"samarqand",
    "Toshkent shahar":"kent shahar",
    "Qoraqalpog'iston":"qoraqalpoq",
}

viloyatlar_yol = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat.items():
    viloyatlar_yol.insert(InlineKeyboardButton(text=key, callback_data=value))

viloyatlar_yol.insert(InlineKeyboardButton(text='Buyurtmani bekor qilish',callback_data='Bosh menu'))
viloyatlar_yol.insert(InlineKeyboardButton(text='ortga',callback_data='ortga'))



viloyat_x = {
    "Andijon":"sjduuwgfuwgdkgjda",
    "Namangan":"akilwyiwefsdjksd",
    "Farg'ona":"kdjhaigdakhdksa",
    "Buxoro":"allaskalkdaslkjd",
    "Toshkent":"euywiudhkns",
    "Sirdaryo":"jweytfugdiahjash",
    "Surxondaryo":"qdwqwdqwsasxa",
    "Qashqadaryo":"asasdsadasd",
    "Xorazm":"dfdsfdsgfdsfgfd",
    "Navoiy":"fghgfjghjgfh",
    "Jizzax":"reggfvdvdvcx",
    "Samarqand":"tyhjyjghfh",
    "Qoraqalpog'iston":"qoraqalpoq",
    "Ortga":"homeback",
    "Buyurtmani bekor qilish":"atmen",
}

viloyatlar_yol_x = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat_x.items():
    viloyatlar_yol_x.insert(InlineKeyboardButton(text=key, callback_data=value))



viloyat_y = {
    "Andijon":"x656565_sjduuwgfuwgdkgjda",
    "Namangan":"x656565_akilwyiwefsdjksd",
    "Farg'ona":"x656565_kdjhaigdakhdksa",
    "Buxoro":"x656565_allaskalkdaslkjd",
    "Toshkent":"x656565_euywiudhkns",
    "Sirdaryo":"x656565_jweytfugdiahjash",
    "Surxondaryo":"x656565_qdwqwdqwsasxa",
    "Qashqadaryo":"x656565_asasdsadasd",
    "Xorazm":"x656565_dfdsfdsgfdsfgfd",
    "Navoiy":"x656565_fghgfjghjgfh",
    "Jizzax":"x656565_reggfvdvdvcx",
    "Samarqand":"x656565_tyhjyjghfh",
}
viloyatlar_yol_y = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat_y.items():
    viloyatlar_yol_y.insert(InlineKeyboardButton(text=key, callback_data=value))



viloyat_z = {
    "Andijon":"asas54_sjduuwgfuwgdkgjda",
    "Namangan":"asas54_akilwyiwefsdjksd",
    "Farg'ona":"asas54_kdjhaigdakhdksa",
    "Buxoro":"asas54_allaskalkdaslkjd",
    "Toshkent":"asas54_euywiudhkns",
    "Sirdaryo":"asas54_jweytfugdiahjash",
    "Surxondaryo":"asas54_qdwqwdqwsasxa",
    "Qashqadaryo":"asas54_asasdsadasd",
    "Xorazm":"asas54_dfdsfdsgfdsfgfd",
    "Navoiy":"asas54_fghgfjghjgfh",
    "Jizzax":"asas54_reggfvdvdvcx",
    "Samarqand":"asas54_tyhjyjghfh",
}

viloyatlar_yol_z = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat_z.items():
    viloyatlar_yol_z.insert(InlineKeyboardButton(text=key, callback_data=value))
    
    
    
viloyat_t = {
    "Andijon":"ddmm78_sjduuwgfuwgdkgjda",
    "Namangan":"ddmm78_akilwyiwefsdjksd",
    "Farg'ona":"ddmm78_kdjhaigdakhdksa",
    "Buxoro":"ddmm78_allaskalkdaslkjd",
    "Toshkent":"ddmm78_euywiudhkns",
    "Sirdaryo":"ddmm78_jweytfugdiahjash",
    "Surxondaryo":"ddmm78_qdwqwdqwsasxa",
    "Qashqadaryo":"ddmm78_asasdsadasd",
    "Xorazm":"ddmm78_dfdsfdsgfdsfgfd",
    "Navoiy":"ddmm78_fghgfjghjgfh",
    "Jizzax":"ddmm78_reggfvdvdvcx",
    "Samarqand":"ddmm78_tyhjyjghfh",
}

viloyatlar_yol_t = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat_t.items():
    viloyatlar_yol_t.insert(InlineKeyboardButton(text=key, callback_data=value))
    
    
    
    
    
viloyat_a = {
    "Andijon":"ekek46_sjduuwgfuwgdkgjda",
    "Namangan":"ekek46_akilwyiwefsdjksd",
    "Farg'ona":"ekek46_kdjhaigdakhdksa",
    "Buxoro":"ekek46_allaskalkdaslkjd",
    "Toshkent":"ekek46_euywiudhkns",
    "Sirdaryo":"ekek46_jweytfugdiahjash",
    "Surxondaryo":"ekek46_qdwqwdqwsasxa",
    "Qashqadaryo":"ekek46_asasdsadasd",
    "Xorazm":"ekek46_dfdsfdsgfdsfgfd",
    "Navoiy":"ekek46_fghgfjghjgfh",
    "Jizzax":"ekek46_reggfvdvdvcx",
    "Samarqand":"ekek46_tyhjyjghfh",
}

viloyatlar_yol_a = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat_a.items():
    viloyatlar_yol_a.insert(InlineKeyboardButton(text=key, callback_data=value))
    
    
    
viloyat_e = {
    "Andijon":"ekek12_sjduuwgfuwgdkgjda",
    "Namangan":"ekek12_akilwyiwefsdjksd",
    "Farg'ona":"ekek12_kdjhaigdakhdksa",
    "Buxoro":"ekek12_allaskalkdaslkjd",
    "Toshkent":"ekek12_euywiudhkns",
    "Sirdaryo":"ekek12_jweytfugdiahjash",
    "Surxondaryo":"ekek12_qdwqwdqwsasxa",
    "Qashqadaryo":"ekek12_asasdsadasd",
    "Xorazm":"ekek12_dfdsfdsgfdsfgfd",
    "Navoiy":"ekek12_fghgfjghjgfh",
    "Jizzax":"ekek12_reggfvdvdvcx",
    "Samarqand":"ekek12_tyhjyjghfh",
}

viloyatlar_yol_e = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat_e.items():
    viloyatlar_yol_e.insert(InlineKeyboardButton(text=key, callback_data=value))

viloyat_en = {
    "Andijon":"jonn",
    "Namangan":"gann",
    "Farg'ona":"onaa",
    "Buxoro":"oroo",
    "Toshkent":"kentt",
    "Sirdaryo":"ryoo",
    "Surxondaryo":"xonn",
    "Qashqadaryo":"qadaryyy",
    "Xorazm":"azmm",
    "Navoiy":"voyy",
    "Jizzax":"zzax",
    "Samarqand":"marqa",
    "Toshkent shahar":"kent shahar",
    "Qoraqalpog'iston":"qoraqalpoq",
    "Yakunlash":"yakunlash",
    "Ortga":"nazad",
}
viloyatlar_eng_birinchi = InlineKeyboardMarkup(row_width=2)
for key,value in viloyat_en.items():
    viloyatlar_eng_birinchi.insert(InlineKeyboardButton(text=key, callback_data=viloyatlar_callback.new(item_name=value)))