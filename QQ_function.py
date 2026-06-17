# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sat May 30 22:20:57 2026

# @author: mirzo
# """

# Qiymat qaytaruvchi funksiya

# def toliq_ism_yasa(ism,familya):
#     """ Toliq  ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familya}"
#     return toliq_ism
# user1 = toliq_ism_yasa("Mirzo", "Shomuratov")
# user2 = toliq_ism_yasa("Asliddin", "Uzoqov")
# print(user2,user1)

# # Return  - o'zgaruvchining qiymatini qaytaradi.

# # Ixtiyoriy argumentlar - parametrga kiritgan malumotni yoki argumentini beramiz, yokida bermaymiz

# def oila_ism_yasa(ism,familya,oilada_kim=""):
#     """ Oila azosi nomi va oilada kimligi ko'rsatuvchi function"""
#     if oilada_kim:#oiladagi rolini tekshiramiz
#         oilada_azo = f"{ism} {familya} {oilada_kim}"
#     else:
#         oilada_azo = f"{ism} {familya}"
#     return oilada_azo.title()
# shaxs1 = oila_ism_yasa("Aziza", "SHomuratova")
# print(shaxs1)

# # Funksiyadan Lug'at qaytaramiz

# def avto_info(komponiya,model,rangi,karobka,yili,narx=None):
#     avto ={
#         'komponiya':komponiya,
#         'model':model,
#         'rangi':rangi,
#         'karobka':karobka,
#         'yili':yili,
#         'narx':narx
#         }
#     return avto
# avto1 = avto_info("KIA", "K9", "Qora", "Avtomat", 2025,220000)
# avtolar = [avto1]
# print("Onlayn  bozordagi mavjud mashinalar:")
# for avto in avtolar:
#     if avto["narx"]:
#         narx = avto["narx"]
#     else:
#         narx = "Nomalum"
#     print(f"{avto['model']}, {avto['komponiya']}. Narxi:{narx}")

# # Funksiyadadn ro'yhat qaytaramiz
# # oraliq nomli function yasaymiz va functionimiz 2 son oralig'idagi sonlarni ro'yhat ko'rinishda qaytaradi.
# def oraliq(min,max,qadam):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar
# print(oraliq(0,11,2))

# # FUNKSIYALARNI TSIKLDA ISHLATISH
# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
# print(avtolar)


# Amaliyot

#1. Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil

def mijoz_info(ism, familiya, tyil, tjoy, email="", tel=None):
    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    mijoz = {
        "ism": ism,
        "familiya": familiya,
        "tyil": tyil,
        "yoshi": 2020 - tyil,
        "tjoy": tjoy,
        "email": email,
        "telefon": tel,
    }
    return mijoz

print("Mijoz haqida ma'lumotlarni kiriting.")
mijozlar =[]
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    telefon = input("Telefon raqami: ")
    mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
    javob = input("Davom etasizmi? (ha/yo'q)")
    if javob!='ha':
        break

print("Mijozlar:")
for mijoz in mijozlar:
    print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()}," 
          f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")
   
#2.Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
def kattasi(x,y,z):
    max = x
    if y>=max:
        max = y
    if z>=max:
        max = z
    return max
   
#3.Amaliyot 3 
def katta_harf(matnlar):
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()
    return matnlar
ismlar = ["ali", "vali", "hasan", "husan"]
yangi_ismlar = katta_harf(ismlar)
print(ismlar)

print(yangi_ismlar)

#4. Amaliyot 4


def aylana_info(radius, pi=3.14159):
    aylana = {
        "radius": radius,
        "diametr": 2 * radius,
        "perimetr": 2 * radius * pi,
        "yuza": pi * radius ** 2,
    }
    return aylana





