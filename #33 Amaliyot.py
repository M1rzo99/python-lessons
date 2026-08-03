#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 17:06:52 2026

@author: abcd
"""

#1.  Bugun o'rgangan narsalaringizni matnga yozing va matnni Python yordamida oching.
with open("amaliyot.txt") as file:
    info = file.read()
print(info)

#3. Sizning tug'ilgan kuningiz  π soni tarkibida uchraydimi yoki yo'q ekanligini aniqlovchi funksiya yozing. Misol uchun, tug'ilgan sanangiz 25 Fevral, 2000-yil bo'lsa, 25022000 ketma-ketligi yuqoridagi matnda uchraydimi yo'q toping.

# def pi_tekshir(sana):
#     with open("pi_million_digits.txt") as file:
#         pi = file.read().replace("\n", "")

#     if sana in pi:
#         return "Topildi ✅"
#     else:
#         return "Topilmadi ❌"


# Misol
#tugilgan_sana = input("Tug'ilgan sanangizni DDMMYYYY ko'rinishida kiriting: ")
#print(pi_tekshir(tugilgan_sana))


#4.Fayl ichidagi matnni float ma'lumot turiga o'tkazing va pickle yordamida yangi faylga saqlang.

import pickle

with open("pi.txt") as file:
    pi = float(file.read().replace("\n", ""))

with open("pi.dat", "wb") as file:
    pickle.dump(pi, file)

with open("pi.dat", "rb") as file:
    yangi_pi = pickle.load(file)

print(yangi_pi)
print(type(yangi_pi))
   

#5.Foydalanuvchidan turli hil ma'lumotlarni so'rab, har bir kiritilgan ma'lumotni yangi qatordan faylga yozib boruvchi dastur tuzing. Dastur qayta chaqirilganida yangi ma'lumotlar fayl oxiridan qo'shilib borsin (yangi faylga emas). 
malumot = input("Ism va familiyangizni kiriting: ")
with open("info.txt", "a") as fayl:
    fayl.write(malumot + "\n")

print("Ma'lumot saqlandi.")

with open("info.txt") as file:
    allInfo = file.read()
print(allInfo)
    
    
    