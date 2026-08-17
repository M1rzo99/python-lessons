
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