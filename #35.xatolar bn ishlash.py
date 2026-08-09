
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

# yosh = input("Yoshingizni kiriting: ")

# try: 
#         yosh = int(yosh)

# except:
#         print("Butun son kiritmadingiz!")


# else:
#         print(f"Siz {2026-yosh} yilda tug'ilgansiz")
        
# print("Dastur tugadi")     
        
# Lekin yuqoridagi usul har doim ham qo'l kelavermaydi.
        
        
# Malum turdagi xatolarni ushalsh

# Xatolarni turlari ko'p, except opertori yordamida esa biz aynan qaysi xatoalrni ushlamoqchi ekanimizni ham ko'rsatib ketishimiz mn.
# MS: yuqoridagi misolda int()  funksiyasi ValueError xatosini qaytaradi.
#Agar biz faqatgina shu error ni ushlamoqchi bo'lsak, kodimizini quyidagicha o'zgartiramiz:
    
#ValueError
# yosh = input("Yoshingizni kiriting: ")

# try: 
#         yosh = int(yosh)

# except ValueError:
#         print("Butun son kiritmadingiz!")

# else:
#         print(f"Siz {2026-yosh} yilda tug'ilgansiz")
        
# print("Dastur tugadi") 

# ZeroDivisionError - 0 ga bo'lish xatoligi.

x,y=5,10
try:
   natija =  y / (x-1)
    
except ZeroDivisionError:
    print("Yuqoridagi sonni 0 ga bo'lib b'lmaydi")
else:
    
    print(f" Natija: {natija}")
    
# KeyError - lug'atda mavjud bo'lmaagan kalitga murojat qilishda kelib chiqadi

user={
 "username":"q13",
 "status":"admin",
 "email":"accaunoff99@gmail.com",
 "phone":"01042276466"
 }
key="tel"

try:
    print(f"Foydalanuvchi: {user[key]}")
except KeyError:
    print("Bunday kalit mavjud emas!")

# FileNotFounder - mavjud bo'lmagan fileni so'raganimizda

#Avvalgi darsimizda fayllar bilan ishlashni o'rgangan edik. Fayllarni biz o'qish (open(filename,'r')) yoki yozish (open(filename,'w')) uchun ochishimiz mumkin. Agar faylga ma'lumot yozish uchun ochishda, mavjud bo'lmagan faylga murojat qilsak, Python yangi fayl yaratadi. Lekin, faylni o'qish uchun ochishda fayl nomini xato yozsak, yoki mavjud bo'lmagan faylni ochmoqchi bo'lsak FileNotFoundError (fayl topilmadi) xatoligi yuzaga keladi. 


# filename = "data.txt" #bunday file mavjud emas
# with  open(filename) as f:
#     text = f.read()
#  Natija: FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'

# Tepadagi xatolini ushlab qolish un except FileNotFoundError dan foydalanamiz

filename = "data.txt" #bunday file mavjud emas
try:
    
 with  open(filename) as f:
     text = f.read()
except FileNotFoundError:
    print(f"Kechirasiz,{filename} fayli mavjud emas.Boshqa faylni tanlang!")
   
    
   
    
   
    
   
    
   
    
   
    
   

        
        