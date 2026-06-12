#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 20:31:24 2026

@author: mirzo
"""

MODUL NIMA?
Funksiyaning qulayliklaridan biri, ko'p takrorlanadigan kodlarni funksiya ichida yashirishimiz va kerak bo'lgan murojat qilishimiz mumkinligida. Maqsadimiz dasturimizni ixcham va tushunarli qilib, kelajakda o'zimiz yoki boshqalar uchun ham "toza" kod qoldrisih. Bu yo'nalishda yana bir qadam qo'yib, dasturimizni modullarga ajratimshimiz mumkin. 
Modul bu loyihamiz ichidagi alohida fayl bo'lib, dasturimiz davomida ishlatiladigan funskyalarni (va o'zgaruvchilarni) mana shu faylga joylab, ko'zdan yashirib qo'yishimiz mumkin. Bu bizga asosiy dasturimizdan chalg'imasdan kod yozish imkoniyatini beradi. 
Modul va uning ichidagi funksiyalarni istalgan payt asosiy dasturimizga yuklab olishimiz, modullarni boshqa dasturchilar bilan ulashishimiz yoki kelajakda o'zimizning boshqa loyihalarimizda foydalanishimiz mumkin.
Umuman olganda katta dasturlar bir nech o'nlab modullardan iborat bo'lishi tabiiy hol.
MODUL YARATAMIZ
Modul yaratish uchun asosiy dasturimizdagi funksiyalarni yangi faylga ko'chiramiz xolos. Modulga oson murojat qilishimiz uchun, faylimiz asosiy dasturimiz bilan bitta papkada bo'lgani afzal. Bunda adashib ketmaslik uchun, loyihangizning (dasturning) asosiy faylini main.py deb nomlash o'rinli. 
Keling, biz ham avto_info_mod.py degan fayl yaratamiz va ichiga quyidagi 3 ta funksiyalarni joylaymiz:

Copy
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
Yuqoridagi funksiyalarga asosiy dasturdan murojat qlishning bir necha usuli bor.


**kwargs USULI
Agar funksiyaga kalit so'z - qiymat ko'rinishidagi argumentlarni uzatish talab qilinsa, va bunday parametrlar soni noma'lum bo'lsa, argument oldidan ikkita yulduzcha qo'yiladi (**kwargs).
**kwargs — keyword arguments (kalit so'zli argumentlar)

Copy
def avto_info(kompaniya,model,**malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar
Yuqoridagi funksiyamiz kompaniya va model degan ikki qiymatni qabul qiladi, undan keyin esa funksiyaga istalgancha parametr uzatish mumkin.  Bunday funksiyaga parametrlar kalitso'z=qiymat ko'rinishida uzatiladi.
Funksiya ichida avval foydalanuvchi kiritgan qo'shimcha qiymatlardan iborat malumotlar deb nomlangan lug'at shakllantiriladi. Undan keyin esa majburiy parametrlarni lug'atga qo'shamiz. 

Copy
avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)

Copy
print(avto2)
Natija: {'rang': 'qizil', 'narh': 35000, 'kompaniya': 'Kia', 'model': 'K5'}


AMALIYOT
Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.