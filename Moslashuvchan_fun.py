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