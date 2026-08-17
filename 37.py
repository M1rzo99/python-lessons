# avvalgi darslarda funksiyalarni tekshiryvchi testlarni yozishni o'rgangan edik.Ushbu mavzuda esa klasslarni test qilishni o'rganamiz.Klass to'gri bo'lsa,undan yaratilgan obyektlar ham to'g'ri ishlaydi

class Car:
    """(self,make,model,year,km=0,pricce=None)"""
    def __init__(self,make,model,year,km=0,price=None): #1. km va price argumentlariga standart qiyat beramiz.
        self.make=make
        self.model=model
        self.year=year
        self.price=price
        self.__km=km #2. km  classdan tashqaridan va uni o'zgartira olmasligimiz un classlradan tashqarida ishlatilgan(incapsulatsiyalangan)

    def set_price(self,price):#3. avtomobil narhini set_price orqali yangilash mumkin.
        self.price = price

    def add_km(self,km): #4. add_km() methodi faqat musbat qiymatini qabul qiladi.
        """ Mashinaning km siga yana km qo'shish """
        if km>=0:
            self.__km +=km
        else:
            raise ValueError(" km manfiy bo'lishi mumkin emas") #5.agar manfiy qiymat kiritilsa, raise operatori yordamida ValueError xatosi qaytariladi. 

    def get_info(self): #6. get_info() methodidan qaytadigan qiymat,.avtomobil narhi bor yoki yo'qligiga qarab turli ko'rinishda bo'ladi.
        info=f"{self.make.upper()} {self.model.title()},"
        info += f"{self.year} - yil,{self.__km}km yurgan."
        if self.price:
            info +=f"Narhi: {self.price}"
            return info

    def get_km(self):
        return self.__km #7. Avtomobil narxini ko'rish un get_km() metodiga murojat qilamiz.
    
car1= Car("GM","Malibu",2020,10000,25000)
print(car1.get_km())