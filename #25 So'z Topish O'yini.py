#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:11:44 2026
Son topish o'yini

@author: mirzo
"""

import random # tasodifiy sonlarni generate qilishda yordam beradi

def sontop(x=10):# qiymat qabul qiladi va komputer o'ylaydigan sonlarni yuqori chegarasidir(x)
    tasodifiy_son = random.randint(1, x) # berilgan sonlar orasidagi butun sonni qaytaradi
    print(f"Men 1 dan {x} gacha son o'yladim.Topa olasizmi?")
    taxminlar = 0
    while True:
       taxminlar +=1
       taxmin = int(input(">>>"))
       if taxmin<tasodifiy_son:
           print("Xato.Men o'ylagan son bundan kattaroq.Yana harakat qilib ko'ring:")
       elif taxmin>tasodifiy_son:
           print("Xato.Men o'ylagan son bundan kichikroq.Yana harakat qilib ko'ring:")
       else:
           break
    print(f"Tabriklayman, {taxminlar} ta taxmin bilan to'g'ri topdingiz.")
    return taxminlar


def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing.Men topaman")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar = +1
        if quyi !=yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"Men o'ylagan son bundan kattaroq (+), yoki kichikroq(-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} taxmin orqali topdim!")
    return taxminlar
            
            
            
            
            
            
            