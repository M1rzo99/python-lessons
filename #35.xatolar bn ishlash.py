
# EXCEPTIONS
# Avvalgi darslarimizning birida biz "Run time error" xatoliklari bilan tanishgan edik. Bunday xatolar dastur bajarish jarayonida kelib chiqadi va dasturning ishlashini to'xtatadi. Sintaks xatolikdan farqli ravishda Python bunday xatolarni dasturni bajarishdan avval aniqlay olmaydi. 
# Ushbu darsimizda qanday qilib mana shunday xatoliklarni jilovlashni o'rganamiz. Maqsadimiz xatolik yuz berganda dastur to'xtab qolishining oldini olish. Gap shundaki, dastur davomida xato yuz berganda Python maxsus exception (istisno) obyektini yaratadi. Agar bu obyekt "tutib" olinmasa, dastur bajarilishdan to'xtaydi.


# try-except

# Istisno obyektlarinbin ushlab qolish un pythonda try-except  operatorlari mavjud.
#Bu operatorlar quyidagicha ishaydi: try operatori badanida bajarilinihsi kerak bo'lgan kod yoziladi,except operatorida esa xatolik yuz berganda bajarilinishi kerak bo'lgan kod yoziladi.
# Shu xolatda dasturimi to'xtab qolmasdan bajarilinadi.

# yosh = input("Yoshingizni kiriting: ")
# yosh = int(yosh) # sonni butun singa o'tkazayapmiz
# print(f"Siz {2026-yosh} yilda tug'ilgansiz")

# Agar foydalanuvchi yoshini kiritganda butun son emas, o'nlik(12.4,3.2) son kiritsa ValuError beradi va dastur ishlashdan  to'xtaydi

#Keling,  yuqoridagi try-execpt yordamida xatolik chiqganda dasturimiz to'xtamasdan ishlashini ko'rib chiqamiz

# yosh = input("Yoshingizni kiriting: ")

# try: 
#     yosh = int(yosh)
#     print(f"Siz {2026-yosh} yilda tug'ilgansiz")
# except:
#     print("Butun son kiritmadingiz!")
# print("Dastur davom etayapti")
# print("Dastur tugadi")

# Yuqorida except functioni ishladi va dasturimiz to'xtab qolmadi.Keyingi qismlarga o'tganini console orqali ko'rish mn.


# try-except-else

# Yuqoridagi kodimizda biz try moduli ichida xato qaytarishi mumkin bo'lgan ifodani ham (tyil = int(tyil)), xato qaytmaganda bajarilishi kerak bo'lgan ifodani ham (print(f"Siz {2021-tyil} yoshdasiz") ) birdan yozib ketayapmiz. Aslida, bunday qilishimiz to'g'ri emas. 
# To'g'ri usuli, bu avval xatoga tekshirish va xato yuz bermaganda bajariladigan ifodani alohida, else blokida yozish:

yosh = input("Yoshingizni kiriting: ")

try: 
        yosh = int(yosh)

except:
        print("Butun son kiritmadingiz!")


else:
        print(f"Siz {2026-yosh} yilda tug'ilgansiz")
        
print("Dastur tugadi")     
        
# Lekin yuqoridagi usul har doim ham qo'l kelavermaydi.
        
        
        
        