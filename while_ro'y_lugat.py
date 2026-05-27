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
cars = ["lacetti","gentra","BWM","gentra","audi","gentra"]
car_o = ["gentra","lacetti"]
for car in car_o:
        while car in cars:
            cars.remove(car)
print(cars)
# yuqoridagi tsiklda toki cars degan ro'yhatda biz bergan qiymat tugagunga qadar tugaydi

# Tasavvur qiling bizda 1 ro'yhat bor va uni ustida amallar bajarib, 2- ro'yhatga joylamoqchimiz. shu payt bizga while juda qo'l keladi
# quyidagi qo'yhatda,talabalar ro'yhati bor,talablar ro'yhati tugagunga qadar sikl aylanadi.pop() yordamida talabalarni sug'urib olamiz.

talaba = ["Hasan","Husan","Ilxom","Jumadurdi","Tohir"]
bah_talaba = {}
while talaba:
    talab = talaba.pop()
    baho = input(f"{talab.title()} ning bahosini kiriting: ")
    print(f"{talab.title()} baholandi")
    bah_talaba[talab]= baho










    