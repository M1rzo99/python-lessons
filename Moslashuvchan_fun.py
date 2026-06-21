#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:05:52 2026

@author: mirzo
"""

# Moslashuvchan Function (args,kwargs)
#agar function bir -nechta argument qabul qilishi kerak bo'lsayu,lekin argumment sonini aniq bilmasak, 
# Pythonda istalgancha qiymat qabul qiluvchi function bor

# *args usuli
# Agar function qabul qiladigan parametrlar soni noaniq bnolsa va parametrlar yagona qiymat ko'rinishida uzatilsa, function yaratishda argumentdan oldin * qo'yiladi.
def summa(*sonlar):
    """Kiritilgan sonlar yog'indisini hisoblaydi"""
    yigindi = 0
    for son in sonlar:
        yigindi +=son
    return yigindi
print(summa(10,12)) 

# oraliq degan function. range functionni qo'lda yasaymiz
def oraliq (min,max):
    sonlar=[]
    while min<max: # qachonki mindagi son max dagi sondan kichik bo'lsa, pastdagi jarayon ishlasin
        sonlar.append(min) # sonlar nomli listga qo'shadi,qachonki mindagi son maaxdagi songa teng bo'lmaguncha.
        min +=1 # while tsikli har safar aylanganda unga +1 qo'shilsin
    return sonlar # va sonlar nomli listni qaytarsin(boshqa joylarda ham ishlatsa bo'ladigan qb)
print(oraliq(0,11))

