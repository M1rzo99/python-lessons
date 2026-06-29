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

# lambda funksiyasi argument sifatida boshqa funksiyalarni qabul qiluvchi funksiyalar bulan ihslashda ham keng foydalanilinadi. Misol un map(), filter() funksiyalari.

# map() funksiyasi - argument sifatida ro'yhat(yoki lug'at )  va boshqa bir funksiyani qabul qilib, ro'yhat elementlariga qabul qilingan funksiaya yordamida ishlov beraid.


from math import sqrt
sonlar = list(range(11)) # 0dan 10 gacha sonlar ro'yhati
ilidzlar = list(map(sqrt,sonlar))             
print(ilidzlar)

# yuqoridagi msiolda 0 dan 10gacha sonlar ro'yhatini tuzib oldik, keyin esa map funksiyasiga ro'yhat va sqrt funksiyasini uzatib, ro'yhatdagi barcha sonlar ildizini hisoblab oldik.

# map() funksiyasi map object qaytargani sababli, qaytgan obyektni  ro'yhatga o'tkazib olish un list() funksiyasidna foydalandik.

# yana bir misol ko'ramiz:
sonlar1 = list(range(11))
def daraja2(x):
    """ Berilgan sonning kvadratini qaytaruvchi function"""
    return x*x
# print(list(map(daraja2, sonlar1))) # sonlar ning kvadaratini hisoblaymiz

# yuqoridagi funklsiyada biz avval berilgan sonning kvadratini hisoblovchi funksiya yaratib oldik, undan keyin esa map yordamida sonlar ro'yhatidgi elementlarning kvadratini ham hisoblab oldik,

# Keling yuqoridagi funksiyani lambda yordamida yozib ko'ramiz:
kvlar = list(map(lambda x:x*x,sonlar1))
print(kvlar)

# Yuqoridagi funksiyada, endi daraja degan funksiyani yaratib o'tirmasdan. o'g'ridan to'g'ri map() ni ichidagi darajani hisoblovchi lambda funksiya uzatdik.
# map() funksiyasi bo'lmaganada biz buinday dasturlarni for yordamida yozishimiz kk bo'lar edi:
kv = []
for son in sonlar:
    kv.append(son*son)
print(kv)

# map() funksiyasiga bir nechta ro'yhatlar ham uzatiosh mn.

a = [4,5,6]
b = [7,8,9]
a_plus_b = list(map(lambda x,y:x+y, a,b))
print(a_plus_b)

# map() istalgan turdagi malumotlar bn ishlaydi:
ismlar=['hasan','husan','ikrom','iqbol']
print(list(map(lambda matn:matn.upper(),ismlar)))


























