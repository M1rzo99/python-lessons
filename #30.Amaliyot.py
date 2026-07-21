#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 20:14:33 2026

@author: mirzo
"""

# Amaliyot #30-dars
#1.Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])

class Talaba:
    def __init__(self,ism,fam,yosh,kasbi):
        self.ism=ism
        self.fam=fam
        self.yosh=yosh
        self.kasbi=kasbi
        self.fanlar=[]
        
    def fan_qosh(self,fan):
        return self.fanlar.append(fan)

    def get_info(self):
        info = f"{self.ism} {self.fam}, "
        info += f"{self.yosh} yoshda va {self.kasbi}. "
        info += f"Quyidagi fanlarni yoqtiradi: {', '.join(self.fanlar)}"
        return info 
    
t1=Talaba("Mirzo", "SHomuratov", 27, "Student")
t1.fan_qosh("Python")
t1.fan_qosh("Java Script")
print(t1.get_info())

#2.Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.

class Fan(Talaba):
    def __init__(self,fan1,fan2,fan3,fan4):
        self.fan1=fan1
        self.fan2=fan2
        self.fan3=fan3
        self.fan4=fan4
        super().__init__(fan1,fan2,fan3,fan4)
        self.fanga_yozildi=[]
        
    def add_fan(self,fan):
        self.fanga_yozildi.append(fan)
        
    def get_fanlar(self):
        info= f"1-fan:{self.fan1},2-fan:{self.fan2},3-fan:{self.fan3}"
        info +=f"4-fan:{self.fan4}. Va qo'shimcha fanlar: {','.join(self.fanlar)}"
        return info

fan1 = Fan("Algebra","Ingliz tili","Rus tili","Python")
fan2 = Fan("Geografiya","Fransuz tili","Arab tili","Java SCript")
fan3 = Fan("Tasviriy Sanat","Nemis tili","Uyg'ur tili","PHP")
fan1.add_fan("Jumavoy tili")
print(fan1.get_fanlar())


#3.Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida Fan klassiga tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.

class Fan1:
    def __init__(self,nomi):
        self.nomi = nomi
    
algebra =Fan1("1-Algebra")
geometriya =Fan1("2-Geometriya")
tarix = Fan1("Tarix")
 
class Tal2():
    def __init__(self,ism,fam):
        self.ism=ism
        self.fam=fam
        self.fanlar = []
        
    def get_info(self):
        info=f"{self.ism} {self.fam}"
        return info
    
    def fanga_yozil(self,fan):
        self.fanlar.append(fan)
        
#4.Talabaning fanlari ro'yxatidan biror fanni o'chirib tashlash uchun remove_fan() metodini yozing. Agar bu metodga ro'yxatda yo'q fan uzatilsa "Siz bu fanga yozilmagansiz" xabarini qaytarsin.

    def remove_fan(self,fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
            return f"{fan.nomi} fani muvofaqqiyatli o'chirildi!"
        else:
            return f"Siz {fan.nomi} faniga yozilmagansiz!"
    
ali = Tal2("Mirzo","SHomuratov")
ali.fanga_yozil(algebra)
ali.fanga_yozil(tarix)
print(ali.remove_fan(tarix))

for fan in ali.fanlar:
    print(fan.nomi)
    

#5.Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
class Professor(Shaxs):
    def __init__(self,ism,familiya,passport,tyil):
        super().__init__(ism,familiya,passport,tyil)
          
pr1 = Professor("Mirzo","Kim","FA321112",1999)
print(pr1.get_info())



#6. Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, Sotuvchi, Mijoz va hokazo)

class Sotuvchi(Shaxs):
    def __init__(self,ism,familiya,passport,tyil):
        super().__init__(ism,familiya,passport,tyil)
          
pr1 = Sotuvchi("Ganisher","hyuk","TR6787878",1980)
print(pr1.get_info())

#7.Har bir klassga o'ziga hoz xususiyatlar va metodlar yuklang.
class Foydalanuvchi(Shaxs):
    def __init__(self,ism,familiya,passport,tyil,yangi_foyda):
        super().__init__(ism,familiya,passport,tyil)
        self.yangi_foyda = yangi_foyda
        
    def get_foydalanuchi(self):
        return self.yangi_foyda
          
pr1 = Foydalanuvchi("Ganisher","hyuk","TR6787878",1980,"Bu kishi Yangi foydalanuvchi,")
print(pr1.get_foydalanuchi())


class Mijoz(Shaxs):
    def __init__(self,ism,familiya,passport,tyil,ol_pul):
        super().__init__(ism,familiya,passport,tyil)
        self.ol_pul ="Ha Pulini oldim"
        
    def get_pul(self):
        return self.ol_pul
          
pr1 = Mijoz("Ganisher","hyuk","TR6787878",1980,"ha")
print(pr1.get_pul())
















