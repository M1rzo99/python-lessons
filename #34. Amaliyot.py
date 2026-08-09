#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 14:14:13 2026

@author: mirzo
"""
import json
#1.Ushbu o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini konsolga chiqaring:
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json = json.dumps(data,indent = 2)
print(data_json)

#2. Ushbu JSON matnni ko'chirib oling, va talabaning ismi va familiyasini  konsolga chiqaring: 
    #Buning un oldin
    #1.Malumotni JOSN formatda filega saqlash kerak 
    #2.JOSN formatni o'qib olsih lozim va print ga chiqasa bo'ladi.
    
talaba_json = {"ism":"Hasan","familiya":"Husanov","tyil":2000}
 
with open("talaba.json","w") as f:
    json.dump(talaba_json,f)
    
with open("talaba.json") as f:
    talaba  = json.load(f)
print(talaba['ism'],talaba['familiya'])

#3. Yuqoridagi ikki o'zgaruvchini alohida JSON fayllarga saqlang.

# with open("ism.json",'w') as f:
#     json.dump(talaba_json['ism'],f)
    
    
# with open("familya.json",'w') as f:
#    json.dump(talaba_json['familiya'],f)
    
# with open("familya.json") as f:
#     fl = json.load(f)
# print(fl)


# with open("ism.json") as t:
#     tl = json.load(t)
# print(tl)


import json

fayllar = {
    "ism": "ism.json",
    "familiya": "familiya.json"
}

for kalit, fayl_nomi in fayllar.items():
    with open(fayl_nomi, "w") as f:
        json.dump(talaba_json[kalit], f)

for kalit, fayl_nomi in fayllar.items():
    with open(fayl_nomi) as f:
        malumot = json.load(f)
    print(malumot)
    
    
#4.Quyidagi JSON faylni yuklab oling. Faylda 3 ta talabaning ism va familiyasi saqlangan. Ularning har birini alohida qatordan "Ism Familiya, n-kurs, Fakultet talabasi" ko'rinishida konsolga chiqaring.

with open("students.json") as f:
    st_tartib = json.load(f)
print(st_tartib)

talabalar = st_tartib["student"] # BU yerda stundent kalitning qiymatini oladi va talabalar nomli o'zgaruvchiga saqlaydi.

for talaba in talabalar:
    ism = talaba["name"]
    familiya = talaba["lastname"]
    kurs = talaba["year"]
    fakultet = talaba["faculty"]

    print(f"{ism} {familiya}, {kurs}-kurs, {fakultet} talabasi")




