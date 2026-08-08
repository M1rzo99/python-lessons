#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 21:59:45 2026

@author: mirzo
"""

#1.EXCEPTIONS
#Avvalgi darslarimizning birida biz "Run time error" xatoliklari bilan tanishgan edik. Bunday xatolar dastur bajarish jarayonida kelib chiqadi va dasturning ishlashini to'xtatadi. Sintaks xatolikdan farqli ravishda Python bunday xatolarni dasturni bajarishdan avval aniqlay olmaydi. 
#Ushbu darsimizda qanday qilib mana shunday xatoliklarni jilovlashni o'rganamiz. Maqsadimiz xatolik yuz berganda dastur to'xtab qolishining oldini olish. Gap shundaki, dastur davomida xato yuz berganda Python maxsus exception (istisno) obyektini yaratadi. Agar bu obyekt "tutib" olinmasa, dastur bajarilishdan to'xtaydi. 



#2.try-except
# Istisno obyektlarni tutib olish uchun Pythonda maxsus try-except operatorlari bor. Bu operatorlar quyidagicha ishlaydi, try operatori badanida bajarish kerak bo'lgan kod yoziladi, except operatori badanida esa xatolik yuz berganda bajarilishi kerak bo'lgan kod yoziladi. Ya'ni dasturimiz to'xtab qolmasdan bajarilaveradi. 
# Tushunarli bo'lishi uchun quyidagi misolni ko'ramiz. 

# Copy
# yosh = input("Yoshingizni kiriting: ")
# yosh = int(yosh)
# print(f"Siz {2021-yosh} yilda tug'ilgansiz")
# Yuqoridagi misolning 1-qatorida biz foydalanuvchidan yoshini kiritishni so'rayabmiz. Navbatdagi qatorda esa foydalanuvchi kiritgan qiymatni int() yordamida butun songa o'tkazayapmiz. Agar foydalanuvchi yoshini kiritganda, butun emas, o'nlik son kiritsa bu ValueError xatoligiga olib keladi, va dastur bajarilishdan to'xtaydi.

# Dastur natijasi
# Keling, yuqoridagi kodni try-except yordamida yozamiz:

# Copy
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)  
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz")  
# except:
#     print("Butun son kiritmadingiz")

# print("Dastur Tugadi!")
# Bu yerda ham dastavval foydalanuvchi yoshini so'radik. int() finksiyasini esa try badani ichida yozdik, agar foydalanuvchi to'gri qiymat kiritgan bo'lsa kodimiz foydalanuvchi tug'ilgan yilini hisoblab ko'rsatadi, exception (istisno) yuz berganda esa "Butun son kiritmadingiz" xabarini konsolga chiqaradi. Lekin dastur bajarilishdan to'xtamaydi, va try-except blokidan keyingi qatorlar ham bajarilaveradi (print("Dastur Tugadi!")). Buni quyidagi natijadan ham ko'rishimiz mumkin:

# Dastur natijasi
# try-except operatorining afzalliklaridan biri, foydalanuvchiga tushunarsiz xatolar o'rniga, o'zimiz istagan, tushunarliroq matnni ko'rsatishimiz mumkin. Shuningdek, kompleks tizimlarda arzimagan xatoni deb dasturimiz to'xtab qolmaydi.




#3.try-except-else
# Yuqoridagi kodimizda biz try moduli ichida xato qaytarishi mumkin bo'lgan ifodani ham (tyil = int(tyil)), xato qaytmaganda bajarilishi kerak bo'lgan ifodani ham (print(f"Siz {2021-tyil} yoshdasiz") ) birdan yozib ketayapmiz. Aslida, bunday qilishimiz to'g'ri emas. 
# To'g'ri usuli, bu avval xatoga tekshirish va xato yuz bermaganda bajariladigan ifodani alohida, else blokida yozish:

# Copy
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)    
# except:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz")
# Albatta, yuqoridagi usul har doim ham qo'l kelavermaydi.