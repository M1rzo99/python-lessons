# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Thu May 28 21:48:28 2026

# @author: mirzo
# """

# Funkaiya  - malum bir vazifani bajarishga mo'ljallangan kodlar yig'indisi.

# Biz shu paytgacha bir nechta functionlardan foydalanaib keldik:
# range(1,20) malum bir oraliqdagi sonlarni yaratish un
# .title() Birinchi harfi katta bo'lishi un. Va hkz,
# Dastur davomida bir xil kodlarni takror yozmaslik un funksiya ishlatamiz

#Funksiyalar turlicha bo'ladi. Sizdan qiymat qabul qilib,qabul qilgan qiymat ustida turlixil amallarni bajaradi, foydalanuvchidan umuman qiymat qabul qilmaydigan functionlar ham bor.

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalom alaykum!")
# salom_ber()


# Function foydalanuvchi ismini qabul qilib,uning ismi bilan murojat qilsin.

# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib,Salom beruvchi funksiya"""
#     print(f"Assalom alaykum, hurmatli {ism.title()}!")
# salom_ber("Mirzo")
# agar function ishklatishda unga qiymat bermasak salom_ber() xatolik yuzaga keladi



# DocString  - biz yozgan functionimiz haqioda malumot hisoblanadi. Dasturchi bir function yozsa,shu fufnction haqida malumot berish kerak. 

def salom_ber(ism):
    """Foydalanuvchi ismini qabul qilib,Salom beruvchi funksiya"""
    print(f"Assalom alaykum, hurmatli {ism.title()}!")
salom_ber("Mirzo")



print(salom_ber.__doc__)














