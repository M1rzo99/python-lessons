#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:15:42 2026

@author: mirzo
"""

#  Ro'yhatlar va lug'atlar in while

# while yordamida ro'yhatni to'ldiramiz

#ismlar =[]
#print("Yaqin do'stlaringizni ro'yhatini shakllantiramiz.")
#n=1 #ismlarni sanash un o'zgaruvchi. (1- do'st,2- do'st)

#while True: # while abadiy aylanadi, qachonki break ga kelgunicha
#    savol = f"{n} - do'stingizni ismini kiriting:"
#    ism = input(savol)
#    ismlar.append(ism)
#    javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#    if javob == "ha":
 #       n +=1
 #       continue
 #   else:
 #       break
#print("Do'stlaringiz ro'yhati:")
#for ism in ismlar:
#    print(ism.title())

# dostlar = []
# print("Do'stlar ro'yhatini shakllantiradigan program")
# n=1
# while True:
#     sorov = f"{n} - Do'stingizni kiriting: "
#     in_sorov = input(sorov).lower().strip()
#     dostlar.append(in_sorov)
#     lib =  input("Yana do'st qo'shasizi? (yes/no): ")
#     if lib == "yes":
#         n +=1
#         continue
#     else:
#         break
    
# print("Do'stlariz ro'yhati: ")
# for sorov in dostlar:
#     print(sorov.title())
    
# while yordamida lugat(Dictionary) ni to'ldirish

# print("Dos'tlaringiz yoshini saqlaymiz")
# dostlar = {} # distionary(lugat) yaratmoqchi bo'lsak shunday usulda yaratamiz
# ishora = True
# n = 1
# while ishora:
#     ism = input(f"{n} - Do'stingizni ismini kiriting: ")
#     yosh = input(f"{ism.title()} ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh) # ism kalit, yosh value
#     n +=1 
#     javob = input("Yana do'stlar qo'shasimi? (yes/no)")
#     if javob == "no":
#         ishora = False
# for ism,yosh in dostlar.items():
#     print(f"{ism.title()}ning yoshi {yosh} yoshda")
    
# yuqoridagi kodeda ism = kalit, yosh = value, ishora = sikl qancha aylanishni belgilaydi

# remove(qiymat) - biz bergan qiymatni o'chirib beradi
# while orqali bizni shu nomdagi qancha element bo'lsa hammasini o'chiramz
# cars = ["lacetti","gentra","BWM","gentra","audi","gentra"]
# car_o = ["gentra","lacetti"]
# for car in car_o:
#         while car in cars:
#             cars.remove(car)
# print(cars)
# yuqoridagi tsiklda toki cars degan ro'yhatda biz bergan qiymat tugagunga qadar tugaydi

# Tasavvur qiling bizda 1 ro'yhat bor va uni ustida amallar bajarib, 2- ro'yhatga joylamoqchimiz. shu payt bizga while juda qo'l keladi
# quyidagi qo'yhatda,talabalar ro'yhati bor,talablar ro'yhati tugagunga qadar sikl aylanadi.pop() yordamida talabalarni sug'urib olamiz.

# talaba = ["Hasan","Husan","Ilxom","Jumadurdi","Tohir"]
# bah_talaba = {}
# while talaba:
#     talab = talaba.pop()
#     baho = input(f"{talab.title()} ning bahosini kiriting: ")
#     print(f"{talab.title()} baholandi")
#     bah_talaba[talab]= baho

# amalaiyot

#1. Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang

# print("Foydalanuvchidan buyurtma qabul qiladigan dastur")
# foy_royhat = []
# n=1
# while True:
#     intf = input(f"{n} - Nima buyurtma berasiz? ")
#     foy_royhat.append(intf)
#     yana = input("Yana buyurtma berasizmi? (yes/no)")
#     if yana == "yes":
#         n +=1
#         continue
#     else:
#         break
# print("Buyurtmalar ro'yhati: ")
# for intf in foy_royhat:
#     print(intf.title())

#2.e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
    
# print("Siz adminsiz, dasturga mahsulot va narh qo'sha olasiz!")
# foy_royhat = {}
# n=1
# while True:
#     intf = input(f"{n} - Nima mahsulot qo'shasiz? ")
#     intf_1 = input(f"{intf.title()} - narxini belgilang:  ")
#     intf_2 = int(intf_1)
#     foy_royhat[intf] = intf_2
#     yana = input("Yana mahsulot qo'shasizmi? (yes/no)")
#     if yana == "yes":
#         n +=1
#         continue
#     else:
#         break
    
# print("Mahsulotlar ro'yhati: ")
# for intf in foy_royhat:
#     print(f"{intf.title()}ning narhi - {intf_2} so'm")

#3.Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

# Tayyor e-bozor lug'ati
ebozor = {
    "olma": 5000,
    "non": 3000,
    "sut": 8000,
    "tuxum": 12000,
    "guruch": 15000
}

# Buyurtma qabul qilish
print("=== BUYURTMA ===")
buyurtma = []
n = 1
while True:
    mahsulot = input(f"{n} - Nima buyurtma berasiz? ").lower().strip()
    buyurtma.append(mahsulot)
    yana = input("Yana buyurtma berasizmi? (yes/no): ").lower().strip()
    if yana == "yes":
        n += 1
    else:
        break

# Narxlarni solishtirish
print("\n=== BUYURTMA NATIJASI ===")
jami = 0
for mahsulot in buyurtma:
    if mahsulot in ebozor:
        narh = ebozor[mahsulot]
        jami += narh
        print(f"{mahsulot.title()} — {narh} so'm")
    else:
        print(f"{mahsulot.title()} — Bizda bu mahsulot yo'q!")

print(f"\nJami to'lov: {jami} so'm")















    