#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 21:15:14 2026

@author: mirzo
"""


# Nesting - ro'yhatni ichida lug'atni saqlash yoki lug'atni ichida ro'yhatni saqlash

# Yuzlab lug'atlarni bitta listga joylab,ularni hoxlagan joyda kam code yozib foydalana olamiz
car0 = {
       'model':'audi',
       'rang':'qora',
       'yili':2025,
       'km':10,
       'narx':33000,
       'karobka':'avtomat'
       }
car1 = {
       'model':'bmw',
       'rang':'qora',
       'yili':2021,
       'km':9000,
       'narx':50000,
       'karobka':'avtomat'
       }
car2 = {
       'model':'damas',
       'rang':'oq',
       'yili':2023,
       'narx':10000,
       'km':321,
       'karobka':'avtomat'
       }

# agar biz oddiy yo'l bilan lug'atlarni print qilsak har bir valueni chaqirish kk bo'ladi
# bu jarayonni qisqartirish un esa, lug'atlarni bitta list ga joylab, list orqali chaqirishdir.
cars = [car0,car1,car2]
for car in cars:
    print(f"{car['model'].title()},"
          f"{car['rang'].title()},yili {car['yili']}"
          f" va {car['karobka'].title()}"
        )

# endi lug'atga index orqali ham murojat qilishimiz mn.Va lug'atdagi elementga pastdagidek murojat qilishimiz mn
print(cars[0]['km'])

# Pastda for tsikli yordamida lug'atlar yaratdik va unga qiymatlarni berib chiqdik
malibus = []
for n in range(10):
    new_car = {
        'model':'Gelik',
        'rang':None,
        'yili':2023,
        'narx':None,
        'km':321,
        'karobka':'avtomat'
        }
    malibus.append(new_car)


    

# Yuqoirda rang qismini ochiq qoldirganmiz vashularga rang bera oalmiz
for malibu in malibus[:3]:
    malibu['rang']='qora'
for malibu in malibus[3:6]:
    malibu['rang'] = 'qizil'
for malibu in malibus[6:]:
    malibu['rang'] = 'sariq'


for malibu in malibus[4:7]:
    malibu["karobka"]="mex"
# mashina karobkasi holatidan kelib chiqib narh berlgilaymiz
for malibu in malibus:
    if malibu['karobka']=='avtomat':
        malibu['narx'] = 50000
    else:
        malibu['narx'] = 70000
print(malibus)


# lug'at ichida ro'yhat
# bir kalitga bir nechta qiymat berish talab qilinganda, qiymatlarni ro'yhat ko'rinishda yozish o'rinlidir
dasturchilar = {
    "Mirzo":['Js','python'],
    "Nodir":['html','js','css'],
    "Nurik":['php','C++'],
    "Maryam":['django','go']
    }
for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:",end='')
    for til in tillar:
        # python functionda har bir matndan so'ng yangi qator tashalydi.Buni oldini olish un
        #print(string,end() methodidan foydalanishimz mumkin) 
        print(f"{til.upper()}\n")


# lug'at ichida lug'at

hamkasblar = {
    "ali":{'familya':"valiyev",
        "yili":1990,
        'malumoti':"oliy",
        'tillar':['python','js']
        },
    "vali":{'familya':"aliyev",
        "yili":2000,
        'malumoti':"oliy emas",
        'tillar':['Go','Django']
        }
    }


for ismm,info in hamkasblar.items():
    print(f"{ismm.title()} {info['familya'].title()},"
          f"{info['yili']}-yilda tug'ilgan."
          f"Ma'lumoti {info['malumoti'].title()},\n"
          "quyidagi dasturlash tilarni biladi:"
          )
    for til in info['tillar']:
        print(til.upper())




















