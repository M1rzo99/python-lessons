#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 13:06:06 2026

@author: mirzo
"""

# Assalomalaykum Bugungi darsda pyhonda numberlarning qo'llanilishini o'rganamiz
# Butun sonlarni ham o'zgaruvchilarga saqlab,o'zgaruvchilar ustida amallarni bajarsak ham bo'ladi
a= 20
b = -10
c= a+b
print(c)

#Python - operatorlar orasidagi bo'shliqlarni inobatga olmaydi. O'qishga qulay bo'lishi uchun yuqoridagi kabi (bo'shliqlar bilan) yozishingiz mumkin.
kvadrat_tomoni = 20
kvadrat_yuzi = kvadrat_tomoni**2
print(kvadrat_yuzi)

# Pythonda 10 lik sonlar floating points number yoki "floats" ddi.
# Ingliz tilida o'nlik sonlarni ajratishda vegul(,) emas nuqta (.) bilan ajratiladi

pi = 3.14159 # O'nlik son(float)
radius = 10 # birlik son(integer)
diameter = 2 * radius

print("aylana uzunligi", pi * diameter, "ga teng")

# ikkita butun sonni bo'lsak, o'nlik son hosil bo'ladi
s = 20
e = 5
d = s/e
print(d) # javob 4.0 bo'ladi

# Butun va o'nlik sonlar orasidag amallar natijasi ham o'nlik sonlar natijasiga teng
u = 10
g = 2.5

print(u+g) # 12.5
print(u*g) # 25.0
print(u**g) #316.227
print(2*(u+g)) #25.0

# Uzun sonlarni kiritishda (million,billon) (_) chiziq orqali ajratsak bo'ladi. Pythonda (_) chiziqni inobatga olmasdan butun sonligicha qabul qiladi

aholsi_sioni = 8_234_978_456 # O'zimizga qulay bo'lgani un shunday yozdik, lekin python buni 8234978456 shaklida qabul qiladi
print("Yer kurrasida", aholsi_sioni,"ga yaqin odamlar Yashaydi.")

# Aksar dasturlash tillarida Constata(0'zgarmas) tushunchasi bor.Bunga P(3.14) qiymatini keltirsak bo'ladi. Lekin Pythonda Constanta tushunchasi yo'q. Agar biz o'zgarmas yaratmoqchi bo'lsak, O'zgaruvchini katta harflar bilan yozsak bo'ladi, va boshqa dasturchilar buni tushunishadi
PI = 3.14159
radiyus = 123345

# Birdaniga bir-nechta o'zgaruvchiga qiyma bermoqchi bo'lsak, ularga mos qiymatlar vergul orqali ajrayilinadi
e,r,t = 3,8,9
print(e,r,t)  # e=3,r=8,t=9

# O'zgaruvchilar turini almashtirish.

# "Men 27 yoshdaman" deyish un, 27 yoshni typeni intjer dan stringga o'tirish kerak
#ism = "Mirzo"
#yosh = 27
#xabar = ism + " " + yosh, "yoshdaman"
#print(xabar)
# tepadagi holatda xatolik kelib chiqadi.chunki type lari to'g'ri kelmagani uchun.

# biz bir turdagi o'zgarisharni boshqa turdagi o'zgaruvchiarga o'tkaza olamiz.bu jarayonni "typecasting" demiz.

# str() - int/float trudagi o'zgaruvchilarni, string(matn) ga o'zgartiradi
# int() - matn/ float ko'rinishidgi qiymatlarni butun songa o'zgartiradi. Bunday holatda matn butun son ko'rinishida bo'lishi kk(12.5) emas!
# float() - matn yoki int ko'rinishidagi qiymatlarni o'nlik sanoqga o'tkazadi.
# float()  - 10.9 , 2.5 butunli sonlarg 

# str()
#ism = "Mirzo"
#yosh = 27
#xabar = ism + ' ' + str(yosh) + 'yoshdaman'
#print(xabar)

# int(), ism ning typi string edi, ing orqali int ga o'zgartirdik
#ism = "13"
#yosh = 27
#xabar = int(ism) + yosh 
#print(xabar)

# float()
#ism = float( "13.2")
#yosh = 27
#xabar = int(ism) + yosh 
#print(xabar)

# Input va sonlar. Bu yerda foydalanuvchi kiritgan son aslida string bolardi, int orqali numberga o'zgartirdik.
# Va yosh orqali num - num bo'ldi
# natijani string ko'rinishida chiqarish kkligi un, num ni stringga o'zgartirdik
#t_yil = int(input("tug'ilgan kuningizni kiriting: "))
#yosh = 2026 - t_yil
#print("Siz"+ ' ' + str(yosh) +' '+  "yosh ekansiz")


# Amaliyot
#son = int(input("Istalgan sonni kiriting: "))
#natija = son**2
#print( str(son) + ' ' + "ning kvadrati" + ' '+ str(natija) + ' '+ "ga teng")

#son = int(input("Istalgan sonni kiriting: "))
#natija = son * (son**2)
#print( str(son) + ' ' + "ning qubi" + ' '+ str(natija) + ' '+ "ga teng")

#t_yosh = int(input("Yoshingizni kiriting: "))
#yosh = 2026 - t_yosh
#print("Siz"+ ' ' + str(yosh) +' '+  "yil tug'ilgan ekansiz")

br_son = int(input("Birinchi sonni kiriting: "))
ikki_son = int(input("Ikkinchi sonni kiriting: "))

yigindi1 = br_son +  ikki_son
yigindi2 = br_son *  ikki_son
yigindi3 = br_son -  ikki_son
yigindi4 = br_son /  ikki_son

print("ikkison qo'shilgan qiymat: " + str(yigindi1))
print("ikkison ko'paytirgandagi qiymat: " + str(yigindi2))
print("ikkison ayirgandagi qiymat: " + str(yigindi3))
print("ikkison bo'lgandagi qiymat: " + str(yigindi4))







 
