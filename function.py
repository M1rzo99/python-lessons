# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Thu May 28 21:48:28 2026

# @author: mirzo
# """

# Funksiya  - malum bir vazifani bajarishga mo'ljallangan kodlar yig'indisi.

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
# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib,Salom beruvchi funksiya"""
#     print(f"Assalom alaykum, hurmatli {ism.title()}!")
# salom_ber("Mirzo")

# Quyidagi buyruq orqali functionimiz haqida malumotlarni olsak bo'ladi.
print(salom_ber.__doc__)

# Functionga bir necha bor murojat qilish

def salom_ber(ism):
    """Foydalanuvchi ismini qabul qilib,Salom beruvchi funksiya"""
    print(f"Assalom alaykum, hurmatli {ism.title()}!")
salom_ber("Mirzo")
salom_ber("Latif")
# Biz function tuzib, unni bir nechta marta takror ishlatsak bo'ladi.Tepadagidek.


# Argument va Parameter
# Function yaratishda, qavs ichida berilgan,funciton to'g'ri ihslashi un uzatiladigan qiymat parameter ddi. 
# Yuqoridagi misolda ism, salom_ber functionini parametri hisoblanadi

# Foydalanuvchi functionga murojat qilishda functionga uzatiladigan qiymat esa argument deb ataladi.
#salom_ber("hasan") kodida "hasan" bu argumentdir.

# Funcitonga bir nechta argument uzatish mn:
    #1. To'g'ri tartibda uzatish:
     # Function parametrlari qaysi tartibda yozilgan bo'lsa,argumentlar ham aynana shu ketma-ketlikda uzatilishi kerak.
    # Quyidagi functionda foydalanuvchining ism va familiyasini parametr sifatida qabul qilib, ularni jamlab uzatishi kerak.
def toliq_ism(ism,fam):
    """ FOydalanuvchi ism va familiyasini chiqardadigan funksiya"""
    print(f"FOydalanuvchi ismi: {ism.title()}\n"
          f"FOydalanuvchi familiyasi: {fam.title()}")
toliq_ism("Mirzo","SHomuratov")
    
def toliq_ism(ism,yosh):
    """ FOydalanuvchi ism va yoshini chiqardadigan funksiya"""
    print(f"FOydalanuvchi ismi: {ism.title()}, {2026-yosh} yoshda")
toliq_ism("Mirzo",1999)
    #









