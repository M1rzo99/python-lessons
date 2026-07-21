# Inkapsulyatsiya
# Obyektaga yo'naltirilgan  Dasturlashning xususiyatlarida biri bu INKAPSULYATSIYA, ya'ni obyektning 
#xususiyatlariga to'g'ridan-to'g'ri (yani nuqta orqali) murojat qilishni va ularning qiymatini taqiqlab qoyish. 
# Pythonda bunday yopiq xususiyatlarning nomi ikki pastgi chiziq bn boshlanadi:

from uuid import uuid4 # randaom ID yaratib beradi,xar safar.Har bir foydalanuvchiga
class Avto:
    """Avtomabil klassi"""
    def __init__(self,make,model,rang,yil,narx,km=0):
        """Avtomobilning xususiyatlari"""
        self.make= make
        self.model = model
        self.rang=rang
        self.yil=yil
        self.narx=narx
        self.__km = km # inkapsulyatsiya - xususiyatni hech kim ko'ra olmaydi va o'zgartira olmaydi,oddiy yo'l bilan
        self.__id = uuid4() # inkapsulyatsiya
        
    def get_km(self):
        return self.__km #inkapsulyatsiya - bu orqali ko'ra oaldi kmni 

    def get_id(self):
        return self.__id
    
#Bunday yopiq xususiyatlarni o'zgartirsh ham methodlar orqali amalga oshirilioshi kerak.Misol un mashinaning necha km yurganini o'zgartirish un klassimizga quyidagi methodni qo'shamiz:
    def add_km(self,km):
        """Mashinaning km siga yana km qo'shamiz"""
        if km>=0:
            self.__km +=km
        else:
            print("Mashinaning km sini kamaytirib bo'lmaydi!")
    

avto1 = Avto("GM","Malibu","Qora",2020,40000,1000)

# Yopiq xususiyatlarni ko'rish uchun esa alohida metodlar yozish maqsadga muvofiq bo'ladi (get_km() va get_id()):
print(f"ID: {avto1.get_id()}")
print(f"KM: {avto1.get_km()}")

avto1.add_km(-1000)
print(avto1.get_km())


# Inkapsulyatsiyaning maqasdadi obyektni malum bir xususiyatalrnini tashqi ta'sirdanhmoya qilish.
# Misol un yuqoridagi misolda mashinaning qancha km yurganini faqat musbat tarafga o'zgartirish mumkin.Noyob ID ni esa umuman o'zgartirib bo'lmaydi.


# Klassing xususiyatlari va Methodlari:

    # avvalgi darslarda biz biror klassdan yaratilgan har bir obyektning xususiyatlarini klass ichidagi def__init__() methodi yordamida berayotgan edik.
    # Bunda method qanday ishlaydi: Biz har gal classga murojat qilayotganimizda aynan shu __init__ methodini ishga tushiradi va biz bergan xususiyatlar bn yangi obyekt yaratilinadi.
    
# Pythonda xususiyatlarni nafaqat obyektga balikm to'g'ridan-to'g'ri classga ham yuklash imkoniyati bor.Bunda klassning xususiyatlariga berilgan qiymat barcha obyektlar uchun umumiy bo'ladi.
# Bu xususiyatni bur obyekt orqali o'zgartirganda shu klassga oid barcha obyektlarda ham uning qiyamti o'zgaradi.

# Classga oid xususiyatlar dev__init__ methodidan oldin e'lon qilinadi
class Avto:
    """Avtomobil klassi"""
    num_avto = 0 #Classga xususiyat berdik
    
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.num_avto += 1

# Kod tajlil qilamiz:
    # 1- qatorda Avto klassini yasadik
    # 3- qatorda Avto klassiga oid bo'lgan xususiyat num_avto yaratdik va unga 0 qiymatini berdik
    # Keyingi qatorlarda __init__ methodi yordamida klassdan yaratilgan obyektlarning xususiyatlarini e'lon qildik,
    # va har gal bu methodga murojat qilinganda, num_avto ning qiymatini 1 ga oshiradigan qilib qo'ydik

# Yuqoridagi usul bn biz endi dastur davomida Avto klasidan jami nechta obyektlar yaratilganini kuzatob borishimiz mn.
# Bunda num_avto o'zgaruvchisiga istalgan obyekt nomi yoki klass nomi orqali murojat qilish mn:
    
avto11 = Avto("Hyundai", "Grande", "Blue", 2021, 30000)
avto22 = Avto("Hyundai", "Grande", "Blue", 2021, 30000)
avto33 = Avto("Hyundai", "Grande", "Blue", 2021, 30000)
avto44 = Avto("Hyundai", "Grande", "Blue", 2021, 30000)

print(avto11.num_avto)#  Natija 4, chunki 4 ta obyekt yaratdik va 4 marta chaqirdik 



# Klassning xususiyatlarini inkapsulyatsiya qilish
# klassning xususiyatlari ham yuqoridagi kabi pastki ikki chiziq bn inkapsulyatsiya qilinadi:
    
class Avto:
    """Avtomobil klassi"""
    __num_avto = 0 # klassga oid xususiyat
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1
        
    def get_num(self):
        return self.__num_avto
        
avto44 = Avto("Hyundai", "Grande", "Blue", 2021, 30000)

print(avto44.get_num()) # inkapsulyatsiya qilindi va count 1 bo'ldi



# KLASSGA OID METODLAR

# Klasslarning o'ziga xos methodlari ham bo'lishi mumkin.Misol un yuqoridagi num_avto
# xususiyatlarini ko'rish un alohida method yozishimiz mumkin.
# Klassga oid methodlar esa @classmethod dekaratori bn boshlanadi
# Va obj ga oid methofdlardan farqli ravishda self emas cls(class) argumentini qabul qiladi

class Avto:
    """Avtomobil klassi"""
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
        
    @classmethod      
    def get_num_avto(cls):
        return cls.__num_avto
    
    # va Class methodlarga class nomi orqali murojat qilinadi:
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
print(Avto.get_num_avto())

# @classmethod bu maxsus dekorator. Dekoratorlar bu o'z ichiga funksiya oluvchi funksiyalar. Dekoratorlar haqida keyingi darslarimizning birida batafsil to'xtalamiz.


































