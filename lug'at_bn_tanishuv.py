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

#Amaliyot

#1.otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
otam = {"ism":"Maqsudbek","yoshi":54,"tug'ilgan_joyi":"Xorazm"}
print(f"Otamning ismi {otam["ism"]}, {otam['yoshi']} yoshdalar va {otam["tug'ilgan_joyi"]} da tug\'ilgan")

#2. Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
sev_taom = {'Onam':"manti","otam":"palov","Azi":"qovurdoq","latif":"tuxum","Mirzo":"shurpa"}
print(f"Azining sevilmi taomi {sev_taom["Azi"]} dir.")
print(f"Latifning sevilmi taomi {sev_taom["latif"]} dir.")
print(f"Mirzoning sevilmi taomi {sev_taom["Mirzo"]} dir.")

#3.Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
lugat = {
    "integer":"matn yoki 10lik sanoqdagi ko'rinishidagi harflarni, raqamlarga o'zgartiradi"
    "float":"o'nlik sanoq sistemasidagi sonlardir(1.0,2.3,56.7) kabi"
    "string":"harflardan tashkil topgan qiymat string ddi.int/float ko'rinishidagi qiymatlarni stringga o'zgartiradi"
    "if/else":"agar/unday bo'lmasa degan manoni bildiradi"
    }

#4.Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

lugat_dir = input("Kalit so'z kiriting: ")
lugat = {
    "integer":"matn yoki 10lik sanoqdagi ko'rinishidagi harflarni, raqamlarga o'zgartiradi"
    "float":"o'nlik sanoq sistemasidagi sonlardir kabi"
    "string":"harflardan tashkil topgan qiymat string ddi.int/float ko'rinishidagi qiymatlarni stringga o'zgartiradi"
    "if/else":"agar/unday bo'lmasa degan manoni bildiradi"
    }
lugat_asl = lugat.get("integer,float,string", "Bunday lugat topilmadi")
print(f"Siz so'ragan qiymat: {lugat_asl["lugat_dir]")












