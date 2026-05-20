#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:00:37 2026

@author: mirzo
"""

# Lug'atlar bilan ishlash
talaba_0 = {
    "ism":"Mirzo",
    "familiya":"Shomuratov",
    "yosh":27,
    "fakultet":"Computer Science",
    "holat":"Gradueted"
    }

#1. items() metofini  ishlatamiz.
# items() - elementlar degan manoni bildiradi. Va bizni o'zgaruvchimizda bor elementlarni ko'rsatadi\
# for sikli orqali esa kalit sozni  va qiymatni chiroyli tartibta tartiblashimiz mumkin.
print(talaba_0.items())
for kalit,qiymat in talaba_0.items():
    print(f"Kalit: {kalit}")
    print(f"qiymat: {qiymat}\n")

#telefonlar = {
 #   "ali": "iphone x",
 #   "vali":"galaxy s9",
 #   "olim":"mi 10 pro",
  #  "orif":"nokia 3110"
  #  }
for val,key in telefonlar.items():
    print(f"{val.title()} ning telefoni {key}.")

# keys () - methodi mahsulotlarni faqat key, (value ni emas) larnini olib beradi
mahsulotlar = {
    "olma":1000,
    "uzum":2000,
    "anor":3000,
    "nok":4000,
    'anjir':5000
    }
print(mahsulotlar.keys())

# keys() methodini ishlatmasak ham keylarimizni ko'ra olamiz
print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

# biz harid qilmoqchi bo'lgan mahsuloatlar do'konda bormi yoqmi tekshirsak bo'ladigan function
bozorlik = ['anor','uzum','shaftoli','qorali']
print("Sizning harid daftaringizdagi mahsulotlardan bizning do'konda shular bor xolos:")
for mah in mahsulotlar:
    if mah in bozorlik:
        print(f"{mah.title()} {mahsulotlar[mah]} so'm")
for mahs in mahsulotlar:
    if mahs not in bozorlik:
        print(f"Iltimos do'koningizga {mahs.title()} olib keling")
        

# Malumotlarin qanday ketma-ketlikda saqlasak,shunday holicha qoladi. agar u tartibsiz bo'lsa ham
# agar biz alifbo boyicha a dan z gacha sortlamoqchi bo'lsak, sorted() methodidan foydalanamiz
print("Masulotlarimiz A to Z ketma-ketligida")
for mahsu in sorted(mahsulotlar):
    print(mahsu)

# Ro'yhatdagi kalit(keys) emas, value(qiynatlarni) chiqarish teleb qilinishi mn
#shunda values() functionidan foydalanamiz
print("Mahsulotlarimiz:")
for  mahsul in mahsulotlar.values():
    print(mahsul)


print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
for tel in telefonlar.values():
    print(tel)
    
# set - methodi, ro'yhatda takrorlanib kelgan malumotlarni, takrorlanmagan holda ko'rsatadi
telefonlar = {
    "ali": "iphone x",
    "vali":"galaxy s9",
    "olim":"mi 10 pro",
    "orif":"nokia 3110",
    "Mirzo": "iphone x",
    "Nodir":"galaxy s9",
    "Nurik":"mi 10 pro",
    "Zafar":"nokia 3110"
    }
    
print("Foydalanuvchilar quyidagi tellerdan foydalanadi:")
for sort_tel in set(telefonlar.values()):
    print(sort_tel)
# yuqoirda bir xil value lar bir-necha bor takrorlanib kelgan,console.log da esa takrorlanib kelgan value lar tushib qolinadi
# set ichidagi malumotlar takrorlanmaydi:
toys = {"ball","car","lamp","ball","car"}
print(toys)
# sets ham malumot turi. set ham ichida malumotlar saqlash xususiyatiga ega.
# type(sets) orqali o'zgaruvchining malumot turini aniqlay olamiz
print(type(toys))
    
    
#amaliyot

anglar = {"qizil", "oq", "yashil"}
ranglar.add("sariq")
ranglar.update(["ko'k", "qora", "pushti"])

# Umumiy elementlar
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set1 & set2
print(set3)

# To'plamlar orasida farq
print(set1.difference(set2))
print(set2.difference(set1))

# Simmetrik farq
print(set1.symmetric_difference(set2))
    
    
    
    
    
    
    
    
