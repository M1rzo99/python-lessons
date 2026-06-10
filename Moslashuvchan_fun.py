#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:05:52 2026

@author: mirzo
"""

MOSLASHUVCHAN FUNKSIYA
Agar funksiyangiz bir nechta argument qabul qilishi kerak bo'lsa-yu, lekin siz argumentlar sonini aniq bilmasangiz, Pythonda istalgancha qiymat qabul qiluvchi funksiya yaratish imkoniyati bor. 
*args USULI
Agar funksiya qabul qiladigan parametrlar soni noaniq bo'lsa, va parametrlar yagona qiymatlar ko'rinishida uzatilsa, funksiya yaratishda argumentdan avval yulduzcha qo'yiladi (*arguments). 
Quyidagi misolni ko'raylik. summa() nomli funksiyamiz istalgancha sonlarni qabul qilib oladi, va ularning yi'gindisi hisoblaydi:

Copy
def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi
Bu funksiyani istalgancha parametr bilan chaqirish mumkin:

Copy
print(summa(1,2))
Natija: 3

Copy
print(summa(1,2,3,4,5))
Natija: 15
*args usulida, bacha uzatilgan parametrlar (bir dona bo'lsa ham) funksiya ichida o'zgarmas ro'yxatga (tuple) joylanadi. Bundan kelib chiqib, yuqoridagi funksiyamizni yanada soddalashtirib yozishimiz mumkin:

Copy
def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return sum(sonlar)

print(summa(4,5,6,7))
Natija: 22
Agar funksiya bir nechta argument qabul qilsa, *args argument doim oxirida yoziladi:

Copy
def summa(x,y,*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return x+y+sum(sonlar)
Yuqoridagi funksiyamiz kamida 2 ta parametr qabul qiladi (x va y) va birinchi ikki argumentlar majburiy argumentlardir.

Copy
print(summa(2))
Netija: TypeError: summa() missing 1 required positional argument: 'y'