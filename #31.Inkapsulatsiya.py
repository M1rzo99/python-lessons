# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Wed Jul 15 22:39:23 2026

# @author: mirzo
# """

# INKAPSULYATSIYA
# Obyektga Yo'naltirilgan Dasturlashning tamoyillaridan biri bu inkapsulyatsiya, ya'ni obyektning xususiyatlarga to'g'ridan-to'g'ri (nuqta orqali) murojat qilishni va ularning qiymatini o'zgartirishni taqiqlab qo'yish. Pythonda bunday yopiq xususiyatlarning nomi ikki pastki chiziq bilan boshlanadi:

# Copy
# from uuid import uuINKAPSULYATSIYA
# Obyektga Yo'naltirilgan Dasturlashning tamoyillaridan biri bu inkapsulyatsiya, ya'ni obyektning xususiyatlarga to'g'ridan-to'g'ri (nuqta orqali) murojat qilishni va ularning qiymatini o'zgartirishni taqiqlab qo'yish. Pythonda bunday yopiq xususiyatlarning nomi ikki pastki chiziq bilan boshlanadi:

# Copy
# from uuid import uuid4
# class Avto:
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
    
#     def get_km(self):
#         return self.__km
    
#     def get_id(self):
#         return self.__id
# Yuqoridagi kodimizning 11-qatorida __km xususiyati avtomobilning necha km yurgani haqida ma'lumot saqlaydi va bu ma'lumotni tashqaridan o'zgartirib bo'lmaydi. Kodimizning 12-qatorida esa har bir yangi yaratilgan avtomobilga yangi, noyob va takrorlanmas ID generasiya qilish uchun uuid4() funksiyasidan foydalanayapmiz. Deylik biz mashinalar sotish uchun onlayn bozor yaratsak, bozorimizga qo'shilgan har bir moshina endi o'zining ID raqamiga ega bo'ladi va bu ID raqamni to'g'ridan-to'g'ri (nuqta orqali) ko'rib bo'lmaydi.

# Copy
# avto1 = Avto("GM","Malibu","Qora",2020,40000,100000)
# avto1.__km
#  Natija: AttributeError: 'Avto' object has no attribute '__km'
# Yopiq xususiyatlarni ko'rish uchun esa alohida metodlar yozish maqsadga muvofiq bo'ladi (get_km() va get_id()):

# Copy
# print(f"ID: {avto1.get_id()}")
# Natija: ID: 1d4f39a4-3222-4682-9231-6275ca5e1bff
# Bunday yopiq xususiyatlarni o'zgartirish ham metodlar orqali amalga oshirilishi kerak. Misol uchun mashinaning necha km yurganini o'zgartirish uchun klassimizga quyidagi metodni qo'shamiz:

# Copy
#     def add_km(self,km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km>=0:
#             self.__km += km
#         else:
#             print("Mashina km kamaytirib bo'lmaydi")

# Copy
# avto1.add_km(1500)
# print(avto1.get_km())
# Natija: 101500
# Inkapsulyatsiyaning maqsadi obyektning ma'lum xususiyatlarini tashqi ta'sirdan himoya qilish. Misol uchun yuqoridagi misolimizda mashinaning qancha yurganini faqat musbat tarafga o'zgartirish mumkin, noyob ID raqamini esa umuman o'zgartirib bo'lmaydi.id4
# class Avto:
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
    
#     def get_km(self):
#         return self.__km
    
#     def get_id(self):
#         return self.__id
# Yuqoridagi kodimizning 11-qatorida __km xususiyati avtomobilning necha km yurgani haqida ma'lumot saqlaydi va bu ma'lumotni tashqaridan o'zgartirib bo'lmaydi. Kodimizning 12-qatorida esa har bir yangi yaratilgan avtomobilga yangi, noyob va takrorlanmas ID generasiya qilish uchun uuid4() funksiyasidan foydalanayapmiz. Deylik biz mashinalar sotish uchun onlayn bozor yaratsak, bozorimizga qo'shilgan har bir moshina endi o'zining ID raqamiga ega bo'ladi va bu ID raqamni to'g'ridan-to'g'ri (nuqta orqali) ko'rib bo'lmaydi.

# Copy
# avto1 = Avto("GM","Malibu","Qora",2020,40000,100000)
# avto1.__km
#  Natija: AttributeError: 'Avto' object has no attribute '__km'
# Yopiq xususiyatlarni ko'rish uchun esa alohida metodlar yozish maqsadga muvofiq bo'ladi (get_km() va get_id()):

# Copy
# print(f"ID: {avto1.get_id()}")
# Natija: ID: 1d4f39a4-3222-4682-9231-6275ca5e1bff
# Bunday yopiq xususiyatlarni o'zgartirish ham metodlar orqali amalga oshirilishi kerak. Misol uchun mashinaning necha km yurganini o'zgartirish uchun klassimizga quyidagi metodni qo'shamiz:

# Copy
#     def add_km(self,km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km>=0:
#             self.__km += km
#         else:
#             print("Mashina km kamaytirib bo'lmaydi")

# Copy
# avto1.add_km(1500)
# print(avto1.get_km())
# Natija: 101500
# Inkapsulyatsiyaning maqsadi obyektning ma'lum xususiyatlarini tashqi ta'sirdan himoya qilish. Misol uchun yuqoridagi misolimizda mashinaning qancha yurganini faqat musbat tarafga o'zgartirish mumkin, noyob ID raqamini esa umuman o'zgartirib bo'lmaydi.INKAPSULYATSIYA
# Obyektga Yo'naltirilgan Dasturlashning tamoyillaridan biri bu inkapsulyatsiya, ya'ni obyektning xususiyatlarga to'g'ridan-to'g'ri (nuqta orqali) murojat qilishni va ularning qiymatini o'zgartirishni taqiqlab qo'yish. Pythonda bunday yopiq xususiyatlarning nomi ikki pastki chiziq bilan boshlanadi:

# Copy
# from uuid import uuid4
# class Avto:
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
    
#     def get_km(self):
#         return self.__km
    
#     def get_id(self):
#         return self.__id
# Yuqoridagi kodimizning 11-qatorida __km xususiyati avtomobilning necha km yurgani haqida ma'lumot saqlaydi va bu ma'lumotni tashqaridan o'zgartirib bo'lmaydi. Kodimizning 12-qatorida esa har bir yangi yaratilgan avtomobilga yangi, noyob va takrorlanmas ID generasiya qilish uchun uuid4() funksiyasidan foydalanayapmiz. Deylik biz mashinalar sotish uchun onlayn bozor yaratsak, bozorimizga qo'shilgan har bir moshina endi o'zining ID raqamiga ega bo'ladi va bu ID raqamni to'g'ridan-to'g'ri (nuqta orqali) ko'rib bo'lmaydi.

# Copy
# avto1 = Avto("GM","Malibu","Qora",2020,40000,100000)
# avto1.__km
#  Natija: AttributeError: 'Avto' object has no attribute '__km'
# Yopiq xususiyatlarni ko'rish uchun esa alohida metodlar yozish maqsadga muvofiq bo'ladi (get_km() va get_id()):

# Copy
# print(f"ID: {avto1.get_id()}")
# Natija: ID: 1d4f39a4-3222-4682-9231-6275ca5e1bff
# Bunday yopiq xususiyatlarni o'zgartirish ham metodlar orqali amalga oshirilishi kerak. Misol uchun mashinaning necha km yurganini o'zgartirish uchun klassimizga quyidagi metodni qo'shamiz:

# Copy
#     def add_km(self,km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km>=0:
#             self.__km += km
#         else:
#             print("Mashina km kamaytirib bo'lmaydi")

# Copy
# avto1.add_km(1500)
# print(avto1.get_km())
# Natija: 101500
# Inkapsulyatsiyaning maqsadi obyektning ma'lum xususiyatlarini tashqi ta'sirdan himoya qilish. Misol uchun yuqoridagi misolimizda mashinaning qancha yurganini faqat musbat tarafga o'zgartirish mumkin, noyob ID raqamini esa umuman o'zgartirib bo'lmaydi.