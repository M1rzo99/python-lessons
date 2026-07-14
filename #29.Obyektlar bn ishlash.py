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



# Obyektlar o'rtasidagi munosabatlar:
#Obyektga yo'nalitirilgan dasturlashning avfzalligi, turli obyektlar o'rtasida o'zaro munosabatlar oson yo'lga qo'yish mnligidair.
# Buni misol ko'rinishida, yangi Fan degan class yaratamiz va fanimizga talabalar qo'shish imkoniyatini ham yaratamiz (add_student() methodi)

class Fan():
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
    
    def add_student(self,talaba):
        """ Fanga talaba q'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni +=1
        
    def get_students(self):
        return [talaba.get_info() for talaba in self.talabalar] # self_talabalar ichidagi har bir talaba un get_info() methodini bajar degan mano kelib ciqadi.Kodni kvadrat qavs ichiga olganimiz un esa, har bir tsikl natijasi vatomat ravishda ro'yhatga qo'shiladi.
# Fan nomli class faqatgina nomi degan parametrga ega. Qolgan xususiyatlarni esa standart qiymat sifatida berilgan. talabalar soni 0 ga teng, talabalar ro'yhatri esa bo'sh
# Fanimizga talaba qo'shish un add_student() methodini chaqiramiz. BU method parametr sifatida Talaba obyektini qabul qiladi. Va uni talabalar ro'yhatiga qo'shadi.
# Shuningdek bu method yangi talaba qo'shilganda talabalar_soni ni1 taga oshiradi.

# Keling  oshlanishiga yangi fan obyektini va bir nechta talabalar yaratamiz:
matem = Fan("Oliy Matematika")
talaba1 = Talaba("Alijon","valiyev",2000)
talaba2 = Talaba("Olimboy", "Pirnafasov", 1990)
talaba3 = Talaba("Eldor", "Quronboyev", 1999)

matem.add_student(talaba1)
matem.add_student(talaba2)
matem.add_student(talaba3)
print(matem.talabalar_soni)

math_talabalar  = matem.get_students()
print(math_talabalar)

# Nuqta yoki Method: 
# pythondagi obyektlarning o'ziga xos xususiyatlaridan biri, obyektning xususiyatlariga nuqta orqlai murojat qilishdir. Misol uchun avval yaratgan talaba1 obyektinign ismini bilish un talaba1.ism deb yozish kifoya
# BU o'ziga yarasha qulay bo'lsada, bunday usuldan foyalanmagan avfzal. Sababi vaqt o'tib,klassingiz takomillashishi, uning bazi xususiyatlari o'zgarishi, o'chirilishi yoki almashitirilishi mn.
# SHunday holatlarda nuqta orqali murojat qilish siz kutgan natijani bermasligi va dastur xato ishlashiga olib kelishi mumkin. Bunday holatlarni oldini olish un esa, obyektnig mwthodlarini methodlar orqalu olishni odat qilish tavfsiya etiladi.
# Huddi shu kabi, obyektning xususiyatlarini yangilsh un ham alohida methodlar yozgan avfzal.

# Dasturchilar  orasida obyektning xususiyatlarini o'zgaritiradigan methodlarni set(o'zgartir) so'zi bn, xususiyatlarni qaytaradigan methodlarni esa get(olish) so'zi bilan boshlash qoida qilib olingan.. Masalan set_name() va get_name() kabi.
# Yuqoridagi qoidaga amali qilib talaba classimizni yangilaymmiz:
class Talaba:
    """ Talaba nomli class Yaratayapmiz"""
    def __init__(self,ism,familya,Tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familya = familya
        self.Tyil = Tyil
        self.bosqich = 1 # Xususiyatga standart qiymat berish shudir
        
    def set_bosqich(self,bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich  = bosqich
    
    def update_bosqich(self):
        """ Talabaning  bosqichini oshiradigan method"""
        self.bosqich +=1
        
    def get_info(self):
        """ Talaba haqida ma'luot"""
        return f"{self.ism} {self.familya} {self.Tyil}-yil, {self.bosqich}-bosqich talabasi"
    
    def get_name(self):
        """Talabaning nomini qaytaradigan method"""
        return self.ism 
    
    def get_lastname(self):
        """ Talabaning familyasini qaytaradigan method"""
        return self.familya
    
    def get_fullname(self):
        """ Talabaning ism-familyasini qaytaradigan method"""
        return f"{self.ism} {self.familya}"
    
    def get_age(self,yil):
        """ Talabaning yoshini qaytaradi"""
        return yil - self.Tyil
    

talaba3 = Talaba("Eldor", "Quronboyev", 1999) 

print(talaba3.get_age(2026)) 
print(talaba3.get_fullname()) 
   
# Obyektning methodlari va xususiyatalarini ko'rish:
    
# Obyektlar bn ishlaganda,o'z-oz'idan shu obyektga tegishli xususiyatlar va methodlarni bilish talab qilinadi.Agar Obyektga teishli classni o'zomiz yaratgan bo'lsak, istalgan payt classni ko'rib oishimiz mn.Lekin boshqalar yaratgan class haqida malumot olish talab qilinsa, bir nechta yo'li bor.
 # dir() funksiyasi.
 # dir() funkssiyasi yordamida istalgan obyekt yoki classning xususiyatlari va methodlarini bilib olishimiz mn.

 
# Har bir class bn keluvchi maxsus Dunder methodlar ham kelib chiqadi.Dunder method ikkita pastki chiziq bn boshlanadi(__) va mahsus holatlar un saqlab qo'yilgan. Biz hozircha faqat __init__ methodi bn tanishdik.
# Dunder methodidan keyin esa, biz murojat qiilishimiz mn bo'lgan methodlar kelgan.

# Dunder - doubla undercourse(ikki pastgi chiziq) so'zlarining qisqartmasi
# Keling, Dunder methodini olib tashlab, bizga kerak bo'lgan methodlarni qaytaruvci sodda function yaratamiz: 
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith("__") is False]
print(see_methods(Talaba))


# __dict__ methodi - obyektning xususiyatlarini lug'at ko'rinishda qaytaradi.
print(talaba1.__dict__)
#Natijadan faqat kalitlarni ajratib olsak, obyektning xususiyatlari kelib chiqadi
print(talaba1.__dict__.keys())

# Amaliyot

#1.  Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)
class Avto:
    def __init__(self,model,rang,narh,holat):
        self.model = model
        self.rang = rang
        self.narh = narh
        self.holat = holat
        self.kilo = 5
        
    def update_km(self,kilo):
         self.kilo = kilo
        
    def get_avtoInfo(self):
        return f"{self.model} {self.rang}-rang, Narhi {self.narh} so'm.{self.kilo} km yurgan."
avto1 = Avto("Porsche 911","Grey", "111.000$", "Yangi")
avto1.rang = "Qora"
avto1.model = "Porshe Cayenne"
avto1.kilo = 0
avto1.update_km(10)
print(avto1.get_avtoInfo())

#2.Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)

class Avtosalon():
    def __init__(self,salon_nomi):
        self.salon_nomi=salon_nomi
        self.avtos_num =0
        self.avtolar = []
        
   #3. Avtosalonga yangi avtomobillar qo'shish va avtosalondagi avtolarni ko'rish uchun metod yozing     
        
    def add_avtos(self,avto):
            """ Fanga talaba q'shish"""
            self.avtolar.append(avto)
            self.avtos_num +=1
            
    def get_avtos(self):
        return [avto.get_avtoInfo() for avto in self.avtolar]


avt=Avtosalon("Avtolar oalmi")
avt1 = Avto("Porsche 911","Grey", "111.000$", "Yangi")
avt2 = Avto("Porsche 911","Grey", "111.000$", "Yangi")
avt3 = Avto("Porsche 911","Grey", "111.000$", "Yangi")

avt.add_avtos(avt1)
avt.add_avtos(avt2)
avt.add_avtos(avt3)
print(avt.avtos_num)

avt_inf = avt.get_avtos()
print(avt_inf)

print(avt1.__dict__)
#Natijadan faqat kalitlarni ajratib olsak, obyektning xususiyatlari kelib chiqadi
print(avt.__dict__.keys())
