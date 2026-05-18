#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 18:39:33 2026

@author: mirzo
"""

#if-elif-else =  bu yerda elif = else/if ga to'g'ri keladi

yosh = int(input('Yoshingiz nechada?:\n >>>'))
if yosh<=4:
    price = 0
elif yosh<=12:
    price = 5000
elif yosh<=40:
    price = 1000
else:
    price = 8000
print(f'Sizga kirish {price} so\'m')
# elifni bizga kerakli darajad afoydalana olamiz.

#         OR- operatori yoki deb tarjima qilinadi.2 va undan orqatiq ishni bajarganda ishlatilinadi
#Misol un: shanba va yakshanba kiritilsa "bugun dam olish kuni" degan yozuv chiqarilsin

kunlar = input("Bugun haftaning qaysi kuni?  ")
if kunlar.lower() == "shanba" or kunlar.lower() == "yakshanba" or kunlar.lower() == "juma":
    print(f"Bugun {kunlar}, dam olish kuni.")
else:
    print(f"Bugun {kunlar}, ish kuni.")
    
    # AND - operatori. 2 va undan ortiq amallarni bajarishda ishlatamiz. and ishlatganda bizning hamma shartni bajarsagina true bo'ladi.
    # ahs holda false qaytaradi
    
kun = input("bugun nima kun?>>")
harorat = float(input("Harorat qanday?>> "))
if kun.lower() == "yakshanba" and harorat>=30:
    print("Kettik cho'milib kelamiz")
elif kun.lower() == "yakshanba" and harorat<30:
    print("Uyda dam olamiz!")
    
# Biz o'zgaruvchilarga boolean qiymatini ham bera olamiz
#narh=15000
#salad = False
#if choy and salad:
  #  narh = narh+10000
#elif choy or salad:
 #   narh = narh+5000
#print(f"Jami {narh} pul to'laysiz!")

# shartlarni ketma-ketlikda bajarish.
# if-elif-else ning kamchiliklaridan biri shuki unga berilgan qiymat true bolsa, shu joyda to'xatydi va keyingi qiymatga o'tmaydi
# ketma-ketlikda tekshirish un esa - davomiy if functionini ihslatamiz

narh = 10000
salad =True
choy =True
manti = True
piyoz = False
sabzi = False
if salad:
    print("Mijoz salad oldi!")
    narh = narh+1000
if choy:
    print("Mijoz choy oldi!")
    narh = narh+2000
if manti:
    print("Mijoz manti oldi!")
    narh = narh+10000
if piyoz:
    print("Mijoz piyoz oldi!")
    narh = narh+1000
if sabzi:
    print("Mijoz sabzi oldi!")
    narh = narh+3000

print(f"umumiy narx {narh} bo'ldi")
# agar tepadagi functionda elif dan foydalansak,salad da true bo'lardi va shu joyda function yakunlanardi


# IN operatori yordamida ro'yhatda malum bir qiymat borligini tekshiramiz
product = ['sabzi','piiyoz','sut','un','gugurt']
'sabzi' in product

#  menyu yaratish
menyu = ['manti','osh','shurpa','shashlik']
oqat = input("Qanday ovqat buyurtma berasiz?>> ")
if oqat.lower() in menyu:
    print("Buyurtma qabul qilindi!")
else:
    print("Menudan bunday ovqat yo'q!")


    # not in orqali esa ro'yhatda qanday element yo'qligni tekshiramiz
    # not ni  != shuning o'rniga ishlatsak ham bo'ladi 
    # if not = 5 yani if !=5 degan manoni bildiradi

menyu = ['manti','osh','shurpa','shashlik']
oqat = input("Qanday ovqat buyurtma berasiz?>> ")
if oqat.lower() not in menyu:
    print("Menudan bunday ovqat yo'q!")
   
else:
    print("Buyurtma qabul qilindi!")
    
# ikkita ro'yhatini solishitish
taomlar = ['manti','osh','shurpa','shashlik','non','osma']
buyurtmaa = ['manti','norin','choy','shashlik']
for taomm in buyurtmaa:
    if taomm in taomlar:
        print(f"Menyuda {taomm} bor")
    else:
        print(f"Afsuski menuda {taomm} yo'q")
        
        
# ro'yhat bo'sh emasligini tekshirish.
taomi = ['manti','osh','shurpa','shashlik','non','osma']
buyur = ['manti','norin','choy','shashlik']
if buyur:
    for tam in buyur:
        if tam in taomi:
            print(f"Menuda {tam} bor")
        else:
            print(f"Menuda bunday taom yo'q!")
else:
            print("Sizning savatchangiz bo'sh!") # Yani buyur=[] shunnday holatda savatcha bo'sh qaytadi
    


# Amaliyot

 








    
    
    
    
    