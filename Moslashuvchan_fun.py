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
# Agar function qabul qiladigan parametrlar soni noaniq bo'lsa va parametrlar yagona qiymat ko'rinishida uzatilsa, function yaratishda argumentdan oldin * qo'yiladi.
def summa(*sonlar): # bitta argument beramiz va istalgancha parametr bersak bo'ladigan function
    """Kiritilgan sonlar yog'indisini hisoblaydi"""
    yigindi = 0
    for son in sonlar:
        yigindi +=son
    return yigindi
print(summa(10,12)) 
print(summa(1,2,3,40))

# TUPLE - o'zgarmas ro'yhat hisoblanadi.

# oraliq degan function. range functionni qo'lda yasaymiz
def oraliq (min,max):
    sonlar=[]
    while min<max: # qachonki mindagi son max dagi sondan kichik bo'lsa, pastdagi jarayon ishlasin
        sonlar.append(min) # sonlar nomli listga qo'shadi,qachonki mindagi son maaxdagi songa teng bo'lmaguncha.
        min +=1 # while tsikli har safar aylanganda unga +1 qo'shilsin
    return sonlar # va sonlar nomli listni qaytarsin(boshqa joylarda ham ishlatsa bo'ladigan qb)
print(oraliq(0,11))

# Agar biz argumentga majburiy ikkita qiymat bersak va qolganlarini args(*) orqali bersak, oldingi ikkita argumnetga qiymat berish majburiy
def smma(x,y,*snlar):
    """ Kiritilgan sonlar yig'indisni hisoblaydigan Function"""
    return x+y+sum(snlar)
print(smma(1,23,4,5))
print(smma(10,23)) # Bu holatrda *snlar argumentiga hechg qanday parametr bermasak ham error chiqmaydi

# **kwargs - keywords degan manoni bildiradi.
# kalit so'zlik argumetlarni ham functionga uzatish mumkin *kwargs orqali.

def avto_info(komp,model,yili,**malumotlar):
    """ Avto haqidagi malumotlarni lug'at ko'rinishida qaytaradigan funksiya"""
    malumotlar['komp']=komp
    malumotlar['model']=model
    malumotlar["yili"] = yili
    return(malumotlar)
print(avto_info("GYM", "GELIK",2019, rangi="Tyomniy",holati="eski"))
# Yuqorida malumotlarni *kwargs shaklid auzatganda,ular ixtiyoriy bo'ladi. Parametr kiritsak ham bo'ladi, kiritmasak ham bo'ladi.
# kwargs da functionni parametrlarini chaqirsak, oldin kwargsdagi malumotlar kelib chiqadi. Chunki bu function shudnay shaklda ishlaydi
# malumotlar nomli list yaratadi va shu listga malumoatlarni joylaydi.

# 1.Amaliyot - Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing.
def sonlar_hoxish(*sonlari):
    """ Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya"""
    soniz = 1
    for son in sonlari:
        soniz *=son
    return(soniz)
print(sonlar_hoxish(2,4,3))

#2.Amaliyot.Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

def talaba_malumot(ism,yosh,**malumot):
    """Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya """
    malumot['ism'] =ism
    malumot['yosh']=yosh
    return malumot
print(talaba_malumot('Mirzo', 27, fam = "SHOMURATOV",nick="Mijo"))

































