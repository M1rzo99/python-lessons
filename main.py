#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:20:45 2026

@author: mirzo
"""

import Moduls #Moduls faylini chaqiramiz
avto1 = Moduls.avto_info("GYM", 'K5', "Oq", "avtomat", 2025,19000)
Moduls.info_print(avto1)

# MODULGA QISQA NOM BERISH
#Yuqoridagi usul bilan modulni chaqirib olishda fayl nomi uzun bo'lsa bu o'ziga yarasha noqulayliklar tug'dirishi mumkin. 
#Buning oldini olish uchun esa, modulni chaqirganda unga as operatori yordamida qisqa nom berishimiz, va modulga qisqa nom orqali murojat qilish mumkin. 
#Quyidagi misolda avto_info_mod ni qisqa qilib aim deb nomlab oldik, va 3-4-qatorlarda modulga murojat qilishda qisqa nomidan foydalandik.

import Moduls as aim # avto_info_mod ni qisqa nom aim bilan chaqiramiz

avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
aim.info_print(avto1)

#Modulga qisqa nom berganingizda bunday nomli boshqa o'zgaruvchi yoki funksiya yo'qligiga amin boling. 
#Shunigdek, dastur davomida bu nomni boshqa o'zgaruvchilarga yoki funksiylarga berib yubormang. 

#Modul ichidan malum bir funksiyalarni ko'chirib olish:
  
# Agar katta modullardan faqatgina bazi functsiyalarga murojat qilish talab qilinsa, kerakli funksiyalarni
# from module_nomi import func1,func2 komandasi yordamida o'zimizning dastruiimizga ko'chiirib olishimiz mumkin.Bu usulning qulayligi, endi funksiyalarga to'g'ridan to'g'ri murojat qilish mumkin(modul ismini yozmagan holdaa)

from Moduls import avto_info,info_print
avto2=avto_info("BYD","CHAMPION","Seliy","avtomat",2024,19000)
info_print(avto2)

# Funksiyalarga qisqa nom berish
# huddi avvalgidek, ko'chirib olgan functionimizga ham qisqa nom berishimiz mn
from Moduls import avto_info as aInfo, info_print as iPrint
avto3 = aInfo("Mirzo", "Jumong", "Oqrang", "Mexanik", 1999,20000)
iPrint(avto3)

# Modul ichidagi barcha funksiyalarni ko'chirib olish:
    
from Moduls import *
avto4 = avto_info("GT","Hummer","Black","avtomat",1999,43000)
info_print(avto4)

#Diqqat! Bu usuldan foydalanish bir nechta sabalarga ko'ra tavfsiya ertilmaydi. Katta modullarda yuzlab funksiyalar bo'lishi mn va funksiya nomi sizning dastruingizda boshqa  funksiya yoki o'zgaruvchi bilan bir xil nomga ega bo'lsa, dastur xato ishlashiga olib keladi

# Modulda o'zgruvchi saqlash

# Modullar ichida nafaqat o'zgaruvchilar,balki turli o'zgaruvchilarni ham saqlash mumkin.
# Modul ichidagi o'zgaruvchilarga ham yuqoridagi usullar bn murojat qilish mn.

# math Moduli:
# bu modulda matematik hisob kitoblarni bajaruvchi funkdiyalar va o'zgaruvchilar joylashgan.Keling ularga bazi misollarni ko'ramz
#1. sqrt()  - qavs ichidagi qiymatning kvadrat ildizi qaytarilinadi.
import math
x=200
print(math.sqrt(x))
 
#2. pow(x,y) - x ning y- darajasini qaytaradi.
print(pow(2,3))


#3. pi -ㅍ ning qiymarini saqlovchi o'zgaruvchi
from math import pi
print(pi)

#4.log2(x) va log10(x)  - x ning 2 va 10lik logarifimioni qaytaruvchi functionlar
print(math.log2(8))
print(math.log10(100))

# random Moduli

#Random Moduli tasodifiy sonlar bn ishlash un qulay functionlarga boy. Keling ularni ayrimlari bn tanishamiz


# randit(a,b) - a va b oraligi'idagi tasodifiy butun son qaytaradi.
import random as r # random Modulini r deb  chaqiramiz
son =r.randint(0,100) # 0 va  100 oralig'idagi tasodifiy son
print(son) # har safar son o'zgaruvchisi chaqirilinganda, random son hosil bo'ladi.































