#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 23:28:37 2026

@author: mirzo
"""

# MAXSUS METODLAR
# Pythonda obyektlar bilan ishlashni yanada qulay qilish uchun bir nechta maxsus metodlar bor. Bu metodlarning nomi ikki pastki chiziq bilan yozilgani uchun, double underscore yoki qisqa qilib dunder metodlar deb ataladi. Dunder metolar yordamida obyektlarga qo'shimcha qulayliklar va vazifalar qo'shishimiz mumkin. Klass yoki obyektga oid dunder metodlar ro'yxatini ko'rish uchun dir() funksiyasidan foydalanamiz:


>>> dir(Avto)
['_Avto__num_avto',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'make',
 'model',
 'narh',
 'rang',
 'yil']
#Dunder metodlardan biz __init__ metodi bilan tanishdik. Bu metod klassdan obyekt yaratishda chaqiriladi va obyektning xususiyatlarini belgilaydi. Ushbu darsimizda esa maxsus metodlarning ba'zilari bilan tanishamiz.




#OBYEKT HAQIDA MA'LUMOT
#Obyektga print() yoki str() orqali murojat qilinganda obyekt haqida tushunarli ma'lumot qaytarish uchun __repr__va __str__ metodlaridan foydalanamiz. Tushunarli bo'lishi uchun avvalgi darsimizdagi Avto klassiga qaytamiz:


class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1
Yuqoridagi klassdan yangi obyekt yaratamiz va obyekt haqida ma'lumot olish uchun print() funksiyasini chaqiramiz:


avto1 = Avto("GM","Malibu","Qora",2020,40000)
print(avto1) # obyekt haqida ma'lumot
Natija: <__main__.Avto object at 0x00000238A6DAE0C8> 
Qandaydur tushunarsiz ma'lumot. Ekrandagi natijadan biz faqat avto1 obyektimiz Avto klassiga tegishli ekanini ko'ramiz. Qanday qilib shuning o'rniga obyekt haqida tushunarliroq ma'lumot olishimiz mumkin?
Gap shundaki biz har gal obyketga print() (yoki str() yoki repr()) orqali murojat qilganimizda, Python obyket ichida __str__ yoki __repr__ metodlariga murojat qiladi. Agar biz bu metodlarni yozmagan bo'lsak, yuqoridagi kabi umumiy ma'lumot qayataradi. 
Biz ushbu metodlarni yangidan yozib, biz istagan ma'lumotni qayataradian qilishimiz mumkin. Odatda, yuqoridagi ikki metoddan birini yozish kifoya. Odatda, __repr__ umumiyorq, __str__ esa batafsilroq ma'lumot olish uchun ishlatiladi. 
Ikkalasidan birini tanlaganda, __repr__metodiga yon bosiladi, sababi bu metod print(), str() va repr() funksiyalarining hammasi bilan ishlaydi. Keling biz ham yuoqirdagi klassimizga__repr__metodini qo'shamiz:


class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1
    
    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.rang} {self.make} {self.model}"
Qaytadan print() funksiyasini chaqiramiz:


avto1 = Avto("GM","Malibu","Qora",2020,40000)
print(avto1)
Natija: Avto: Qora GM Malibu
Mana endi natijamiz ancha tushunarli ko'rinishda chiqdi.




#OBYEKTLARNI TAQQOSLASH
#Taqqoslash operatorlari yordamida biz turli obyektlarni solishtirishimiz mumkin. Taqqoslash natijasi mantiqiy qiymat (True yoki False) ko'rinishida bo'ladi. 


x,y = 5,10
print(x>y)
Natija: False
Keling endi Avto klassidan 2 ta obyekt yaratamiz, va ularni taqqoslab ko'ramiz:


avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto1>avto2
Natija: TypeError: '>' not supported between instances of 'Avto' and 'Avto'
Xatolik. Demak bu ikki obyektni solshtirib bo'lmas ekan. 
Biz taqqolash operatorlariga murojat qilganimizda, Python obyektlar ichida taqqoslash uchun maxsus metodlarni qidiradi, agar metodlar topilmasa yuqoridagi kabi TypeError qaytaradi. 
Taqqoslash metodlari quyidagilardan iborat:

Metod
Operator
x.__lt__(self,y)
x<y
x.__le__(self,y)
x<=y
x.__gt__(self,y)
x>y
x.__ge__(self,y)
x>=y
x.__eq__(self,y)
x==y
x.__ne__(self,y)
x!=y
Yuqoridagi obyektlardan yarmi uchun metodlar yozishimiz kifoya, misol uchun __lt__ (x<y) metodini yozsak, __gt__ (x>y) metodini yozishimiz shart emas, yoki __le__ metodi, __ge__metodini ham o'z ichiga oladi, va hokazo.
Keling tushunarli bo'lishi uchun Avto klassiga obyektlarni solishtirish uchun metod yozamiz. Deylik, biz obyektlarni narhi bo'yicha solishtirmoqchimiz, unda klassimizga quyidagi metodlarni qo'shamiz (klassni to'liq yozmadik, faqat qo'shilgan metodlarni keltiramiz):


    def __eq__(self,boshqa_avto):
        """Tenglik"""
        return self.narh == boshqa_avto.narh
    
    def __lt__(self,boshqa_avto):
        """Kichik"""
        return self.narh<boshqa_avto.narh
    
    def __le__(self,boshqa_avto):
        """Kichik yoki teng"""
        return self.narh<=boshqa_avto.narh
Kodimizga e'tibor qilsangiz biz tenglik (__eq__) yoki kichiklikni (__lt__) tekshirmoqchi bo'lganimizda ikki avtoning aynan narhi bo'yicha solishtiramiz (self.narh == boshqa_avto.narh).
Mana endi avtolarni solishtirsak bo'ladi:


avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
print(avto1>avto2)
Natija: False


avto3 = Avto("Honda","Accord","Oq",2017,40000)
print(avto1==avto3)
Natija: True


