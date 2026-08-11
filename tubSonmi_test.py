#Funksiyani alohida tubSonmi.py fayliga saqlaymiz. Funksiyani tekshirish uchun name.py dasturini yozamiz:
    
import unittest
from name import tubSon

class tubSonTest(unittest.TestCase):
    def test_True(self):
        self.assertTrue(tubSon(7))
        self.assertTrue(tubSon(193))
        self.assertTrue(tubSon(547))
        self.assertFalse(tubSon(3))
        
    def test_False(self):
        self.assertFalse(tubSon(6))
        self.assertFalse(tubSon(265))
        self.assertFalse(tubSon(489))
        self.assertFalse(tubSon(20))
unittest.main()

#Test davomida tubSonmi() funksiyasini bir nechta tub (7, 193, 547) va tub bo'lmagan (6, 265, 489) sonlar bilan chaqirdik. 
#Bunda assertTrue() metodi funksiyamiz haqiqatdan ham True qiymatini qaytarishini, assertFalse() metodi esa funksiyamiz False qiymat qaytarishini tekshiradi.


#TAQQOSLASH METODLARI
# TestCase klassi tarkibidagi boshqa taqqoslash metodlari ham mavjud:

# Metod   Nimani taqqoslaydi?
# assertEqual(a, b) a == b
# assertNotEqual(a, b) a != b
# assertTrue(x) x ning qiymati True
# assertFalse(x) x ning qiymati False

# assertIsNot(a, b)
# a bu b emas
#  assertIsNone(x)
# x ning qiymati None
#  assertIsNotNone(x)
# x ning qiymati None emas
#  assertIn(a, b)
# a b ning ichida
#  assertNotIn(a, b)
# a b ning ichida emas
#  assertIsInstance(a, b)
# a b ning vorisi
#  assertNotIsInstance(a, b)
# a b ning vorisi emas










