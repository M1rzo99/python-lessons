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


#Yuqorida ko'rgan usulimiz fayl bilan ishlashning eng xavfsiz usuli. Aslida biz fayllarni to'g'ridan-to'g'ri fayl=open('pi.txt') yordamida ochishimiz, fayl bilan ishlab bo'lgandan so'ng esa fayl.close() komandasi yordamida faylni yopishimiz ham mumkin edi:
    
fayl = open('pi.txt') 
PI = fayl.read()
print(pi)
fayl.close() 
    
    
# Etiborli jihat!
#Lekin, bu usul xavfli hisoblanadi va tavsiya qilinmaydi. Gap shundaki, open() funksiyasi yordamida faylni ochganimizdan keyin, toki close() metodini chaqirgunga qadar faylimiz ochiq holatda turadi. Agar, faylni vaqtida yopmasak, yoki fayl yopilmasidan avval dasturimiz to'xtab qolsa fayl tarkibiga ziyon yetishi, ma'lumotlar yo'qotilishi mumkin. Misol uchun, boshqa dasturlarda ham (masalan Microsoft Word) faylni yopmasdan oldin kompyuteringiz o'chib qolsa, yoki dastur behosdan yopilib ketsa faylingizga ziyon yetkani kabi.
#Shuning uchun open() funksiyasiga with orqali murojat qilganimizda, faylimiz with blokining oxirigacha ochiq turadi, va with tugashi bilan, fayl ham yopiladi. Demak fayl ustidagi amallarni biz with bloki ichida bajarib olishimiz kerak.    
    
    
print(pi)

# Matn faylda qanday saqalangan bo'lsa, huddi shu ko'rinnishda consolega chiqadi.Saqlangan ma'lummotlar son bo'lsa,faylda o'qiganimizda qaytgan qiymat string(matn) ko'rinishida bo'ladi. Matnni songa o'tkazish un biroz ishlov beramiz.

pi=pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlalymiz
pi=pi.replace("\n", "")# qator tashlash belgisini almashtiramiz
pi=float(pi) # matnni float(o'nlik) songa o'tkazamiz
print(pi)    
type(pi)
    
    #.replace() metodi matn tarkibidagi biror harf yoki belgini boshqa harf yoki belgi bilan almashtirish uchun ishlatiladi.
    
# Papka ichidagi fayllarni ochish
# Agar bzi ochayotgan fayl dasturimiz bn bir papkada emas bo'lsa,shu papka ichidagi papkada joylashgan bo'lsa,fayl nomidan oldin papka nomi yoziladi

with open("data/pi.txt") as fayl :
    pi=fayl.read() # read orqali malumotni faqat o'iy olamiz
    
# Agar papkalar bir nechta qavat bo'lsa,fayl nomi va ungacha bo'lgan papkalarni alohida yozib olgan avfzal:
faylnomi = "data/math/numbers/pi.txt"
with open(faylnomi) as fayl:
    pi=fayl.read()


# Windowsda papkalar orasida \ belgisi ishlatilsa,Pythonda / belgisini ishlatavering.Agar \ belgisini ishlatsangiz, bu belgini 2 marta yozing: C\\Pyton\\darslar\\data




















