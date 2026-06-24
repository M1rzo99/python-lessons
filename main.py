#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:20:45 2026

@author: mirzo
"""

import Moduls # Moduls faylini chaqiramiz
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


# math MODULI
# Bu modulda matematik hisob kitoblarni bajaruvchi funksiyalar va o'zgaruvchilar joylashgan. Keling ularga ba'zi misollarni ko'ramiz.
# sqrt() - qavs ichida berilgan qiymatning kvadrat ildizini qaytaradi

# Copy
# import math

# x=400
# print(math.sqrt(x))
# Natija: 20.0
# pow(x,y) - x ning y-darajasini qaytaradi

# Copy
# print(pow(5,5))
# Natija: 3125
# pi - 
# π
# π ning qiymatini saqlovchi o'zgaruvchi

# Copy
# from math import pi
# print(pi)
# Natija: 3.141592653589793
# log2(x) va log10(x) - x ning 2 va 10-lik logorifmini qaytaruvchi funksiyalar

# Copy
# print(math.log2(8))
# print(math.log10(100))
# math ichidagi ayrim funksiyalar
# Funksiya
# Funksiya ta'rifi
# ceil(x)
# x dan katta yoki teng bo'lgan eng kichik butun sonni qaytaradi
# fabs(x)
# x ning absolyut qiymatini qaytaradi
# floor(x)
# x dan kichik yoki teng bo'lgan eng yaqin butun sonni qaytaradi
# exp(x)
# x
# e
# x 
# e
#   ni qaytaruvchi funksiya
# cos(x)
# cos
# ⁡
# (
# x
# )
# cos(x) ni qaytaruvchi funksiya
# sin(x)
# sin
# ⁡
# (
# x
# )
# sin(x) ni qaytaruvchi funksiya
# tan(x)
# tan
# ⁡
# (
# x
# )
# tan(x) ni qaytaruvchi funksiya
# degrees(x)
# x burchakning radian qiymatini darajaga konvertasiya qilish
# radians(x)
# x burchakning daraja qiymatini radianga konvertasiya qilish 
# e
# Matematik konstanta 
# e
# e (2.71828...)
# math moduli ichidagi barcha funksiyalar bilan Pythonning rasmiy sahifasida tanishishingiz mumkin.