 #!/usr/bin/env python3
 # -*- coding: utf-8 -*-
 # """
 # Created on Fri Jul 10 13:16:09 2026

 # @author: mirzo
 # """

# Xususiyatlarga standart qiymat berish: 
 # Pythonda obyektning bzi xususiyatlarini parametr uzatmasdan, klass yaratishda undega standart qiymat berib ketish mn
# Keling Talaba klassga qaytamiz. Bu klassimiz 3 ta ususiyatga eda: ism,familya,Tyil.Biz bosqich nomli xususiyat qo'shamiz.
#Unga standart qiymat sifatida 1 beramiz. E'tibor bersak bu  xususiyat obyekt yaratilishda parametr sifatida uzatilmaydi.

class Talaba:
    """ Talaba nomli class Yaratayapmiz"""
    def __init__(self,ism,familya,Tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familya = familya
        self.Tyil = Tyil
        self.bosqich = 1 # Xususiyatga standart qiymat berish shudir
    def get_info(self):
        return f"{self.ism} {self.familya} {self.Tyil}-yil, {self.bosqich}-bosqich talabasi"
talaba1 = Talaba("Jumanazar", "Shokirov", "2002")
print(talaba1.get_info())
        
class Sabzavotlar:
    def __init__(self,nomi,turi,kilo):
        self.nomi= nomi
        self.turi = turi
        self.kilo = kilo
        self.narx = 2000
        self.yet_joy = "Katta dalada yetishtilgan"
    def get_inf(self):
        return f"{self.nomi} {self.turi}, {self.kilo}.{self.yet_joy}, Uning narxi {self.narx} won."
maxsulot1 = Sabzavotlar("Piyoz", "Qizil", "5kg")
print(maxsulot1.get_inf())


# Standart qiymatni o'zgartirish:
# Obyektnnig standart qiymatioga ham boshqa xususiyatlar kabi nuqta orqali murojat qilishimiz va uning qiymatini almashtirishmiz mumkin:
talaba1.bosqich = 2
talaba1.ism = "Mirzo"
print(talaba1.get_info())

# Yana boshqa usuli,obyekt xususiyatlarini yangilovchi method yaratish:
class Talaba:
    """ Talaba nomli class Yaratayapmiz"""
    def __init__(self,ism,familya,Tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familya = familya
        self.Tyil = Tyil
        self.bosqich = 1 # Xususiyatga standart qiymat berish shudir
    def get_info(self):
        return f"{self.ism} {self.familya} {self.Tyil}-yil, {self.bosqich}-bosqich talabasi"
    
    def set_bosqich(self,bosqich):
        self.bosqich = bosqich
        
        
talaba1 = Talaba("Jumanazar", "Shokirov", "2002")
talaba1.set_bosqich(10)
print(talaba1.get_info())

# Xususiyatlarni yangilashda turli xil usullardan foydalanish mumkin. Misol un talabaning bosqichi odatda + 1 ga  ko'payib boradi yil o'tgan sayin
# shuning un quyidagi method ham yozishn mumkin

class Talaba:
    """ Talaba nomli class Yaratayapmiz"""
    def __init__(self,ism,familya,Tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familya = familya
        self.Tyil = Tyil
        self.bosqich = 1 # Xususiyatga standart qiymat berish shudir
    def get_info(self):
        return f"{self.ism} {self.familya} {self.Tyil}-yil, {self.bosqich}-bosqich talabasi"
    
    def set_bosqich(self,bosqich):
        self.bosqich = bosqich
        
        
    def update_bosqich(self):
        self.bosqich +=1
        
talaba1 = Talaba("Jumanazar", "Shokirov", "2002")
print(talaba1.get_info())

talaba1.update_bosqich()
print(talaba1.get_info())

talaba1.update_bosqich()
print(talaba1.get_info())

talaba1.update_bosqich()
print(talaba1.get_info())

















