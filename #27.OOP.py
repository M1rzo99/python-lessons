#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 23:00:25 2026

@author: mirzo
"""

# OOP - oBjectga yo'naltirilgan dasturlash tushunchasi.

# Klassik(chiziqli) dasturlash.

# Ilk komputerlar va dasturlar,matematik muammolarni yechishga qaratilgan.
#Bunday dasturlar foydalanuvchcidan biror malumiotni qabul qilib oladi va qatiy ketma-ketlikda yani tartibga amal qilgan holda, turli arifmetik amallar bajarib,dastur so'ngida foydalaniuvchi kutgan natijasni qaytaradi.
# shuning un ham bunday dastur,chiziqli yoki tartibli dastur ddi.

# Chiziqli dasturlarning afzalliklari:
    
# Dasturlashni o’rganish uchun qulay
# Sodda va tushunarli kod
# Dastur algoritmini kuzatish oson
# Dastur xotirada kamroq joy egallaydi


# Chiziqli dasturlarning kamchiliklari:
    
# Murakkab dasturlarni chziqili usulda yozish qiyin (ilojsiz)
# Bir dastur uchun yozilgan koddan boshqa dasturda qayta foydalanib bo’lmaydi
# Dastur ichidagi ma’lumotlar (o’zgaruvchilar) barcha funksiyalar uchun ochiq
# ZAMONAVIY DASTURLAR CHIZIQLI EMAS.


# 1970 - yillarda Object Oriented Programming tamoyili olg'a surila boshladi.

# Object - Dasturlashda o'zaro bog'liq bo'lgan o'zgaruvchilar va functionlar bitta konteynerga jamlanadi va bunday konteynerlar OBJECT ddi.
#Proportiers - Bir obyektga tegishli o'zgaruvchilarnig xususiyatlari,unga tegishli funksiyalar esa methodlar ddi.

#Agar real dasturdan misol keltiradigan bo’lsak, istalgan dastur ichidagi tugma bu obyekt. 
#Uning shakli, rangi va matni esa xususiyatlari bo’ladi. Tugma ustida bajariladigan amallar tugmaning metodlari deyiladi.
#Misol uchun tugmani bosish, uzoq bosish, ustiga sichqonchani olib borish va hokazo.


# Object Orinted Dasturlar o'nlab balkim yuzlab objectlardan iborat bo'ladi. Va bunday dastular uchun dastur boshi yoki oxiri degn tushuncha nisbiy bo'ladi.
# Object Oriented dastrular bajarilishida qatiy ketam-ketlik amal qilmaydi.Foydalanuvchi istalgan objectga murojat qilishi,uning ustida amallar bajarishi mn.
# Bitta Objectga murojat ortidan,boshqa object ham faollashishi mn.


#Misol uchun, mobil ilovalarda obyektlar bu dastur ichidagi tugmalar, matnlar, rasmlar va boshqa elementlardir. Foydalanuvchi istalgan tugmani bosishi, istalgan matnni ajratib olishi va boshqa amallarni istalgan tartibda bajarishi mumkin. Bunda bitta tugma (ya’ni obyektni) bosish bulan boshqa obyekt (masalan rasm) o’zgarishi mumkin.
#Zamonaviy kompyuter o’yinlari ham minglab obyektlardan iborat. Foydalanuvchi esa virtual o’yin olamida erkin harakat qilishi, istlagan tarafga yurishi, istalgan vaqtda turli obyektlar bilan turli amallar bajarishi mumkin. 


#KLASS NIMA?

# Object Orinted Programmingda haqida so'zlar ekanmiz, uning fundamental tushunchalaridan biri Class haqida gapirib o'tmaslikning iloji yo'q.
# Class bu -object yaratish un shablon yoki qolibdir.
# Bitta classdan biz istalgancha nusxa olishimiz va yangi object yaratishimiz mn. 
# Demak, Object bu biror classning xususiy ko'rinishidir.
# Odatda claslarning nomi o'zgarmas,undan yaratilgan objectlar esa istalgancha nomlarnishi mn.



# OOP tamoyillari:
    #Incapsulation
# # biz oldinroq malum bir objectga tegishli bo'lgan xususiyatlar va methodlarni bitta konteynerga joylaymiz dedik. Bu jarayon incapsulation(kapsulaga solish) ddi.
#Incapsulation bizga classslar yaratishga va bu classlardan objectlar yaratishga yordam beradi.

    #Abstraksiya
    # Abstraksiya yordamida biz codimizning ichki tuziulishini yashiramiz.Tashqaridan qaraganda objectimiz 2ta parametr va 2ta methodan iborat bo'lsihi mn,lekin obyeckt to'g'ri ishlashi un uning ichida o'nlab o'zgaruvchilar va funksiyalar yashirin bo'ladi.
    # Classlardan foydalanishda objectimizning ichki tuzilishi va qanday ishlashi talab qilinmaydi.
    # Bu o'zimizga ham boshqa dasturchilarga ham codemizdan foydaslanishda qulayliklar yaratadi
    
    
    # Vorislik
    # Dasturlash jarayonida bir classdan boshqa class yaratishimiz mn. Misol un bizda transport classi bor, biz bu clasdan Avtomobil,Kema,Poyezd,Motosikl kabi klasslar yaratishimiz mn.
    # Bunda bizning asl classimiz ota yoki super class ddi,unda yaratilgan classlar esa voris klass ddi.
    
# Voris classlar,ota classning bazi yoki barcha xususiyatlari va methodlariga ega bo'ladi.

    # Polimorfizm
    # Voris class super classdan o'zlashtirgan methodning nomini saqlagan holda,uning ishlashini o'zgartirishga poliformizm ddi.
    
    # Keling bir misol ko’raylik. Biz kompyuter o’yini yaratish jarayonida o’yin Qahramon uchun super klass yaratamiz. 
    #Qahramon bir nechta xususiyatlarga va metodlarga ega. Jumladan attack() ya’ni xujum qilish metodi, qahramonni xujum qilishga undaydi.
    #Endi biz bu superklassdan boshqa voris klasslarni yaratamiz. 


#Birinchi qahramonimiz Qilichboz va bu qahramon xujum qilganda qilich bilan xujum qiladi.
#Ikkinchi qahramonimiz esa Jangchi, va u qurolsiz bo’lgani sababi qo’l va oyoqlari bilan xujum qiladi.
#Uchunchi qahramonimiz pistolet bilan, 
#Oxrigisi esa kamon va yoylar bilan qurollangan.
#To’rttala qahramonimiz ham superklassdan attack() metodini meros oladi, lekin bu metodni biz har bir qahramon uchun turli ko’rinishda yozishimiz va talqin qilishimiz mumkin. Bu esa o’z navbatida bizni turli qahramonlar va turli xujum turlari uchun alohida metodlar yozishdan qutqaradi.
#Mana shular OOPning asosiy tamoyillari ekan.


#OOP AFZALLIKLARI VA KAMCHILIKLARI:
    # Afzalliklari
    #Parallel dasturlash – bir loyihaning turli qismlari bir vaqtda yaratilishi mumkin
    #Vorislik tamoyili klasslardan qayta foydanalish imkonini beradi
    #Polimorfizm tamoyili klasslarni moslashuvchan qiladi
   # Klasslardan boshqa dastur va loyihalarda qayta-qayta foydalanish mumkin
   

    #Kamchiliklari
    #Dasturlashga yangi qadam qo’yganlar uchun biroz tushunarsiz
    #Har doim ham samarali emas
    #Ba’zida dasturimizni haddan tashqari murakkablashtirib yuborishi mumkin















