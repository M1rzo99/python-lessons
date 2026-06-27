#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 20:31:24 2026

@author: mirzo
"""

# 23.Modullar

# Functionni qulayliklaridna biri - ko'p takrorlanadigan kodlarni function ichiga yashirishimizva kerak bo'lganda murojat qilishiumiz mumkinligida.
# Maqsad dasturimizni ihcham va tushunarli qilib,kelajakda o'zimiz va boshqalar un toza kod qoldirishimiz.

# Modul bu - loyihamiz ichidagi alohida fayl bo'lib, dasturiumiz davomida ishlatilinadigan fayllarni va o'garuvchilarni manashu faylga joylab. ko'zdan yashirib qo'yishimiz mumkin.
# Bu bizga asosiy dasturimizdan chalg'imasdan kod yozish imkonini beradi.

# Modul yaratish un asosiy dasturiumizdagi functionlarni yangi faylga ko'chiramiz xolos.Modulga oson murojat qilishimiz un, faylimiz asosiy dastur bn bitta papkada bo'lgani avfzal.
# Bunda adashib ketmaslik un loyihaning asosiy faylinii main.py deb noimlash o'rinli

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
    avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting",end='')
        kompaniya=input("Ishlab chiqaruvchi: ")
        model=input("Modeli: ")
        rangi=input("Rangi: ")
        korobka=input("Korobka: ")
        yili=input("Ishlab chiqarilgan yili: ")
        narhi=input("Narhi: ")    
        #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
        #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))    
        # Yana avto qo'shish-qo'shmaslikni so'raymiz
        javob = input("Yana avto qo'shasizmi? (yes/no): ")
        if javob=='no':
            break
    return avtolar

def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narh']}$")
    

    
    
  #MODULDA O'ZGARUVCHI SAQLASH
Modullarning ichida nafaqat funksiyalar, balki turli o'zgaruvchilarni ham saqlash mumkin. Modul ichidagi o'zgaruvchilarga ham huddi yuqoridagi usullar bilan murojat qilish mumkin.
PYTHON MODULLARI
Python dasturlash tili tayyor modullar bilan keladi, modullarning to'liq ro'yxatini quyidagi bo'glama orqali kirib ko'rishingiz mumkin:
Logo
Python Module Index — Python 3.14.6 documentation
docs.python.org
Keling ulardan ba'zilari bilan tanishamiz.
math MODULI
Bu modulda matematik hisob kitoblarni bajaruvchi funksiyalar va o'zgaruvchilar joylashgan. Keling ularga ba'zi misollarni ko'ramiz.
sqrt() - qavs ichida berilgan qiymatning kvadrat ildizini qaytaradi

Copy
import math

x=400
print(math.sqrt(x))
Natija: 20.0
pow(x,y) - x ning y-darajasini qaytaradi

Copy
print(pow(5,5))
Natija: 3125
pi - 
π
π ning qiymatini saqlovchi o'zgaruvchi

Copy
from math import pi
print(pi)
Natija: 3.141592653589793
log2(x) va log10(x) - x ning 2 va 10-lik logorifmini qaytaruvchi funksiyalar

Copy
print(math.log2(8))
print(math.log10(100))

    
#math ichidagi ayrim funksiyalar

Funksiya
Funksiya ta'rifi
ceil(x)
x dan katta yoki teng bo'lgan eng kichik butun sonni qaytaradi
fabs(x)
x ning absolyut qiymatini qaytaradi
floor(x)
x dan kichik yoki teng bo'lgan eng yaqin butun sonni qaytaradi
exp(x)
x
e
x 
e
  ni qaytaruvchi funksiya
cos(x)
cos
⁡
(
x
)
cos(x) ni qaytaruvchi funksiya
sin(x)
sin
⁡
(
x
)
sin(x) ni qaytaruvchi funksiya
tan(x)
tan
⁡
(
x
)
tan(x) ni qaytaruvchi funksiya
degrees(x)
x burchakning radian qiymatini darajaga konvertasiya qilish
radians(x)
x burchakning daraja qiymatini radianga konvertasiya qilish 
e
Matematik konstanta 
e
e (2.71828...)
math moduli ichidagi barcha funksiyalar bilan Pythonning rasmiy sahifasida tanishishingiz mumkin.
random MODULI
Random moduli tasodifiy sonlar bilan ishlash uchun qulay funksiyalarga boy. Keing ulardan ayrimlari bilan tanishamiz.


# randint(a,b)
Bu funksiya a va b oraligi'da tasodifiy butun son qaytaradi. 

Copy
import random as r # random modulini r deb chaqirayapmiz

son = r.randint(0,100) # 0 va 100 oralig'ida tasodifiy son
print(son)


#choice(x)
x ning ichidan tasodifiy qiymatni qaytaruvchi funksiya. Bunda x bir necha elementdan iborat o'zgaruvchi (matn, ro'yxat) bo'lishi kerak.

Copy
ismlar = ['olim','anvar','hasan','husan']
ism = r.choice(ismlar) # ismlar dan tasodifiy ism tanlaymiz
print(ism)
print(r.choice(ism)) # ismdan tasodifiy harf tanlaymiz

Natija

Copy
x = list(range(0,51,5))
print(x)
print(r.choice(x))

 #shuffle(x)
x ichidagi elementlarni tasodifiy tartibda qaytaruvchi funksiya. Bunda x bir necha elementdan iborat o'zgaruvchi (matn, ro'yxat) bo'lishi kerak.

Copy
x = list(range(11))
print(x)
r.shuffle(x)
print(x)

Natija
random moduli ichidagi boshqa funksiyalar haqida Python rasmiy sahifasidan ma'lumot olishingiz mumkin.


