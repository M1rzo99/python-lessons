# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Mon Aug 10 22:17:10 2026

# @author: mirzo
# """

# # Dastur davomida yangi funksiya yoki klass yozar ekanmiz, ularni to'g'ri ishlashini ham tekshirishimiz tabiiy. Kodni tekshirish, kelajakda dasturimiz xato ishlashining oldini oladi. Odatda, funksiya va klasslarni tekshirish uchun alohida test dasturlar yozishimiz mumkin. Bunday dasturlar funksiyaga turli parametrlar orqali murojat qilib, undan qaytgan qiymatlar to'g'ri yoki xato ekanini tekshiradi. 
# # Pythonda bu jarayonni osonlashtirish uchun maxsus unittest moduli mavjud. unittest yordamida alohida funksiya, obyekt yoki butun boshli modulni ham tekshirshimiz mumkin. Lekin, tavsiya qilingan usuli bu testni dastavval kichik qismlardan boshlab, kengaytirib borish. 

# Boshlanishiga biror sodda funksiya yozamiz. Quyidagi funksiya foydalanuvchi ismi va familiyasini qabul qiladi, va ism familiyani jamlab qaytaradi:

# def get_full_name(ism, familiya):
#     return f"{ism} {familiya}".title()
# Funksiyani tekshiramiz:


# >>> print(get_full_name('alijon','valiyev'))
# 'Alijon Valiyev'
# Keling endi shu funksiyamizni tekshirish uchun dastur yozamiz. Bu yerda ikki narsaga ahamiyat beramiz: avvalo funksiyamizni alohida modulda saqlaymiz (name.py), ikkinchidan test dasturimizni ham alohida modulda yozamiz va unga ham tushunarli nom beramiz (masalan, name_test.py).
# Test faylimizning (name_test.py) tarkibi quyidagicha bo'ladi:


# import unittest
# from name import get_full_name

# class NameTest(unittest.TestCase):
#     def test_toliq_ism(self):
#         formatted_name = get_full_name('alijon','valiyev')        
#         self.assertEqual(formatted_name, 'Alijon Valiyev')

# unittest.main()
# Dasturni tahlil qilamiz:
# Dastavval unittest modulini chaqiramiz (import unittest)
# Keyingi qatorda name.py modulimizdan tekshirmoqchi bo'lgan funksiyamizni ham yuklab olamiz (get_full_name).
# 4-qatorda test klassini yaratamiz, bu klassunittest.TestCase klassidan meros oladi. Bu klass berilgan parametrlar uchun funksiyadan qaytgan qiymatlarni tekshirishga mo'ljallangan. Klassimizga o'zimiz istagan, tushunarli nom beramiz (NameTest). 
# Klassimiz ichida test_toliq_ism metodini yaratdik. Bu metod get_full_name funksiyasidan qaytgan qiymatni biz avvaldan bergan qiymatga teng yoki yo'q ekanini tekshiradi. Buning uchun esa maxsus .assertEqual() metodidan foydalandik. E'tibor bering, test medotlarning nomi har doim test so'zi bilan boshlanishi kerak.
# assertEqual() metodi ikki qiymat qabul qiladi va ularning teng ekanligini tekshiradi (assert ingliz tilidan tasdiqlash deb tarjima qilinadi). Agar get_full_name('alijon','valiyev') funksiyamiz to'g'ri ishlasa, funksiyadan 'Alijon Valiyev' qiymati qaytishi kerak. assertEqual() metodi aynan shuni tekshirishga mo'ljallangan.
# So'nggi qatorda unittest klassinini chaqiramiz, bu esa o'z navbatida biz yuqorida yozgan testni chaqiradi. 
# name_test.py dasturimizni bajaramiz va quyidagi natijani olamiz:


# Ran 1 test in 0.001s

# OK
# Natijadan bitta test bajarilganini va va bu test muvaffaqiyatli o'tganini (OK) ko'rishimiz mumkin.
# Keling endi dars boshida yaratilgan get_full_name funksiyamizga o'zgartirish kiritamiz:


# def get_full_name(ism, familiya, otasi=''):
#     if otasi:
#         return f"{ism} {otasi} {familiya}"   
#     else:
#         return f"{ism} {familiya}".title()
# Bu safar funksiyamiz otasining ismini ham qabul qiladi, lekin bu argument ixtiyoriy. 
# Testimizga ham o'zgartirish kiritamiz. Bu safar ikki hil ism uchun ikkita alohida test bajaramiz:


# import unittest
# from name import get_full_name

# class NameTest(unittest.TestCase):
#     def test_toliq_ism(self):
#         formatted_name = get_full_name('alijon','valiyev')        
#         self.assertEqual(formatted_name, 'Alijon Valiyev')
#     def test_toliq_ism_otasi(self):
#         name = get_full_name('hasan','husanov','olimovich')
#         self.assertEqual(name,'Hasan Olimovich Husanov')

# unittest.main()
# Testni bajaramiz, va quyidagi natijani olamiz:


# AssertionError: 'hasan olimovich husanov' != 'Hasan Olimovich Husanov'
# - hasan olimovich husanov
# ? ^     ^         ^
# + Hasan Olimovich Husanov
# ? ^     ^         ^


# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s

# FAILED (failures=1)
# Bu safar funksiyamiz 1 ta testdan yiqildi (failures=1). Biz kutgan natija (Hasan Olimovich Husanov) va funksiya qaytargan natija (hasan olimovich husanov) bir hil emas. Ya'ni, ism familiya va otasining ismi katta harflar bilan yozlishi kerak edi, lekin natija unday emas. Demak funksiyamizda xato bor. Xatoni to'g'rilaymiz:


# def get_full_name(ism, familiya, otasi=''):
#     if otasi:
#         return f"{ism} {otasi} {familiya}".title()   
#     else:
#         return f"{ism} {familiya}".title()
# Testni qaytadan chaqiramiz:


# Ran 2 tests in 0.001s

# OK
# Bu safar funksiyamiz  ikki testdan ham muvaffaqiyatli o'tdi.