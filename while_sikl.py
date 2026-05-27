#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 23:15:22 2026

@author: mirzo
"""

#1. Foydalanuvchi inputga kiritgan malumotga text qo'shib hiqarish
#ism = input("Ismingizni kiriting:")
#print(f"Salom {ism.title()}, Xush kelibsiz!")

#2. Ingliz tilida input ichidagi so'rovli matn prompt ddi.
# shu promtni o'zgaruvchiga yuklab,yangi promptda ishlatsak ham bo'ladi
#ism = input("Ismingizni kiriting:")
#savol = f"Salom, {ism.title()}.Yoshingiz nechida? "
#yosh = input(savol)
#print(f"{ism.title()},{yosh} yo. Xush kelibsiz!")

#3. input() funcitonga kiritilgan har qanday qiymatni matn ko'rinshida qabul qiladi
# Shunign un o'zlarimzni ehtiyojlarimizga qarab, int or float qilib olsak bo'ladi
#ism = input("Ismingizni kiriting:")
#savol = f"Salom, {ism.title()}.Yoshingiz nechida? "
#yosh = input(savol)
#yosh = int(yosh)
#height = input("Bo'yingiz necha metr?")
#height = float(height)
#print(f"{ism.title()},{yosh} yo. {height} metr. Xush kelibsiz!")

#4. while - for kabi malum bir ro'yhatni olib,ro'yhat ichidagi qiymatlar tugagunga qadar biror kodni takrorlaydi
# va for dan farqi, while true bo'lsa kodni takrorlayveradi
# while - toki,gecha degan manolarda keladi
#son  = 1 # songa 1 qiymat beramiz
#while son<=5: #toki son 5ga teng yoki kichik ekan..
#    print(son,end=" ") # 5 sonini konsolga chiqaramiz
 #   son  = son+1 # songa 1 qo'shamiz.toki son 5 bo'lguncha
    
#5. input orqali qilonatotgan dasturimiz bir marta bajarilinayotgan edi. Endi input orqali natijani foydalanuvhcidan qabul qilib,while orqali foydlanuvhci to'xtatishini hoxlagancha ishata olamiz
#print("Bu dastur,Kiriitlgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan sonni kiriting"
#savol +="(Dasturni to'xtatish un 'exit' deb yozing):"
#qiymat = ''
#while qiymat != "exit":
#   qiymat = input(savol)
 #   if qiymat !="exit":
 #       print(float(qiymat)**2)
#print("\nDastur tugadi!")
    
#5. Katta dasturlarda bir emas,bir nechta shartlarni tekshirish va ulardan biri bajarilganda dastur to'xtash talab qilinshi mn, shunda flag(0'zgaruvchan ishora) dan foydalanamiz

#print("Kiritilgan sonni kvadratini qaytaruvchi dastur.")
#savol = "Istalgan sonni kiriting"
#savol += "(Dastur to'xtashi un 'exit' deb yozing)"
#ishora = True
#while ishora:
 #   nat = input(savol)
 #   if nat == "exit":
 #       ishora = False
 #   else:
 #       print(float(nat)**2)

#print("Dastur to'xtadi!")

#5.Break operatori for siklini to'xtatish un ham ishlatilinadi
# while sikli ichida bir nechta break operatori bo'lishi ham mumkin
sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:#son 5 ga teng bo'lsa kod to'xtaydi
        break
    print(f"{son} ning kvadrati {son **2} ga teng\n")


#6. continiue operatori esa aksincha, malum bir shart bajarilinganda bir bergan qiymatni sakrab o'tish un berilgan
sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:#son 5 ga teng bo'lsa kod to'xtaydi
        continue
    print(f"{son} ning kvadrati {son **2} ga teng")

# Y8uqoridagi qiymatda 5 soniga kelganda 5 ni ko'rsatmasdan davom etib ketadi

soni = 0
while soni<10:
    soni +=1
    if soni%2!=0: #10  gacha bo'lgan juft sonlarni ko'rish un 
    #if soni%2==0: #10  gacha bo'lgan toq sonlarni ko'rish un 
        continue
    else:
        print(soni)
        
#7. ABadiy tsikl tuzoqi
# Abadiy tsikl - mantiqiy xatolar sabab yuzaga keladi
#noto'g'ri shart,o'zgarmas qiymat, kodlar ketma-ketligidagi xatoliklar va hkz.

# abadiy codeni to'xtatish un ctrl + c ni bosamiz



#  Amaliyot
#1.Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating

#print("Foydalanuvchining sevimli kitoblarini ko'rsatadigan program.")
#savol = "Sevimli kitobingizni kiriting"
#savol += "(Dastur to'xtashi un 'stop' deb yozing)"
#ishora = True
#while ishora:
 #   kitob = input(savol)
 #   if kitob == "stop":
 #       ishora = False
 #   else:
 #       print(f"Sevimli kitobingizni nomi: {kitob.title()} ekan.Bu juda Yaxshi kitob\n")

#print("Dastur to'xtadi!")

#2.Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).

##print("Bu dastur yoshga qarab, chipta narxini belgilab beradi.")
#prompt = "\nYoshingizni kiriting (to'xtatish uchun 'exit' yoki 'quit'): "

#while True:
#    yoshi = input(prompt).strip().lower()
    
    # chiqish sharti
#    if yoshi in ("exit","quit"):
#        print("Dastur to'xtatildi, Xayr")
#        break
    
    # Raqam ekanligi
#    if not yoshi.isdigit():
#        print("Iltimos faqat son kiriting")
#        continue
#    yosh = int(yoshi)
    
    # Narxni aniqlash
#    if yosh <7:
   #     price =1000
#    elif yosh <= 18:
  #      price=2000
#    elif yosh <=65:
#        price=3000
  #  else:
  #      price = 0
  #      print(f"Siz {yosh} dasiz va sizga kirish Bepul")
   #     continue
 #   print(f"Siz {yosh} yoshdasiz - chipta narxi: {price} so'm")

#.isdigit() — stringdagi barcha belgilar raqam ekanini tekshiradi.
#.strip() — stringning bosh va oxiridagi bo'sh joylarni olib tashlaydi.


#3.Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?


savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol).strip().lower()
    
    if qiymat in ("exit"):
        print("Dastur Yakulnadi,Xayr")
        break
    
    if not qiymat.isdigit():
        print("Iltimos faqat raqam kiriting")
        continue
    qiymati = int(qiymat)
    if qiymati<0:
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng\n")




