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

def pi_tekshir(sana):
    with open("pi_million_digits.txt") as file:
        pi = file.read().replace("\n", "")

    if sana in pi:
        return "Topildi ✅"
    else:
        return "Topilmadi ❌"


# Misol
tugilgan_sana = input("Tug'ilgan sanangizni DDMMYYYY ko'rinishida kiriting: ")
print(pi_tekshir(tugilgan_sana))

