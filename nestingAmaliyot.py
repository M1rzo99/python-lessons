#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:39:40 2026

@author: mirzo
"""

#1.Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
adabiyot_shaxs0 = {
    "ism": "Abu Abdulloh Muhammadm Ibn Ismoil",
    "yili":810,
    "manzil":"Buxoro",
    "ko'rgan_umri":60,
    "asarlari":"Al-jome' as-sahih ,Al-adab al-mufrad, At-tarix al-kabir,At-tarix as-sag'ir"
    }
adabiyot_shaxs1 = {
    "ism": "Abdulla Qodiriy",
    "yili":1894,
    "manzil":"Toshkent",
    "ko'rgan_umri":44,
    "asarlari":"O'tgan kunar, Mehrobdan Chayon, Obid Ketmon"
    
    }
adabiyot_shaxs2 = {
    "ism": "Erkin Vohidov",
    "yili":1936,
    "manzil":"Farg'ona",
    "ko'rgan_umri":80,
    "asarlari":"Tong Nafasi,Qo'shiqlarim Sizga,O'zbegim, Qiziquchan Matmusa"
    
    }
adabiyot_shaxs3 = {
    "ism": "Alisher Navoiy",
    "yili":1441,
    "manzil":"Xirot",
    "ko'rgan_umri":60,
    "asarlari":"Xamsa,Lison ut-Tayr, Mahbub Al-Qulb"
    }
adabiyot_shaxslar = [adabiyot_shaxs0,adabiyot_shaxs1,adabiyot_shaxs2,adabiyot_shaxs2]

for n in adabiyot_shaxslar:
    print(f"{n['ism']},{n['yili']} yili, {n['manzil']} tug'ilgan.{n['ko\'rgan_umri']} yil umr ko'rganlar.")

#2.Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
for n in adabiyot_shaxslar:
    print(f"{n['ism']} ning mashxur asarlari:")
    print(f"{n['asarlari']}\n")

#3.Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.
kinolar={
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }
    
for iss,kinolar in kinolar.items():
    print(f"\n{iss} ning sevimli kinolari:")
    for kino in kinolar:
        print(kino)

#3.Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.

davlatlar = {
    "Uzbekistan":{
        "poytaxt":"toshkent",
        "hududi":"448978 kv.km",
        "aholisi":39000000,
        "pul birliogi":"so'm"
        },
    "Russia":{
        "poytaxt":"moskva",
        "hududi":"17098246kv.km",
        "aholisi":144000000,
        "pul birliogi":"rubl"
        },
    "AQSH":{
        "poytaxt":"Vashington",
        "hududi":"9631418kv.km",
        "aholisi":327000000,
        "pul birliogi":"dollar"
        },
    "Malaysia":{
        "poytaxt":"Kuala-Lampur",
        "hududi":"329750kv.km",
        "aholisi":25000000,
        "pul birliogi":"rinnigit"
        }
    }


#for dav_n,davlatm in davlatlar.items():
  #  print(
 #       f"{dav_n} ning poytaxti {davlatm["poytaxt"].title()}"
 #       f"\nHududi:{davlatm["hududi"]}"
  #      f"\nAholisi:{davlatm["aholisi"]}"
  #      f"\nPul birligi:{davlatm["pul birliogi"]}\n"
   #     )
    
#4.Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
dav = input("Davlat nomini kiriting:")

if dav in davlatlar: 
        davlat = davlatlar[dav]
        print(
        f"\n{dav} ning poytaxti {davlat["poytaxt"].title()}"
        f"\nHududi:{davlat["hududi"]}"
        f"\nAholisi:{davlat["aholisi"]}"
        f"\nPul birligi:{davlat["pul birliogi"]}\n"
        )
else:
        print("Bizda bu davlat haqida ma'lumot yo'q!")











