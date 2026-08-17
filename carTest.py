# Xususiyatlarni tekshirish 
# Klassdan obyekt yaratishda,obyekt xususiyatlarini parametr ko'rinishida beramiz. 
# Quyidagi testda aynan shu jarayon to'g'ri kechganini tekshiramiz.

import unittest
from car import Car

#class CasrTest(unittest.TestCase):
 #   """Car klassini test qilish"""

 #   def test_create(self):
        # avto1 obyektini km va narhini bilmasdan tekshiramiz
 #       avto1 = Car("BMW","camry",2020)
 #       # Qiymatlar mavjudligini assertIsNotNone methodi bn tekshiramiz
 #       self.assertIsNotNone(avto1.make)
 #       self.assertIsNotNone(avto1.model)
  #      self.assertIsNotNone(avto1.year)
        # Qiymat mavjud emasligini assertIsNone metodi bn tekshiramiz 
  #      self.assertIsNone(avto1.price)
        # Qiymat tengligini assertEquals metodi bn tekshiramiz
   #     self.assertEqual(0,avto1.get_km())
        # Yangi Obyekt yaratamiz va narhni ham ko'rsatamiz
   #     avto2 = Car("BMW","carmy",2020,price=45000)
   #     self.assertEqual(45000,avto2.price)
#unittest.main()


# Testimizni tahlil qilamiz. Dastaval biz obyektimiz to'g'ri yaratilayotganini tekshrish uchun avto1 obyektini 3 ta prametr bilan yaratib oldik (make, model, year) va  bu xususiyatlar bo'sh emasligini  assertIsNotNone() metodi bilan tekshirdik. 

#avto1 obyektini yaratishda uning narhini ko'rsatmadik, demak bu xususiyat standart qiymat (None) ga teng bo'lishi kerak. Buni tekshirish uchun esa assertIsNone() metodiga murojat qildik. Vanihoyat, avtomobil kilometraji 0 ga teng ekanligini assertEquals() metodi yordamida test qildik.

#Test so'ngida biz yana bir obyekt yaratdik (avto2) va bu safar avtomobil narhini ko'rsatganimiz uchun assertEquals() metodi yordamida bu qiymat to'g'ri saqlanganini tekshirib oldik.

#Testlarni yozishni davom etamiz. Navbat obyektga tegishli turli metodlarga.

#Test dasturlarni alohida faylga yozishni unutmang.


# setIUp() methodi.

# Yuqoridagi misolda bitta test davomida 2 ta obyekt yaratdik, va obyektning parametrlarini qo'lda yanigdan kiritdik. Agar shu yo'sinda davom etsak,turli testlar un har gal yangi obyekt yaratishimiz, va ularning har biriga xususiyatlarni qayta-qayta kiritishimiz talab qilinadi. 
# Buning oldini olish un test klassimizning boshida setUp() metofini yaratib, bu method ichida barcha kerakli qiymatlarni va obyektlarni saqlab qo'yishimiz va turli testlarsda shu qiymatlarga murojat qilihimiz mn.


class CarTest(unittest.TestCase):
    """ car klassini tekshirish un test"""
    def setUp(self):
        make="BMW"
        model="Malibu"
        year=2021
        self.price=40000
        self.km=10000
        self.avto1=Car(make,model,year)
        self.avto2 = Car(make,model,year,price=self.price)

 #   def test_create(self):
 #       # Qiymatlar mavjudligini assertIsNotNone metodi bn tekshiramiz
 #       self.assertIsNotNone(self.avto1.make)
 #       self.assertIsNotNone(self.avto1.model)
 #       self.assertIsNotNone(self.avto1.year)
 #       # Qiymat mavjud emasligini asseretIsNone metodi bn tekshiramiz
 #       self.assertIsNone(self.avto1.price)
        # Qiymat tengligini assertEquals metofi bn tekshiramiz
 #       self.assertEqual(0,self.avto1.get_km())
        # avto2 nathini tekshiramiz
 #       self.assertEqual(self.price,self.avto2.price)



    def test_set_price(self):
        self.avto2.set_price(self.price)
        self.assertEqual(self.price,self.avto2.price)

# Endi add_km() methodini tekshiraylik.BU methodimiz musbat qiymat qabul qilishi,manfiy qiymat uzatilganda ValueError xatosini qaytarishi kk.Shuning un methodni test qilishda avval musbat,keyin esa manfiy qiymat berib ko'ramiz.

    def test_add_km(self):
        #1.Musbat qiymat berib ko'ramiz
        self.avto1.add_km(self.km)
        self.assertEqual(self.km,self.avto1.get_km())
        #2. manfiy qiymat berib ko'ramiz
        new_km = -5000
        try: 
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error),ValueError)
unittest.main()

#E'tibor bering, setUp() metodi ichida ba'zi o'zagruvchilar self yordamida berilgan (self.price,self.km, self.avto1, self,avto2).'
#' Bu o'zgaruvchilarga biz CarTest() klassining ichida istalgan joydan murojat qilishimiz mumkin. 
#Shuning uchun ham, test_create() funksiyasi ichida biz yangi obyekt yaratmasdan, setUp() ichidagi avto1 va avto2 obyektlariga murojat qildik.


# Methodlarni tekshirish
# Obyektlarimiz bir nechta methodlardan iborat.Ularning har biri un alohida test yozamiz. 
#Bu methodlarni CarTest ichiga yozishni unutmaymiz.

#Navbat get_info() metodiga. 
# bu method ham obyektning xususiyatlaridan kelib chiqgan holda 2 xil qiymat qaytarishi mn,demak testimiz bu ikki holatni hisobga olishi kk.
def test_get_info(self):
    avto1_info="GM Malibu,2020-yil, 0km yurgan."
    self.assertEqual(avto1_info,self.avto1.get_info())
    # avto1 narhi va km o'zgartiramiz
    self.avto1.set_price(50000)
    self.avto1.add_km(20000)
    avto1_info = "GM Malibu,2020-yil,20000km yurgan.Narhi: 50000"
    self.assertEqual(avto1_info,self.avto1.get_info())
unittest.main()
