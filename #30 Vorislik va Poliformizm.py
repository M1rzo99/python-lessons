
# 30-dars. Vorislik va Poliformizm
# Klasslardan klasslar yaratishni o'rganamiz.

#  Obyektga yo'naltirilgan dasturalshning qulayliklaridan biri bu klasslardan boshqa klasslar yaratishdir.
# Bizga kerak bo'lgan yangi klass\, avval yaratilgan klass bn o'xshashlik joylari bo'lsa, biz bu klassdan voris klass yaratishimiz mn.
# Bunda asl klass ota yoki super klass deb ataladi.
# Super klasdan yaratilgan voris klass, superClassning barcha yoki tanlangan xususiyatlari va methodlarini meros olish bn birga,o'ziga xos xususiyat va methodlarga ega bo'ladi.

# Shaxs nomli class yaratamiz, va bu class boshqa classlar un super class vazifasini bajaradi.

class Shaxs:
    """Shaxs haqida ma'lumot """
    def __init__(self,ism,familya,passport,tyil):
        self.ism = ism
        self.familya = familya
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        """shaxs haqida ma'lumot method"""
        info = f"{self.ism} {self.familya}."
        info += f"Passport: {self.passport} va {self.tyil} - yilda tug'ilgan"
        return info
    
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi method"""
        return yil - self.tyil 
# Classni etekshirib ko'ramiz

shaxs1 = Shaxs("Mirzo","Shomuaratov","FA0342323", 1999)
print(shaxs1.get_info())
print(shaxs1.get_age(2026))

# Voris klass Yaratamiz:
# Talaba nomli class yaratamiz va oldinigi shaxs nomli classni super class sifatida foydalanamiz.

# class Talaba(Shaxs):
#     """Talaba Klassi"""
#     def __init__(self, ism, familya, passport, tyil):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familya, passport, tyil)   
#  # Kodni tahlil qilaylik: 
# # 1- qatorda klass nomidan so'ng,qavs ichiga super klass nomini berdik.
# # 3- qatorda def __init__ ichida klassimiz  klass xususiyatlarini meros qilib olishini ko'rsatdik.
# # 5- qatorda super() __init__ super clsssdagi  superformancelarni oladi.
# # bu bizga super classdagi xususiyatlarni qayta yozishdan saqlaydi.

# t1 = Talaba("Navro'z","Sobirov", "TA 2131313", 2001)
# print(t1.get_age(2026))
# print(t1.get_info())

# Eslatma: Dastur davomida super class voris klassdan oldin yozilgan bo'lishi kerak.

# VORIS KLASSGA XOS XUSUSIYATLAR VA METODLAR:
# Hozirgi ko'rinishda Talaba va Shaxs klasaslari o'rtasida hech qanday farq yo'q.
# Keling Talaba klassimizga o'ziga xos xususiyatlar va methodlar qo'shaylik.
# Avvalosiga,  talabaninng ID va Bosqichini xususiyat sifatida qo'shamiz
# Bunda ID raqam, obyekt yaratishda parametr sifatida uzatilinadi,bosqich esa standart qiymatga ega:
    
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familya, passport, tyil,iDraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familya, passport, tyil)
        self.iDraqam = iDraqam
        self.bosqich =1
        self.baho = 10
        
    def get_bosqich(self):
        return self.bosqich
    
    def get_id(self):
        return self.iDraqam
    
    def get_baho(self):
        return self.baho
    
        
t1=Talaba("Kamron", "Sobirov", "HG21211212", 2005, "00019785")
print(f"{t1.get_info()}. ID raqami: {t1.get_id()} va {t1.get_bosqich()}-bosqich Talabasi.Uning bahosi {t1.get_baho()} balldir.")

# Poliformizm  - super class methodlarini qayta yozishdir.
      
# Voris classga super classdan meros qolgan methodni qayta talqin qilish mumkin. Avvalgi misolimizdagi get_info() super methodini ko'raylik,bu method talabaning ismi,familyasi,passport raqami va tugilgan yilini qaytaradi.
class Talaba2(Shaxs):
    """Talaba2 klassi"""
    def __init__(self, ism, familya, passport, tyil,iDraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familya,passport,tyil)
        self.iDraqam = iDraqam
        self.bosqich = 20
        
    
    def get_id(self):
        """Talaba ID raqami"""
        return self.iDraqam
    
    def get_bosqich(self):
        """Talaba bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familya}. "
        info +=f"{self.get_bosqich()}-bosqich. ID raqami: {self.get_id()}"
        return info
    
talaba1 = Talaba2("Doniyor", "Alimov", "JK2123548","2000", 9034312,)
print(talaba1.get_info())    
    
    
    
    # Obyekt ichida obyekt

# Bazida klassimiz xususiyatlar va ular bn ishlaydigan methodlarga to'lib ketishi, bu esa o'z navbatida obyektlar bn ishlashni qiyinlashtirishi mumkin.SHunday holatlarda ba'zi xususiyatlarni alohida klass ko'rinisihida yozish
# va keyinchalik bu klassdan obyektni boshqa  obyektning xusussiyati sifatida foydalanish mumkin.
 
# Misol,SHaxs classimizga yana bir manzil degan xususiyat qo'shaylik.odatda manzil bir nechta qismlardan iborat bo'ladi(xonadon,ko'cha,mahalla tuman/shahar,viloyat,indeks va hakazo) va ularning har biri un SHaxs class ichida alohida xususiyat yaratmasdan
# alohida manzil degan klass yuklash maqsadga muvofiq bo'ladi.

class Manzil:
    def __init__(self,uy,kocha,tuman,viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
        
    def get_manzil(self):
        """Manzil ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy} uyi. "
        return manzil
    
# Talaba classimizga ham manzil xususiyatini qo'shamiz:
    
class Talaba3(Shaxs):
    """Talaba2 klassi"""
    def __init__(self, ism, familya, passport, tyil,iDraqam,manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism,familya,passport,tyil)
        self.iDraqam = iDraqam
        self.bosqich = 20
        self.manzil = manzil
        
    
    def get_id(self):
        """Talaba ID raqami"""
        return self.iDraqam
    
    def get_bosqich(self):
        """Talaba bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familya}. "
        info +=f"{self.get_bosqich()}-bosqich. ID raqami: {self.get_id()}"
        return info
    
    
talaba_manzil = Manzil(44,"Rovot", "Urganch", "Xorazm")
talaba3 = Talaba3("Mirzo1", "Shomuratov", "FG0122345", 1999, "OD:90434321",talaba_manzil) 

print(talaba3.manzil.get_manzil())



    
    
    
    
    
    

