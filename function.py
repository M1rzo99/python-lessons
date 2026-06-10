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
# print(salom_ber.__doc__)

# Functionga bir necha bor murojat qilish

# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib,Salom beruvchi funksiya"""
#     print(f"Assalom alaykum, hurmatli {ism.title()}!")
# salom_ber("Mirzo")
# salom_ber("Latif")
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
    
    #2.KALIT SO'Z BILAN UZATISH
#Yuqoridagi kabi holatlarning oldini olish uchun argumentlarni parametr nomi bilan qo'shib uzatishimiz mumkin. Buning uchun funksiyaga o'zgartirish kiritish talab qilinmaydi.

def toliq_ism(ism='Mirzo',yili=1999):
    """ FOydalanuvchi ism va yoshini chiqardadigan funksiya"""
    print(f"FOydalanuvchi ismi: {ism.title()}, {2026-yili} yoshda")
toliq_ism()


#3. standart qiymat bilan uzastish
# funksiya yaratishda,istalgan parametr un standart qiymat ko'rsatib ketishimiz mn.Agar foydalanuvchi shu parametr un argument kiritmasa,
# funksiya bajarilinayotgandan shu standart qiymatni ishlatadi.

# def yosh_hisobla(tug_yil,joriy_yil=2026):
#     """ Foydalanuvchi tugilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil - tug_yil} yoshdasiz hazrat!")
# yosh_hisobla(1999)

#AMALIYOT
#1.Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
def ism_yosh_korsat(ism,yosh):
    """ Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya"""
    print(f"{ism.title()}, sizning yilingiz {2026-yosh} dir hazrat!")
ism_yosh_korsat('Mirzo', 27)

#2.Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
def kv_kub_aniqla(son):
    """Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya """
    print(f"{son} ning kvadrati {son**2} dir.Va "
          f"{son} ning kubi {son**3} dir.")
kv_kub_aniqla(2)   

#3.Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
def juft_toq_aniqla(son):
    """Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya"""
    son=0
    if son ==1/0.5:
        print("Juft son")
    else:
        print("Toq son")
juft_toq_aniqla(1)

#4.Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
def son_katta_kichik_aniqla(son1,son2):
    """Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya """
    son=0
    if son1>=son2:
        print(f"{son1} {son2} dan katta.")
    elif son1<=son2:
        print(f"{son2} {son1} dan kichik.")
    else:
        print("Sonlar bir-biriga teng.")
son_katta_kichik_aniqla(1, 3)













