#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 14:24:46 2026

@author: mirzo
"""

# Dictionary - lug'at ddi.quyidagi tartibda ishlatamiz
car_0 = {"model": "bmw","rangi": "blue"}
print(f"Moshina {car_0['model']}, rangi {car_0['rangi']}")

mevalar = {"uzum":1000,"banan":2000,"olma":3000}
print(f"Uzum narxi: {mevalar['uzum']},Banan narxi:{mevalar['banan']},Olma narxi:{mevalar['olma']}")

# lug'at ichiga qo'shimcha kalit va qiymatlar qo'sha olishimiz mn quyidagi ko'rinishda:

talaba = {"ism":"Mirzo","yosh":27,"Davlat":"Korea"}
print(talaba)
talaba["tili"] = "Uzb"

talaba["yo'nalishi"] = "cs"
print(talaba)

# Malum bir kalit so'zga mos keluvchi qiymatni ham o'zgartira olamiz
talaba["ism"] = "Odil"
print(talaba)

# bosh lug'at yaratib ham,keyinhalik unga qiymatlar bera olamiz:
    
sabzavot =  {}
print(sabzavot)
sabzavot["sabzi"] = "sariq"
sabzavot["piyoz"] = "2 kg"
print(sabzavot)

# Dictionarydan biroe malumotni olib tashlash
del sabzavot['piyoz']
print(sabzavot)

# Biz dictionary yaratamiz va undagi qiymatlarni chaqira olamiz. Lekin dictionary da yo'q qiymat bo'lsachi? 
# shu payt get("kalit soz", "qaytuvchi xabar") orqqali bera olamiz

sabzavotlar = sabzavot.get("sabzi","Bunday qiymat mavjud emas")
print(sabzavotlar)

# agarda ikkinchi(errorni ko'rsatadigan) kalit so'zga =hech qanday qiymat bermasak, null ko'rsatadi










