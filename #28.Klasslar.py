#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 18:50:43 2026

@author: mirzo
"""

x=10
print(type(x))

matn= "Assalom"
print(type(matn)) # matn obyekt, string classiga tegishli.
print(matn.upper()) # upper methodini qo'lladik.


def salom():
    print("Assalomaalykum")
print(type(salom)) # Salom nomli obyekt, funksiya nomli classga tegishli

# pythonda o'zimizni classlarni yaratish.
class Talaba:
    def __init__(self,ism,familya,tyil):
        self.ism=ism
        self.familya =familya
        self.tyil=tyil
        
        # talabaning familyasini hisoblaydi
    def get_familya(self):
            return self.familya
        
        # talabaning yoshini aniqlaydigan function
    def get_age(self,yil):
            return yil - self.tyil
        
        # get_name methodi bizning objectimizdagi ismlarni oladi.
    def get_name(self):
            return self.ism
        
        # tanishtir nomli method yaratdik
    def tanishtir(self):
        return(f"Ismim {self.ism} {self.familya}, tug'ilgan yilim {self.tyil}") # return orqali malumot qaytarilinadi va bu malumotni xohlagan joyda ishlata olamiz

# shu classlar oqrali objlar yaratdik.
talaba1 = Talaba("Mirzo","Shomuaratov", 1999)
talaba2 = Talaba("Latif","Shomuratov", 2005)
talaba3 = Talaba("Hojiakbar", "Ismoilov", 1992)

  # pass operatori
  # pythonda hech qnaday vazifani bajarmaydi. Bu operatorda bosh methodlar yaratishda foydalanaish mn.Misol clasimiz un methodlarni bilamiz, lekin method badani hali tayyor emas.
  # AGar bo'sh qoldirsak, python IndentationError qaytaradi. Shunday haolatlarda funksiya badaniga pass operatorini qo'yib ketishimiz mn.

class User:
    def __init__(self,name,instaName,email):
        self.name=name
        self.instaName=instaName
        self.email=email
        
    def describe(self):
        pass
    
    def get_name(self):
        return self.name
      
    def get_email(self):
        return self.email
        

    def get_info(self):
        return (f"Mening ismim {self.name}, emailim:  {self.email} va Instagram nickim {self.instaName}")
    
us1 = User("Mirzo", "M1rzo_99", "accaunoff99@gmail.com")
us2 = User("NODIR", "nodir", "Nodirbe@gmail.com")
us3 = User("Nursulton", "nurik", "Nurali@gmail.com")
    
# Yuqoridagi klassimizda describe() va get_email() funksiyalar badani hali tayyor emas,boshliqni toldirish un esa pass operatoridan foydalanamiz.
# pass operatoridan if-else,for,while operatorlari badanida ham foydalanish mn.















