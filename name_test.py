import unittest # unittest modulini import qilamiz va biz modul,function larni test qilishda yordam beradi,
from name import get_full_name # name nomli module ichidan biz test qilmoqchi bo'lgan functionni import qilamiz
from name import get_fam

# class NameTest(unittest.TestCase): # class ga nom beramiz va unttest niichidagi TestCaase dan foydalanamiz.
#     def test_toliq_ism(self): #Funksiya yaratamiz
#         formatted_name = get_full_name("mirzo", "shomuratov") #get_fil_name dagi qiymat 
#         self.assertEqual(formatted_name, "Mirzo Shomuratov")# Va biz kutayaotgan qiymat ni ko'rsatamiz
# unittest.main()

class My_fam(unittest.TestCase):
    def test_fam_memebers(self):
        format_fam_mem = get_fam("hamida",'maqsud','latif','iroda')
        self.assertEqual(format_fam_mem, "hamida,maqsud,latif,iroda")
                
unittest.main()


# Dasturni tahlil qilamiz:
# Dastavval unittest modulini chaqiramiz (import unittest)
# Keyingi qatorda name.py modulimizdan tekshirmoqchi bo'lgan funksiyamizni ham yuklab olamiz (get_full_name).
# 4-qatorda test klassini yaratamiz, bu klassunittest.TestCase klassidan meros oladi. Bu klass berilgan parametrlar uchun funksiyadan qaytgan qiymatlarni tekshirishga mo'ljallangan. Klassimizga o'zimiz istagan, tushunarli nom beramiz (NameTest). 
# Klassimiz ichida test_toliq_ism metodini yaratdik. Bu metod get_full_name funksiyasidan qaytgan qiymatni biz avvaldan bergan qiymatga teng yoki yo'q ekanini tekshiradi. Buning uchun esa maxsus .assertEqual() metodidan foydalandik. E'tibor bering, test medotlarning nomi har doim test so'zi bilan boshlanishi kerak.
# assertEqual() metodi ikki qiymat qabul qiladi va ularning teng ekanligini tekshiradi (assert ingliz tilidan tasdiqlash deb tarjima qilinadi). Agar get_full_name('alijon','valiyev') funksiyamiz to'g'ri ishlasa, funksiyadan 'Alijon Valiyev' qiymati qaytishi kerak. assertEqual() metodi aynan shuni tekshirishga mo'ljallangan.
# So'nggi qatorda unittest klassinini chaqiramiz, bu esa o'z navbatida biz yuqorida yozgan testni chaqiradi. 

# name_test.py dasturimizni bajaramiz va quyidagi natijani olamiz:

# Ran 1 test in 0.001s

# OK
# Natijadan bitta test bajarilganini va va bu test muvaffaqiyatli o'tganini (OK) ko'rishimiz mumkin.