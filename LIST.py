#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:03:57 2026

# List

@author: mirzo

"""

mevalar = ["o'rik","olma","behi","uzum"]
sonlar = [12000,34000,45000,67000]
son_harf = [21,34,"Mirzo","uzum",-45]
bosh = [ ]

# append() orqali ro'yhatni ohiriga qiymat qo'shishimiz mn
#mevalar.append("nok")
#print(mevalar)
#mevalar.append("piyoz")
#print(mevalar)

# insert(ind,obj) orqali o'zmiz istagan indexga qiymat qo'sha olamiz
mevalar.insert(0, "banan")
print(mevalar)
mevalar.insert(2, "tannasgul")
print(mevalar)

# Bo'sh royhat yaratamiz va append() orqali ro'yhatga object qo'shamiz
cars = []
cars.append("porsche")
cars.append("kia")
cars.append("malibu")
cars.append("GPT")
print(cars)

# del orqali bizga kerak bo'lmagan objectni o'chiirb tashlask bo'ladi
del cars[0]
print(cars)

# agarda objectni indexini bilmaymiz,faqat obj nomini bilamiz.Va shu objectni ro'yhatdan o'chirmoqci bo'lsak remove orqali o'chirishimiz mn
# ro'yhatimizda bir nechta bir xil objlar bor, ularni remove orqali o'chirmoqchi bo'lsak, faqat birinchi turgan obj ni o'chira olamiz xolos.
cars.remove("GPT")
print(cars)

# bizda list bor va shu listdan biror obj ni olib, boshqa o'zgaruvchi qiymatiga beramiz.va kk joyda ishlatishimz mn
# .pop(idx) orqali

mahsulot = mevalar.pop(0)
print(mahsulot)

print("Men" + " " ,mahsulot + " " + "Sotib oldim")
print("Sotib olinmagan mahsulotlar" + " ", mevalar, " " + "qoldi")

# agarda pop() ga idx bermasak, listdagi oxirgi qiymatni oladi




# Amaliyot 1
dostlarim = ["Munis","Aziz","Abbos"]
print("Salom" + " " + dostlarim[2] + " " + "bugun choyxona bormi? Yoki" + " " + dostlarim[0] + " " + " biladimi?")

# Amaliyot 2
sonlar = [12,10,23,20,50,67]
print(sonlar[3] - sonlar[2])
print(sonlar[3] / sonlar[2])
print(sonlar[3] + sonlar[2])
print(sonlar[1] * sonlar[2])

sonlar.remove(12)
print(sonlar)
del sonlar[0]
print(sonlar)

# pop() orqali olmoqchi bo'lgan qiymatni o'zgaruvchiga beramiz va pop() dagi qiymat o'zgaruvchiga biriktiriladi
mah = sonlar.pop()
print(mah)

# Amaliyot 3. O'zgaruvchi yaratib, append(0) orqali o'zgaruvchiga qiymat qo'shish

t_shaxslar = []
z_shaxslar = []

t_shaxslar.append("Shay MuhammadSodiq-MuhammadYusuf")
t_shaxslar.append("Al-Xorazmiy")

z_shaxslar.append("Sultonov Maqsudbek")
z_shaxslar.append("Saparova Hamidaxon")
print(t_shaxslar)
print(z_shaxslar)

qiy1 = z_shaxslar.pop(0)
qiy2 = t_shaxslar.pop(0)
print("Men istardimki" + " " + qiy1 + " " + " bilan" + " " +  qiy2 + " " + "suhbat qurishlarini")

# Amaliyot 4
friends = []
friends.append("Nodir")
friends.append("Nurik")
friends.append("Daston")
friends.append("Haima")
friends.append("Ilmira")

#friends.remove("Daston")
#friends.remove("Haima")

kel_1 = friends.pop(2)
kel_2 = friends.pop(3)

print("Bugungi tadbirga ", kel_1 , "va " + " ", kel_2,"lar kelmadi" )










