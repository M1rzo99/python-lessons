
# Kirish
# Python datrulash tili kunda-kunga ommaplashib borayapti. Bunga sabab, birinchi navbatda Pythonning sodda va tushunarli sintaksi sabab bo'lsa,ikkinchi ehtimol pythonning keng qamrovli kutubxonalar to'plamidir.
# Ushbu darsda pythonning bazi bir muhim modullari bn tanishamiz. Standart kutubxonaning to'liq tarkibi bn https://docs.python.org/3/library/ sahifasida tanishing


#1.datetime - sana va vaqat
#ushbu modul yordamida Pythinda sanalar bn ishashimiz mn. Moduldan foydalanishdan avval uni import qilamiz.Har gal moduldan foydalanishda datetime deb qayta yozmaslik unm import qilishda modulga dt nomini beramiz

import datetime as dt
hozir = dt.datetime.now() # Hozrigi vaqt va sanani ko'rish un
print(hozir)
# Natijasdan ko'rib turganimizdek yil,oy,kun,minut,sec,millisec ko'roinishida chiqayapti. Biz bu qiymatlani istaganimizni maxsus methodlar yordamida ajratib olishimiz mn.

# sanani ajratib olish
print(hozir.date())
# vaqtni ajratib olish
print(hozir.time())
# soatni ajratib olish
print(hozir.hour)
# minutni ajratib olish un
print(hozir.minute)
# secundni ajratib olish
print(hozir.second)

# agar bugunni sanasi talanb qilinsa, daterime ihcidagi date.today moduliga murojat qilamiz
bugun = dt.date.today()
print(f"Bugungi sana: {bugun}")

# agar biror sanai qo'lda kiritish talab qilinsa .date() methodiga kerakli sananni(yil,oy,kun) ko'rinishida kiritamiz
ertaga = dt.date(2026,8,18)
print(f"Ertangi sana: {ertaga}")

# Faqatgina vaqt bn ishlash un .datetime.now().time() metodiga murojat qilishmiz mn:
hozir = dt.datetime.now()
vaqtHozir = hozir.time()
print(f"Hozir soat: {vaqtHozir}")
# Istalgan vaqtni qo'lda kiritish un esa .time() metodiga kerakli vaqtni(soat,min,sek) ko'rinishida beramiz

vaqtKeyin = dt.time(23,45,00)
print(f"Kechki vaqt: {vaqtKeyin} da ko'rishamiz!")

# ayirish operatori yordamida sanalar va vaqtlar orasidagi farqni hisoblash mn:
bugun  = dt.date.today()
ramazon = dt.date(2027,2,8)

farq = ramazon -bugun
print(farq)
print(f"Ramazonga {farq.days} kun qoldi.")


# Huddi shu kabi ikki vaqt oralig'ini sekundlarda yoki soatlarda ham ko'rishimiz mn:
hozir = dt.datetime.now()
futbol = dt.datetime(2021, 3, 10, 23, 45, 00)
farq= futbol-hozir
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Futbol boshlanishiga {sekundlar} sekund qoldi")
print(f"Futbol boshlanishiga {minutlar} minut qoldi")
print(f"Futbol boshlanishiga {soatlar} soat qoldi")


# yuqoridadgi sanaslr AQSH tandartiga koʻra, yil-oy-kun koʻrinishida chiqayapti. Sanani oʻzimizga moslab chiqarish uchun .strftime() metodini chaqiramiz, va sanani oʻzimizga qulay formatda chiqaramiz.

# vaqtni millisekundsiz chiqaramiz
vaqt = hozir.strftime("%H:%M:%S")
print(f"Hozir soat: {vaqt}")

# sanani kun-oy-yil koʻrinishida chiqaramiz
sana = hozir.strftime("%d-%m-%Y")
print(f"Bugun sana: {sana}")

# sanani kun/oy/yil koʻrinishida chiqaramiz
sana_vaqt = hozir.strftime("%d/%m/%Y, %H:%M")
print(sana_vaqt)


# math —MATEMATIK FUNKSIYALAR

# bu modul o'z ichida metamatikaga oid turli funksiyalar va o'zgaruvhcilarni saqlaydi.
# Keling ularni bazilari bn tanishamiz.

#1. P ning qiymati
import math
PI = math.pi
print(f"PI ning qiymati: {PI}")

#2. e - natural logarifm asosi. e ko'pincha o'sish va kamayish jarayonlarini hisoblashda ishlatilinadi.
# Misol un: bankdagi foizlar,aholi o'sishi,fizikadaffi jarayonlar,ehtimolli,AI va statistika.
# Logarifm nima? Qaysi darajaga ko'tarish kerak Ya'ni 2 ni nechanchi darajaga ko'tarsak x(8 )bo'ladi?
# loga b = c. log2 8 = 3. 2 ning 3 darajasi 8 bo'ladi
# log10 100=2 -> 10 ning 2 chi darajasi 100 bo'ladi.
E = math.e
print(f"e ning qiymati: {E}")

#3. Trigonametriya. Modul tarkibida deyarli barcha trigonometrik funksiyalar mavjud(cos,sin,tangens,across va hkz)
math.sin(math.pi/2)
math.cos(0)
math.tan(PI)

# shuningdek degrees sva radians methodlari yordamida burchakdan radianga va aksincha konvertasiya qilishimiz mn:
math.degrees(math.pi/2)
math.radians(90)

#4. Logorifmlar
# log() va log10() funksiyalari yordamida natural va o'n asosli logarifmlarni hisoblash mn.
#natural logarifm
print(math.log(5))
# 10 asosli logarifm
print(math.log10(100))

#5. Sonlarni Yaxlitlash

# Sonlarni Yaxlitlashning Pythinda maxsus round() funcsiyasi mavjud. Bunga qo'shimcha,math moduli ichidagi ceil() funksiyasi yordamida berilgan o'nlik sonni keyingi butun songa,floor() yordamida esa quyi butun songa yaqinlashtirish mn.
x=4.6
print(math.ceil(x)) # O'nlikdan yuqori butun songa
print(math.floor(x)) # O'nlikdan past butun songa

#6. Ildiz va daraja.
# Berilgan sonning kvadrat ildizini hisoblsdh un sqrt(), sonni darajaga oshirish un esa pow() funksiyalariga murojat qilamiz:
x=81
# kvadrat ildiz
print(math.sqrt(x))

print(math.pow(x,3)) # x ning kubi
print(math.pow(x,5)) # x ning 5-darajasi
print(math.pow(x,1/3)) # x dan kub ildiz. x ning qiymatini 3 marta o'ziga bo'lish demakdir.

# math moduli tarkibida boshqa funksiyalar ham mavjud. Yuqorida biz ularning ba'zilari bilan tanishdik. Bu modul asosan butun va oʻnlik sonlar bilan ishlashga moʻljallangan. Kompleks sonlar bilan ishlash uchun cmath moduliga murojat qilishingiz mumkin.



#pprint - CHIROYLI PRINT
# pprint yordamida turli o'zgaruvchilarni chiroyli ko'rinishda konsolga chiqarishimiz mn.BU bizga uzun lug'atlar,JSON fayllar yoki matnlar bn ishlashda juda asqotadi.
# Misol un bemor.json faylini yaratamiz, oldin print() keyin pprint() yodamida lug'atga chiqarib, farqini ko'ramiz.

from pprint import pprint
import json
filename="bemor.json"
with open(filename) as f:
    bemor = json.load(f)
#print(bemor)
pprint(bemor)


# RegEx - andoza yordamida matn izlash
#Pythondagi juda foydali modullardan biri bu re (regular expressions) moduli.
# Bu modul yordamida biror matn berilgan andozaga tushish, tushmalsigini tekshrib ko'rishimiz mumkin. Yoki berilgan andoza asosida matnlar orasidan kerakli matnlarni ajratib olish mumkin.


#Keling boshlanishiga sodda misol ko'ramiz. Quyida biz 3 ta so'z va so'zlarni tekshirish uchun andoza yaratdik. 
# Quyidagi andozamiz т harfidan boshlanuvchi (^т), р harfiga tugovchi (р$), 5 harfdan iborat so'zlarni qidiradi (^т...р$). 

#So'zlarni andozaga solishtirish uchun re.match() funksiyasidan foydalanamiz. 
# Agar tekshirgan so'zimiz andozaga mosh tushsa, re.match() metodi so'zni o'zini qaytaradi, aks holda None qiymatini qaytaradi.

# import re
# word1 = "темир"
# word2 = "томир"
# word3 = "тулпор"
#  # Yani bosh harfi T va oxirgi harfi R bn tugaydigan 5 harfdan ibordat so'zni qidiradi,mos kelsa shu so'zni chiqaradi bo'lmasa None qaytaradi.
# #andoza = "^т...р"
# print(re.match(andoza,word1))
# print(re.match(andoza,word2))
# print(re.match(andoza,word3))

# Keling endi,so'z topish o'yinida ishlatilgan so'zlar ro'yhatidan fiydalanamiz va ro'yhatdan biz bergan andozaga tushuvchi so'zlarni ajratib oalmiz
import re
from uzwords import words
andoza= "^a..a$"
matches = []
for word in words:
    if re.match(andoza,word,re.IGNORECASE):
        matches.append(word)
print(matches) 

# https://ihateregex.io/ - tel raqam,email yoki kerakli so'zlarni ajratib olish un andozalar to'plami.

# Pastdagi matndan biror bir email ni ajratib olamiz.
matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """
andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
email = re.findall(andoza,matn) # findall orqali emailni ajratib olshimiz mn.
print(email)

# Andoza yordammida foydalanuvhci kiritgan qiymatlarni ham ma'lum shartlarga jb berishini tekshirib olishimmiz mn.


# Kuchli parolni tekshirish
andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg = "Yangi parol kiriting"
msg += '(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, '
msg += '1 ta son va 1 ta maxsus belgi boʻlishi kerak): '
while True:
    password = input(msg)
    if re.match(andoza,password):
        print("Maxfiy so'z qabul qilindi")
        break
    else:
        print("Maxfiy so'z shartlarga mos kelmadi!")