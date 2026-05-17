#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:44:33 2026

@author: mirzo
"""

# Bu bo'limda xatolar bilan ishlashni o'rganamiz

# 1. SytaxError - odatda dasturlash tili qoidalariga amal qilmasak sodir bo'ladi.Aksar dasturlash tillari syntaxerror bor kodlarni bajaradi, lekin python bajarmaydi
#print "hello world"

# EOL (end of line - qator yakuni) xatosi
# odatda qator oxirida qo'shtirnoq yoki  birtiroqni yopish essdan chiqganda yuzaga keladi
#print("Helo world!

# EOF (End of Function - function yakuni ) xatoligi esa function oxirida qavs ni yopish esdan chiqganda kelib chiqadi
#print("Hello world!"

#2. IndentationError - joy tashlashda xatolik
#python tilida joy tashlab yozish yoki qatot boshidan joyiz muhim ahamiyatga ega
 #print('hello world')

# Bazi joylarda (for tsikli yoki if-elif-else) larda qator tashlab yozish muhim
# agarda for yoki if-elif-else da joy tashlaganda, hamma joy tashlashlarni bir xil shaklda qilmasak error kelib chiqadi.


# Run time error - dasturni bajarishda kelib chiqadigan xatolik
#1. typeError - function yoki methodni noto'g'ri malumot ustida bajarish

#son  = input("Istalgan sonni kiriting:")
#print(f"{son} ning kvadrati {son**2} ga teng")
# yuqoridagi qiymatda inputdan keladigan qiymatni matndan son ko'rinishga o'tkazishni unutdik.Shuning sabali error kelib chiqadi.


#2. NameError - O'zgaruvchi,function, obyekt nomini noto'g'ri yozishda kelib chiqadi.
#mevalar = ["nok","olma"]
#for meva in mvalar:
 #   print(meva)
# yuqoridagi codeda: name "mevalar" is not defined deb chiqadi

#3. ValueError - function noto'g'ri qiymat yuborish natijasida kelib chiqadi
#son = int(input("istalgan sonni kiriting:"))
#if son>=0:
 #   print("Musbat son")
#else:
#    print("manfiy son")

# yuqoridagi codeda: ValueError: invalid literal for int() with base 10: '2.1
# chunki inputdan kelgan qiymat maxfiy va musbat shaklida kelsin degan function yozganmiz, 10 lik sanaoqda kelsa degan qismni unutganmiz

#4. IndexEerror - ro'yhatdagi elementlarga murojat qilishda, element indexini noto'g'ri kiritish
#mevalar = ["nok","olma"]
#print(mevalar[3])
# IndexError: list index out of range
# chunki bizda 3 nomli index yo'q

#5. ZeroDivisionError - dastur jarayonida 0 ga bo'lish yuzaga kelgandagi holat
x,y = 50,50
z=250/(x-y)
#ZeroDivisionError: division by zero
# yani 250 ni 0 ga bo'lib bolmaydi. Har qanday qiymatni  0 ga bo'ib bo'lmaydi degani



