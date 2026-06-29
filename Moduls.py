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
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
 