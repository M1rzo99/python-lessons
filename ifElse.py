#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:02:45 2026

@author: mirzo
"""
# if = agar shunday bo'lsa,bu shartni bajar; 
# else = agar shunday bo'lmasa, bu shartni bajar
# if asosan true bo'lsa
# else asosan false bo'lsa
#avtolar = ["audi","bmw","kia","gelikGT","GM"]
for avto in avtolar:
    if avto == "audi":
        print(avto.upper())    
    else:
        print(avto.title())
        
    
# true/false
# ism nomli o'zgaruvchi yaratdik va unga qiymat berdik
# qiymat to'g'ri bo'lsa true,noto'g'ri bo'lsa false qaytaradi
# ism = "Mirzo"
# ism == "Mirzo"
#ism == "Mirzobek"

# matnlar bilan ishlaganda,matnni ma'lum bir ko'rinishg keltirib olish kerak. 
# chunki ali,Ali,ALI bir manoga ega bo'lgani bilan harflar katta kichigligi comp tilida har xil manoni beradi
# turli-xil matnlarni solishtrishdan avval ularni kichik harflar ko'rinishiga keltirib olamiz
# .lower() ko'rinishida
#ism = "Mirzo"
#ism.lower() == 'mirzo'

# qiymatlarni teng emasligini tekshirish
# != operatori - ikki qiymat teng emas degani
#ism = input("Ismingiz nima?\n>>>")
if ism.lower() != "mirzo":
     print(f"Uzr,{ism.title()} biz Mirzo ni kutayapmiz")
else:
        print("Salom, Mirzo")
     
#ovqat = input("Bizda faqat gumma bor,yeysizmi?\n>>")
if ovqat.lower() != "yoq":
    print("Ovqat 5 minda tayyor bo'ladi")
else:
    print("Sizda he deyishdan boshqa imkon yo'q!")
    
     
# Sonlarni solishtirish
#jb = float(input("15x5 nechiga teng?\n>>>"))
if jb != 75:
    print("Javob xato!")
else: 
    print("75 javobi to'g'ri :)")

# yosh
#yosh = int(input("Yoshingiz nechida?\n"))
#f yosh>18:
    #print("Xush kelibsiz!")
#else: 
  # print("Siz hali 18 ga to'lmagansiz,kirish mn em
          
# login uzunligi
#login = input("Yangi login yarating:  ")
if len(login) <=5:
    print("Login 5 harfdan katta bo'lishi shart!")       
else:
    print(f"{login.title()} nomli Yangi login yaratilindi!")
          
# Yoshni aniqlash
#yil = int(input("Tug'ilgan yilingizni kiriting:  "))
if 2026-yil<18:
    print(f"{2026-yil} Yoshda ekansiz")
    print("Kirish mn emas!")
else:
    print(F"Sizning yoshingiz, {2026-yil} da ekan,Hush kelibsiz!")          
          
          
          
          
# Bir qatorlik if/else
#ysh = int(input("Yoshingizni kiriting:\n>>"))
#if ysh>65: print("Siz 65 yoshdan katta ekansiz!")
#lse: print("Siz 65 yoshdan kichik ekansz!")

          

          #10 dars amaliyot
#1 Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
#avtolara = ["audi","bmw","kia","gelikGT","gym"]
#for avsto in avtolara:
  #  if avsto.lower() == "bmw":
   #     print(f"{avsto.upper()}")
  #  else:
   #     print(avsto)

#2 Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
avtolar = ["audi","bmw","kia","gelikGT","GM"]
for avto in avtolar:
    if avto != "audi":
        print(avto.title())    
    else:
        print(avto.upper())
        
#3 Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
foy = input("Sizning login ismingiz nima?\n>>>")
if foy.lower() == "admin":
    print("Foydalanuchilar ro'yhatini ko'rasizmi?")
else: 
    print(f"Xush kelibsiz {foy.title()}!")

#4 Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
son1 = int(input("1-sonni kiriting:\n>>"))
son2 = int(input("2-sonni kiriting:\n>>"))

if son1==son2:
    print("Sonlar bir birga teng")
else:
    print(f"birinchi son {son1}, ikkinchi son {son2} dir")
    
#5 Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring
son3 = int(input("istalgan son kiriting:\n>>"))

if son3<0:
    print(f"manfiy son {son3}")
else:
    print(f"musbat son {son3} dir")
#6 Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
son4 = int(input("istalgan son kiriting:\n>>"))
if son4>0:
    print(f"{son4} ning ildizi, {son4**0.5} ga teng")
else: 
    print("Hozirgi son manfiy,Musbat son kiritng!")
    
    
    
     
    
 