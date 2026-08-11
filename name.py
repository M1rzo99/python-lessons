# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Mon Aug 10 22:17:10 2026

# @author: mirzo
# """

# # Dastur davomida yangi funksiya yoki klass yozar ekanmiz, ularni to'g'ri ishlashini ham tekshirishimiz tabiiy. Kodni tekshirish, kelajakda dasturimiz xato ishlashining oldini oladi. Odatda, funksiya va klasslarni tekshirish uchun alohida test dasturlar yozishimiz mumkin. Bunday dasturlar funksiyaga turli parametrlar orqali murojat qilib, undan qaytgan qiymatlar to'g'ri yoki xato ekanini tekshiradi. 
# # Pythonda bu jarayonni osonlashtirish uchun maxsus unittest moduli mavjud. unittest yordamida alohida funksiya, obyekt yoki butun boshli modulni ham tekshirshimiz mumkin. Lekin, tavsiya qilingan usuli bu testni dastavval kichik qismlardan boshlab, kengaytirib borish. 

# Boshlanishiga biror sodda funksiya yozamiz. Quyidagi funksiya foydalanuvchi ismi va familiyasini qabul qiladi, va ism familiyani jamlab qaytaradi:
# def get_full_name(ism, familiya, otasi=''):
#     if otasi:
#         return f"{ism} {otasi} {familiya}".title()   
#     else:
#         return f"{ism} {familiya}".title()


# def get_fam(mo,fa,sis,bro):
#     return f"{mo},{fa},{sis},{bro}"
# print(get_fam("hamida","maqsud","iroda","latif"))

# Sonlarni tekshirish

