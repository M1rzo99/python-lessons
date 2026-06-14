# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sat May 30 22:20:57 2026

# @author: mirzo
# """

# Qiymat qaytaruvchi funksiya

def toliq_ism_yasa(ism,familya):
    """ Toliq  ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familya}"
    return toliq_ism
user1 = toliq_ism_yasa("Mirzo", "Shomuratov")
user2 = toliq_ism_yasa("Asliddin", "Uzoqov")
print(user2,user1)

# Return  - o'zgaruvchining qiymatini qaytaradi.

# Ixtiyoriy argumentlar - parametrga kiritgan malumotni yoki argumentini beramiz, yokida bermaymiz

def oila_ism_yasa(ism,familya,oilada_kim=""):
    """ Oila azosi nomi va oilada kimligi ko'rsatuvchi function"""
    if oilada_kim:#oiladagi rolini tekshiramiz
        oilada_azo = f"{ism} {familya} {oilada_kim}"
    else:
        oilada_azo = f"{ism} {familya}"
    return oilada_azo.title()
shaxs1 = oila_ism_yasa("Aziza", "SHomuratova")
print(shaxs1)

# Funksiyadan Lug'at qaytaramiz

def avto_info(komponiya,model,rangi,karobka,yili,narx=None):
    avto ={
        'komponiya':komponiya,
        'model':model,
        'rangi':rangi,
        'karobka':karobka,
        'yili':yili,
        'narx':narx
        }
    return avto
avto1 = avto_info("KIA", "K9", "Qora", "Avtomat", 2025,220000)
avtolar = [avto1]
print("Onlayn  bozordagi mavjud mashinalar:")
for avto in avtolar:
    if avto["narx"]:
        narx = avto["narx"]
    else:
        narx = "Nomalum"
    print(f"{avto['model']}, {avto['komponiya']}. Narxi:{narx}")

# Funksiyadadn ro'yhat qaytaramiz
# oraliq nomli function yasaymiz va functionimiz 2 son oralig'idagi sonlarni ro'yhat ko'rinishda qaytaradi.
def oraliq (min,max):
    sonlar=[] #bo'sh ro'yhat
    while min<max:
        sonlar.append(min)
        min +=1
    return sonlar
    
print(oraliq(0, 10))














