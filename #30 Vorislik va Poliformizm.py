# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Mon Jul 13 19:30:56 2026

# @author: mirzo
# """

# #30 VORISLIK VA POLIMORFIZM
# #SUPER KLASS VA VORIS KLASS
# Obyektga yo'naltirilgan dasturlashning qulayliklaridan biri bu klasslardan boshqa klass yaratish imkoniyati. Bizga kerak bo'lgan yangi klass, avval yaratilgan boshqa klass bilan o'xshashlik joylari bo'lsa, biz bu klassdan voris klass yaratishimiz mumkin. Bunda asl klass - ota, yoki super klass deb ataladi. 
# Super klassdan yaratilgan voris klass otaning barcha yoki tanlangan xususiyatlari va metodlarini meros olish bilan birga, o'ziga xos xususiyat va metodlariga ega bo'ladi.
# Keling boshlanishiga Shaxs klassini yaratamiz, bu klassimiz keyinchalik boshqa klasslar uchun super klass vazifasini bajaradi:

# Copy
# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#     def __init__(self,ism,familiya,passport,tyil):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil
    
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info
        
#     def get_age(self,yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil
# Klassimizni tekshirib ko'ramiz:

# Copy
# inson = Shaxs("Hasan","Alimov","FB001122",1995)
# print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")
# Natija: Hasan Alimov. Passport:FB001122, 1995-yilda tug`ilgan. 26 yoshda.



# VORIS KLASS YARATISH
# Endi avvalgi darsimizda yaratgan Talaba klassimizni qaytadan yaratamiz. Bu safar, avvalgidan farqli ravishda, Talaba ni yaratishda, Shaxs dan super klass sifatida foydalanamiz:

# Copy
# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
# Kodimizni tahlil qilaylik:
# 1-qatorda klass nomidan so'ng, qavs ichida super klass nomini berdik
# 5-qatorda (def __init__ ichida) klassimiz super klassning xususiyatlarini meros olishini ko'rsatdik 
# Yangi yaratgan Talaba klassimiz Shaxsning barcha xususiyatlari va metodlariga ega bo'ladi.

# Copy
# talaba = Talaba("Valijon","Aliyev","FA112299",2000)
# print(talaba.get_info())
# Natija: Valijon Aliyev. Passport:FA112299, 2000-yilda tug`ilgan
# Talaba klassi uchun alohida get_info() metodini yozmagan bo'lsakda, bu metod Talabaga Shaxsdan meros o'tdi.
# Huddi shu kabi get_age() metodiga ham murojat qilishimiz mumkin:

# Copy
# >>>print(talaba.get_age(2021))
# 21
# Dastur davomida super klass voris klasslardan avval yozilgan (chaqirilgan) bo'lishi kerak.