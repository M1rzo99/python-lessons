#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 21:22:15 2026

@author: mirzo
"""

#lambda - YOHUD NOMSIZ FUNKSIYA
# Pythonning o'ziga xos xususiyatlaridan birin, nomsiz vaqtinchalik funksiyalar yaratish imkonidir.
# Bunday funksiyalarni yaratishda def operatori o'rniga lambda operatori ishlatilgani un ham lambda funksiyasi deb ataladi.

# Nomsiz funksiyalar quyidagicha yaratiladi:
lambda argument:ifoda

# Lambda funksiyasi istalgan miqdordagi argumentlarga ega bo'lishi mn, amma funksiya badanida faqat bitta ifoda mavjud bo'ladi.
# Ifoda bajarilinadi va qaytarilinadi, return operatori shart emas.

# Nomsiz funksiyalar biror ifodani tezda hisoblab olishda qulay. Misol un quyidagi lambda funksiya ikkita argument qabul qiladi(pi,r) va aylana uzunligini qaytaradi:
import math
uzunlik = lambda pi,r:2*pi*r
print(uzunlik(math.pi,10))

# Yana bir misol - x ning y nchi darajasi demakdir

product = lambda x,y: x**y
print(product(3,2))

# lambda funksiyasini misolda ko'ramiz:
def daraja(n):
    return lambda x:x**n
kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")