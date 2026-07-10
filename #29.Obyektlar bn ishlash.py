# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Fri Jul 10 13:16:09 2026

# @author: mirzo
# """

# XUSUSIYATLARGA STANDART QIYMAT BERISH
# Avvalgi darsizmida biz klass yaratish, unga xususiyatlar va metodlar qo'shishni ko'rdik. Klassdan obyekt yaratganimizda esa uning xususiyatlarini parametr sifatida uzatishni o'rgandik.
# Pythonda obyektning ba'zi xususiyatlarini parametr yordamida uzatmasdan, klass yaratishda unga standart qiymat berib ketishimiz mumkin. Keling, Talaba klassimizga qaytamiz. Bu klassimiz 3 ta xususiyatga ega edi: ism, familiya, tyil. Biz yana bitta qo'shimcha, bosqich nomli xususiyat qo'shamiz, va unga standart qiymat sifatida 1 beramiz, e'tibor qiling bu xususiyat obyekt yaratilishida parametr sifatida uzatilmaydi:


# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
# Endi, Talaba klassidan yangi obyekt yaratganimizda har bir yangi talabaning kursi 1 ga teng bo'ladi.


# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_info())
# Natija: Alijon Valiyev. 1-bosqich talabasi
# STANDART QIYMATNI O'ZGARTIRISH
# Obyektning standart qiymatiga ham boshqa xususiyatlar kabi nuqta orqali murojat qilishimiz va uning qiymatini almashtirishimiz mumkin:


# talaba1.bosqich= 2
# print(talaba1.bosqich)
#   Natija: 2
# Yana boshqa usuli, obyekt xususiyatini yangilovchi metod yozish.

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
#     def set_bosqich(self,bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
# Metodga murojat qilamiz:


# talaba1.set_bosqich(3)
# print(talaba1.get_info())
# Natija: Alijon Valiyev. 3-bosqich talabasi
# Umuman olganda xususiyatlarni yangilashda turli usullardan foydalanish mumkin. Misol uchun talabaning bosqichi odatda 1 tadan ko'payib boradi, shuning uchun quyidagicha metod ham yozishimiz mumkin:


# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
#     def set_bosqich(self,bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
        
#     def update_bosqich(self):
#         """Talabanining bosqichini 1taga ko'paytirish"""
#         self.bosqich += 1
# update_bosqich() metodiga murojat qilganimizda talabning bosqichi oshib boradi:


# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_info())

# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())
# Natija: Alijon Valiyev. 1-bosqich talabasi


# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())
# Natija: Alijon Valiyev. 2-bosqich talabasi


# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())
# Natija: Alijon Valiyev. 3-bosqich 


# OBYEKTLAR O'RTASIDA MUNOSABAT
# Obyektga yo'naltirilgan dasturlashning afzalligi, turli obyektlar o'rtasida o'zaro munosabatlarni oson yo'lga qo'yish mumkinligida. Buni misolda ko'rish uchun, yangi Fan degan klass yaratamiz va fanimizga talabalar qo'shish imkoniyatini ham yaratamiz (add_student() metodi):


# class Fan():
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
# E'tibor bering, Fan klassi faqatgina yagona nomi degan parametrga ega. Qolgan xususiyatlariga esa standart qiymat berilgan: talabalar soni (self.talabalar_soni) 0 ga teng, talabalar ro'yxati (self.talabalar) esa bo'sh.
# Fanimizga talaba qo'shish uchun add_student() metodini chaqiramiz. Bu metod parametr sifatida Talaba obyektini qabul qiladi va uni talabalar ro'yxatiga qo'shadi. Shuningdek, bu metod yangi talaba qo'shilganda talabalar_soni ni 1 taga oshirib qo'yadi.
# Keling boshlanishiga yangi fan obyektini va bir nechta talabalarni yaratamiz:


# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Alijon","Valiyev",2000)
# talaba2 = Talaba("Hasan","Alimov",2001)
# talaba3 = Talaba("Akrom","Boriyev",2001)
# Talabalarni yangi fanimizga qo'shamiz:


# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)
# Mana, fanimiz tayyor, talabalar qo'shildi. Keling endi fan haqida ma'lumotlarni olamiz:


# print(matematika.talabalar_soni)
# Natija: 3
# Fanimizga 3 ta talaba qo'shilibdi. Talabalar haqida ma'lumot olsak bo'ladimi?


# print(matematika.talabalar)
# Natija: [<__main__.Talaba object at 0x000001AB08939588>, <__main__.Talaba object at 0x000001AB089397C8>, <__main__.Talaba object at 0x000001AB087D9F08>]
# Talabalarning ismi familiyasi o'rniga qandaydur tushunarsiz ma'lumotlar. Aslida hammasi to'g'ri, yuqorida fanimizga yangi talabalarni obyekt sifatida qo'shgan edik, yuqoridagi natija esa matematika.talabalar ro'yxatida Talaba klassiga oid 3 ta obyekt borligini ko'rsatayapti. 
# Fanimizga yozilgan talabalar haqida tushunarli ma'lumot olish uchun esa Fan klassiga yana bir, get_students() degan, yangi metod qo'shamiz. Bu metod talabalar ichidagi har bir talaba obyektiga murojat qilib, get_info() metodi yordamida talabaning ma'lumotlarini oladi, ro'yxatga qo'shadi va shu ro'yxatni qaytaradi:


# class Fan():
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
    
#     def get_students(self):
#         return [talaba.get_info() for talaba in self.talabalar]
# Shu o'rinda Pythonda ro'yxatlar bilan ishlashning qulayliklaridan birini ham ko'rsatib o'tsak. Yuqoridagi kodimizning 13-qatorida e'tibor bersangiz, biz yangi ro'yxat shakllantirishda 1 qator koddan foydalandik:

# [talaba.get_info() for talaba in self.talabalar]
# Kodimizni tahlil qilsak, self.talabalar ichidagi har bir talaba uchun get_info() metodini bajar degan ma'no kelib chiqadi. Kodni kvadrat qavslar ichiga olganimiz uchun esa, har bir tsikl natijasi avtomat ravishda ro'yxatga qo'shib boriladi. 
# Mana endi metodga murojat qilib, talabalar haqida ma'lumot olishimiz mumkin:


# mat_talabalar = matematika.get_students()
# print(mat_talabalar)
# ['Alijon Valiyev. 1-bosqich talabasi ', 'Hasan Alimov. 1-bosqich talabasi ', 'Akrom Boriyev. 1-bosqich talabasi ']
# Shunday qilib biz ikki bir-biriga bog'liq bo'lmagan obyektlar ustida turli munosabatlar o'rnatishimiz mumkin.