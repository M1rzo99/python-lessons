#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 18:05:45 2026

@author: mirzo
"""


#1. JSON nima? 
# JSON(JAVA SCRIPT Object Notation) bugungi kunda ma'lumotlarni saqlash va internet orqali uzatish un qo'llanilidigan eng mashhur platforma hisoblanadi.
# Dastavval Java Script un Yaratilgan bu format, bugungi kunda deyarli barcha dasturlash tillari tomonidan ishlatilinadi.Qolaversa JSON formatdagi fayllarning tarkibini oddiy matn muharriri yordamida ko'rish va tahrirlash mumkin.
# Aksar hollarda dastur va server orasidagi ma'lumotlar aynan JSON ko'rinishda uzatilinadi.

# JSON yordamida nafaqat lug'at,balki boshqa turdagi ma'lumotlarni ham saqlashimiz mumkin.Bunda Pythondagi malumot turlari,quyidagi jadval asosida,Java Script ma'lumot turlariga konvertasiya qilinadi: 
    # Python    JavaScript
    
 #   dict             Object
 #   list             Array
 #   tuple            Array
  #  str()            String
 #   int()            Number
  #  float            Number
  #  True            true
   # False           false
   # None            null
   
# Demak,dsaturimiz davomida malumotlarni JSON ko'rinishdia saqlashmiz, internet orqali boshqa foydalanuvxhilarga ,dasturlarga yoki serverlarga yuborishimiz,JSON fayllarni Pythonda ochib,unga ishlov berishimiz va turli amallar bajarishimiz mn.
# JSON o'zgaruvchilar, tarkibidan qat'iy nazar matn ko'rinishida saqlanadi.

#2.Pythondan JSON ga

# JSON ma'lumotlar va fayllar bn ishlash un pythonda maxsus json moduli bor. Demak,dasturimiz boshida biz bu modulni yuklab olishmiz kk.
# malumotlarni JSON matniga o'tkazish un  ikki funksiyasan foydalanamiz:
    # json.dumps(x) - berilgan x o'zgaruvchisini JSON matniga o'zgartiradi
    # json.dump(x,fayl) - berilgan x o'zgaruvchini JSON ga o'tkazib,ko'rsatilgan faylga saqlaydi.
 
# json.dumps() - Ma'lumotlarni json formatiga o'tkazish un foydalanamiz: 
import json
x=10
x_json = json.dumps(x)

ism="Mirzo"
ism_json = json.dumps(ism)


sonlar = [12,45,56,78,7]
sonlar_json = json.dumps(sonlar)

# JSON malumotlarni matn(string) ko'rinishid saqlaydi
print(type(sonlar_json))



bemor = {
  "ism": "Alijon Valiyev",
  "yosh": 30,
  "oila": True,
  "farzandlar": ("Ahmad","Bonu"),
  "allergiya": None,
  "dorilar": [
    {"nomi": "Analgin", "miqdori": 0.5},
    {"nomi": "Panadol", "miqdori": 1.2}
  ]
}

bemor_json = json.dumps(bemor)
print(bemor_json)

# Yuqridagi natijada o'qish un juda noqulay. Keling uni o'qishga qulay holatga o'tkazamiz. 
# Buning un bizga dumps() ga qoo'shimcha indent=4 parametrnini beramiz.Bu parametr ma'lumotlarni saqlashda chapdan o'ngga qancha joy tashlash kerakligini aytadi.

bemor_json = json.dumps(bemor, indent=4)
print(bemor_json)

# Mavzu boshida,JSON ichidagi ma'lumotlar Java Script malumot turlariga konventsiya qilinadi degandik.Buni yuqoridagi misolda korishingiz mumkin(farzandlar,oila,allergiya kalitlari qiymatini asl lugat bn solishtiring)




# Json.dump()
 # Ma'lumotlarni JOSN formatiga o'tkazish va faylga saqlash un json.dump() funksiyasini chaqiramiz.Funksiya parametri sifatida o'zgaruvchi va fayl nomini ko'rsatamiz.
 # Albatda buning un avval faylni ochgan bo'lishimiz kerak. 
 

bemor = {
  "ism": "Alijon Valiyev",
  "yosh": 30,
  "oila": True,
  "farzandlar": ("Ahmad","Bonu"),
  "allergiya": None,
  "dorilar": [
    {"nomi": "Analgin", "miqdori": 0.5},
    {"nomi": "Panadol", "miqdori": 1.2}
  ]
}

# bemor objectini json formatga o'tkazadi va bemor.json faylg saqlaydi
with open("bemor.json",'w') as f:
    json.dump(bemor,f)

# bemor.jsonga asaqlangan faylni o'qiydi.
with open("bemor.json") as file:
    info = file.read()
print(info)






#json.load()
#Bu funksiya JSON fayllarning tarkibini Pythonga yuklab olish uchun ishlatiladi. 

filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)
    
print(type(bemor))
#Natija: <class 'dict'>












