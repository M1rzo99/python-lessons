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

    #2.KALIT SO'Z BILAN UZATISH
Yuqoridagi kabi holatlarning oldini olish uchun argumentlarni parametr nomi bilan qo'shib uzatishimiz mumkin. Buning uchun funksiyaga o'zgartirish kiritish talab qilinmaydi.

Copy
yosh_hisobla(tugilgan_yil=1997, ism='olim')
Natija: Olim 23 yoshda
Yuoqirdagi misolda funksiyani chaqirishda biz parametrlar ketma-ketligiga rioya qilmagan bo'lsakda, argumentlarni parametr_nomi=qiymat ko'rinishida yozganimiz sababli funksiya to'g'ri ishladi. 
Huddi shu kabi yuqoridagi toliq_ism funksiyasiga murojat qilishimiz mumkin:

Copy
toliq_ism(familiya='hakimov',ism='olim')
Natija:
Foydalanuvchi ismi: Olim
Foydalanuvchi familiyasi: Hakimov
Kalit so'z usulidan foydalanganda parametr nomi to'g'ri yozilganiga ahamiyat bering.
STANDART QIYMAT
Funksiya yaratishda, istalgan parametr uchun standart qiymat ko'rsatib ketishimiz mumkin. Agar foydalanuvchi shu parametr uchun qiymat (argument) kiritmasa, funksiya bajarilishi jarayonida standart qiymat ishlatiladi. Standart qiymatni funksiya yaratish vaqtidaparametr = qiymat ko'rinishida beriladi.

Copy
def yosh_hisobla(tugilgan_yil, joriy_yil=2020): # joriy yil uchun st.qiymat 2020
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
Yuqoridagi misolda biz joriy_yil parametriga 2020 standart qiymatini berib ketdik. 
Funksiya yaratishda, standart qiymatga ega parametrlar doim oxirida yozilishi kerak. Aks holda xatolik yuzaga keladi.
Keling avval funksiyani ikkala argument bilan chaqiramiz:

Copy
yosh_hisobla(1995,2020)
Natija: Siz 25 yoshdasiz
Endi esa faqat bitta argument (tugilgan_yil) bilan chaqiramiz:

Copy
yosh_hisobla(1993)
Natija: Siz 27 yoshdasiz
Bu safar foydalanuvchi joriy_yil ni kiritmagani sababli, standart qiymat, 2020 ishlatildi. 
FUNKSIYAGA MUROJAT QILISHDA XATOLIKLAR
Funksiyalarga murojat qilishda turli xatoliklarga yo'l qo'shimiz tabiiy. Bunday holatlarda Python qaytargan xatoni sinchiklab o'qib, xato qayerdaligini topishimiz va uni to'g'rilashimiz zarur. Quyida men avvalroq yaratgan funksiyalarimizni xato usullar bilan chaqiraman. Xato nimada ekanini topa olasizmi?

Copy
def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
tyil = input("Tug'ilgan yilingizni kiriting: ")
yosh_hisobla(tyil)
Natija: TypeError: unsupported operand type(s) for -: 'int' and 'str'

Copy
def yosh_hisobla(tugilgan_yil, joriy_yil):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

yosh_hisobla(1993)
Natija: TypeError: yosh_hisobla() missing 1 required positional argument: 'joriy_yil'

Copy
def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!")

salom_ber('hasan')
Natija: TypeError: salom_ber() takes 0 positional arguments but 1 was given

Copy
def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
 
 toliq_ism('olim hakimov')
Natija: TypeError: toliq_ism() missing 1 required positional argument: 'familiya'









