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
avto1 = Avto("GM","Malibu","Qora",2020,40000,100000)
avto1.get_id()