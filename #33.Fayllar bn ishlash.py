#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 19:52:52 2026

@author: Mirzo
"""
# Fayllar bn ishlash: Kirish
# Ushbu bo'limda katta hajmdagi ma;lumoitlarni fayldan yuklab olish va dastur yakunida kerakli ma'lumotlarni va dastur natijasini faylga saqlashni o'rganamiz.
# Fayllar bn ishlash dastur foydalanuvchilariga ha dasturga o'zlari istagan ma'lumotlarni yuklash imklonini beradi.


# Fayldan o'qish: 
#Komputerimizda aksar ma'lumlotlar fayl ko'rinishida bo'ladi. Bu xoh matn bo'lsin,xoh jadval,xoh rasm,xoh video. Fayllarda turli ma'lumotlar  saqlanishi mumkin.
# ob-havo ma'lumotlari,yillik hisobotlar,mijozlarning telefon raqamlari,talabalarning ro'yhati va hkz.
#  Ko'pgina holatlarda katta ma'lumotlarni aynan fayllardaan o'qish talab qilinadi.Ayniqsa,tahliiy dasturlarda fayl ko'rinishida saqlangan, katta hajmdagi jadvallar bn ishlash tabiiy.
# LEKIN FAYLLAR BN ISHLASH BOSHQA HOLATLARDA HAM ASQOTADI.MISOL: ODDIY MATNNI HTML KO'RINISHIDA O'TKAZISHNI AVTOMATLASHTIRUVCHI DASTUR YOZISHDA.

# Faylni to'liqligicha o'qish:
    
with open('pi.txt') as fayl:
    pi=fayl.read()
    
print(pi)

# Kodni tahlil qilamiz:
    
#1. 1- Qatorda open() funksiyasi yordamida faylni ochayapmiz.Bunda funlksiya argument sifatida fayl nomini berayapmiz. 
#BU yerda biz ochayotgan fayl va dasturimiz bir papkada bo'lishi muhim.

# 2. Open()  funksiyasi faylni obyekt sifatida qaytaradi,as operatori yordamida esa biz objectimizga fayl deb nom berayapmiz.

#3. 2- qatorda esa .read() methodi yordamida fayl obyektining tarkibifan bizga kerakli matnni olib,yangi PI o'zgaruvchisiga yuklayabmiz.

#4. with operatorining vazifasi biz fayl bn ishlab bo'lganmizdan so'ng,faylni yopish. Yuqoridagi misolda,2-qatordan so'ng fayl zudlik bn yopilgan.