#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 12:53:02 2026

@author: abcd
"""
#MAXSUS METODLAR
#Pythonda obyektlar bilan ishlashni yanada qulay qilish uchun bir nechta maxsus metodlar bor. Bu metodlarning nomi ikki pastki chiziq bilan yozilgani uchun, double underscore yoki qisqa qilib dunder metodlar deb ataladi. Dunder metolar yordamida obyektlarga qo'shimcha qulayliklar va vazifalar qo'shishimiz mumkin. Klass yoki obyektga oid dunder metodlar ro'yxatini ko'rish uchun dir() funksiyasidan foydalanamiz:

#dir(Avto)
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



# Biz dunderlar orqali o'zimizga kerakli bo'lagna methodlarni yozib olsak bo'ladi. 
# Dunder ayna bizga qulaylik yaratadi. Misol qilib arifmetik amallarni: 1-son 2- sondan kattami,kichikmi,tengmi,teng kattami yoki teng kiechikmi Yoki Tengmi shularni solishitirish mumkin bo'ladi.

# Dunder ningishlashi: Taqqoslash ni berganda,qaysiki  biz ishlatmoqchi bo'lgan methodni,biz yozgan methodlar orasidan birma-bir qidiradi va Keraklisini topib solishtiradi. SHu tariqa dunder methodlar ishalydi
 


#Dunder methodlaridan biz __init__ methodi bn tanioshdik. BU method classdan obyekt yaratishda chaqirilinadi va Obyejt xususiyatlarini belgilaydi.

#Obyekt haqida ma'lumotlar: 
    #Obyektga print() yokida str() orqali murojat qilganda obyekt haqida tushunarli ma'lumot qaytarish uchun __repr__ va __str__ methodlaridan foydalanamiz. 
    # Va asosan __repr__ dan foydalanishni tavfsiya berishadi

# Keling avvalgi darsimizdagi Avto classi orqali bazi misollar ko'ramiz:
    
#class Avto:
 #   __num_avto = 0
  #  """Avtomobil klassi"""
  #  def __init__(self,make,model,rang,yil,narx):
    #    """Avtomobilning xususiyatlari"""
    #    self.make=make
    #    self.model=model
    #    self.rang=rang
    #    self.yil=yil
    #    self.narx=narx
  #      Avto.__num_avto +=1
  #  """ cycle har bir aylanganligini ko'rsatib beradi"""
#Yuqoridagi classdan obyekt yaratamiz va obyekt haqida malumot olish un print() functionini chaqiramiz
#avto1 = Avto("GYM", "Malibu2", "Qora", "2019", 20000)
#print(avto1)

#Natija: <__main__.Avto object at 0x00000238A6DAE0C8> 
# Qandaydir tushunarsiz ma'lumot.
# Gap shundaki biz har gal obyektga print() yoki str() yoki repr() orqali murojat qilganda,Python Obyekt ichida __str__ yoki __repr__ methodlarioga murojat qiladi. 
#Agar biz bu metholarni yozmagan bo'lsak, yuqorodagi kabi malumot qaytaradi.

#Biz ushbu methodlari yangidan yozib,biz istagan ma'lumotni qaytaradigan qilishimiz mumkin.Odatda Quyidagi ikki methoddan birini yozish kifoya.Odatda __repr__ umumiyroq, __str__ esa batafsilroq ma'lumot olish un ishlatilinadi.
# Ikkalasidan biri tanlanganida, __repr__ methodi yon bosiladi, sababi bu print(),str() va repr funksiyalarining hammasi bn ishlaydi.


class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narx):
        """Avtomobilning xususiyatlari"""
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narx=narx
        Avto.__num_avto +=1
        
    def __repr__(self):
        return f"Avto:Rangi {self.rang},Zavod {self.make} va Markasi {self.model}"
    
    """ cycle har bir aylanganligini ko'rsatib beradi"""
#Yuqoridagi classdan obyekt yaratamiz va obyekt haqida malumot olish un print() functionini chaqiramiz
avto1 = Avto("GYM", "Malibu2", "Qora", "2019", 20000)
print(avto1)

# Obyektlarni Taqqoslash

#Taqqoslash operatorlari yordamida biz turli obyektlarni solishitrishimiz mumkin.Taqqoslash natijasi mantiqiy qiymat(True yoki False) ko'rinishida bo'ladi.

x,y = 10,20
print(x>y)

# Avto classidan ikkita obyekt yaratamiz va ularni taqqoslab ko'ramiz: 
avto1 = Avto("GYM", "Malibu2", "Qora", "2019", 20000)
avto2 = Avto("KIA", "K5", "Blue", "2010", 30000)


# Natija: TypeError: '>' not supported between instances of 'Avto' and 'Avto'

# Xatolik: Demak bu ikki obyektni solishtirb bo'lmas ekan. 
# Biz taqqoslash operatoriga murojat qilganimizda,Python obyektlar ichida taqqoslash un maxsus methodlarni qidiradi, agar method topilmasa yuqoridagi kabi TypeError qaytaradi.

# TAQQOSLASH METHODLARI QUYIDAGILARDAN IBORAT: 

# Metodva             Operator
#x.__lt__(self,y   )      x<y
#x.__le__(self,y)        x<=y
#x.__gt__(self,y)        x>y
#x.__ge__(self,y)        x>=y
#x.__eq__(self,y)        x==y
#x.__ne__(self,y)        x!=y

# Yuqoridagi obyektlarni yarmi un methodlar yozishimiz kifoya.Misol un __lt__ (x,y) metodini yozsak, __gt__(x>y) methodini yozishimiz shart emas, yoki __le__ methodi, __ge__ mothodini ham o'z ichiga oladi.

# Keling Avto classda yaratilgan obyektlarni narhlari bn solishtiramiz:
    
    
    
class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narx):
        """Avtomobilning xususiyatlari"""
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narx=narx
        Avto.__num_avto +=1
        
    def __eq__(self,boshqa_avto):
        """Tenglik"""
        return self.narx == boshqa_avto.narx
    
    def __lt__(self,boshqa_avto):
        """Kichik"""
        return self.narx < boshqa_avto.narx
    
    def __le__(self,boshqa_avto):
        """Kichik yoki teng"""
        return self.boshqa_avto <= boshqa_avto.narx
    
        
    def __repr__(self):
        return f"Avto:Rangi {self.rang},Zavod {self.make} va Markasi {self.model}"
    
    """ cycle har bir aylanganligini ko'rsatib beradi"""
#Yuqoridagi classdan obyekt yaratamiz va obyekt haqida malumot olish un print() functionini chaqiramiz
avto1 = Avto("GYM", "Malibu2", "Qora", "2019", 20000)
avto2 = Avto("KIA", "K5", "Blue", "2010", 30000)
print(avto1==avto2)
       
#Obyekt Uzunligi

# Pythonda le() funksiyasi yordamida turli obyrktlarni uzunligini bilishimiz mumkin,misol un matn,ro'yhat,lug'at,set va hakazo
matn = 'hello market'
print(len(matn))    
    
sonlar = [1,2,3,4,5,6,7]
print(len(sonlar))





#OBYEKT ELEMENTLARIGA MUROJAT QILISH
#Ba'zi obyektlarning (matn, ro'yxat, lug'at va hokazo) elementlariga alohida murojat qilish mumkin. 

mevalar = ['olma','anor','uzum']
mevalar[0]
#Bizning salonimizda ham 3 ta avto bor, ularni ko'rish uchun yuqoridagi kabi element raqami orqali murojat qila olamizmi?

#salon1[0]
#Natija: TypeError: 'AvtoSalon' object is not subscriptable
#Afsuski yo'q. Ko'rib turganingizdek bizning obyektimizga bunday murojat qilib bo'lmas ekan. Obyektimizga bu xususiyatni qo'shish uchun __getitem__metodini yozishimiz kerak.

class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __len__(self):
        return len(self.avtolar)
    
    def __getitem__(self,index):
        return self.avtolar[index]
#Endi salon1 obyektimizning elementlariga murojat qilinganda __getitem__metodi obyekt ichidagi avtolar ro'yxatidan ko'rsatilgan element (avtomobilni) qaytaradi.




#Keling obyekt elementlaridan birini o'zgartirib ko'ramiz:


avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
#salon1[0]=avto4
#Natija: TypeError: 'AvtoSalon' object does not support item assignment
#Y#ana xatolik. Gap shundaki __getitem__ metodi o'z nomi bilan (get) element qaytaruvchi metod. Biror elementni o'zgartirish uchun esa __setitem__metodini ham qo'shishimiz kerak. Bu metodimizga murojat qilinganda ham, yangi qiymat Avto klassiga oid ekanligini tekshirib olish maqsadga muvofiq bo'ladi:


#def __setitem__(self,index,value):
    #    if isinstance(value,Avto):
    #        self.avtolar[index]=value
#Qaytadan elementni o'zgartirishga harakat qilib ko'ramiz:

#avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
#salon1[0]=avto4
#print(salon1[0])
#Natija: Avto: Qizil Mazda 6
#Kutilgan natija chiqdi












