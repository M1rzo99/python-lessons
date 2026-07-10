# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Fri Jul 10 13:16:09 2026

# @author: mirzo
# """

# XUSUSIYATLARGA STANDART QIYMAT BERISH
# Avvalgi darsizmida biz klass yaratish, unga xususiyatlar va metodlar qo'shishni ko'rdik. Klassdan obyekt yaratganimizda esa uning xususiyatlarini parametr sifatida uzatishni o'rgandik.
# Pythonda obyektning ba'zi xususiyatlarini parametr yordamida uzatmasdan, klass yaratishda unga standart qiymat berib ketishimiz mumkin. Keling, Talaba klassimizga qaytamiz. Bu klassimiz 3 ta xususiyatga ega edi: ism, familiya, tyil. Biz yana bitta qo'shimcha, bosqich nomli xususiyat qo'shamiz, va unga standart qiymat sifatida 1 beramiz, e'tibor qiling bu xususiyat obyekt yaratilishida parametr sifatida uzatilmaydi:

# Copy
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

# Copy
# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_info())
# Natija: Alijon Valiyev. 1-bosqich talabasi
# STANDART QIYMATNI O'ZGARTIRISH
# Obyektning standart qiymatiga ham boshqa xususiyatlar kabi nuqta orqali murojat qilishimiz va uning qiymatini almashtirishimiz mumkin:

# Copy
# talaba1.bosqich= 2
# print(talaba1.bosqich)
#   Natija: 2
# Yana boshqa usuli, obyekt xususiyatini yangilovchi metod yozish.

# Copy
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

# Copy
# talaba1.set_bosqich(3)
# print(talaba1.get_info())
# Natija: Alijon Valiyev. 3-bosqich talabasi
# Umuman olganda xususiyatlarni yangilashda turli usullardan foydalanish mumkin. Misol uchun talabaning bosqichi odatda 1 tadan ko'payib boradi, shuning uchun quyidagicha metod ham yozishimiz mumkin:

# Copy
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

# Copy
# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_info())

# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())
# Natija: Alijon Valiyev. 1-bosqich talabasi

# Copy
# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())
# Natija: Alijon Valiyev. 2-bosqich talabasi

# Copy
# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())
# Natija: Alijon Valiyev. 3-bosqich talabasi