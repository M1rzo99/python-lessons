# Xususiyatlarni tekshirish 
# Klassdan obyekt yaratishda,obyekt xususiyatlarini parametr ko'rinishida beramiz. 
# Quyidagi testda aynan shu jarayon to'g'ri kechganini tekshiramiz.

import unittest
from car import Car

class CasrTest(unittest.TestCase):
    """Car klassini test qilish"""

    def test_create(self):
        # avto1 obyektini km va narhini bilmasdan tekshiramiz
        avto1 = Car("BMW","camry",2020)
        # Qiymatlar mavjudligini assertIsNotNone methodi bn tekshiramiz
        self.assertIsNotNone(avto1.make)
        self.assertIsNotNone(avto1.model)
        self.assertIsNotNone(avto1.year)
        # Qiymat mavjud emasligini assertIsNone metodi bn tekshiramiz 
        self.assertIsNone(avto1.price)
        # Qiymat tengligini assertEquals metodi bn tekshiramiz
        self.assertEqual(0,avto1.get_km())
        # Yangi Obyekt yaratamiz va narhni ham ko'rsatamiz
        avto2 = Car("BMW","carmy",2020,price=45000)
        self.assertEqual(45000,avto2.price)
unittest.main()


# Testimizni tahlil qilamiz. Dastaval biz obyektimiz to'g'ri yaratilayotganini tekshrish uchun avto1 obyektini 3 ta prametr bilan yaratib oldik (make, model, year) va  bu xususiyatlar bo'sh emasligini  assertIsNotNone() metodi bilan tekshirdik. 

#avto1 obyektini yaratishda uning narhini ko'rsatmadik, demak bu xususiyat standart qiymat (None) ga teng bo'lishi kerak. Buni tekshirish uchun esa assertIsNone() metodiga murojat qildik. Vanihoyat, avtomobil kilometraji 0 ga teng ekanligini assertEquals() metodi yordamida test qildik.

#Test so'ngida biz yana bir obyekt yaratdik (avto2) va bu safar avtomobil narhini ko'rsatganimiz uchun assertEquals() metodi yordamida bu qiymat to'g'ri saqlanganini tekshirib oldik.

#Testlarni yozishni davom etamiz. Navbat obyektga tegishli turli metodlarga.

#Test dasturlarni alohida faylga yozishni unutmang.