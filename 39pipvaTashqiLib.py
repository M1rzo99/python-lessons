# PIP 
# Tashqi paketlarni o'rnatish uchun Pythonda maxsus pip paket menejeri mavjud. pip odatda Python bilan birga o'rnatiladi, lekin turli sabablarga ko'ra kompyuteringizda pip o'rnatilmagan bo'lsa, uni quyidagi sahifadan yuklab olishnigiz mumkin: https://pypi.org/project/pip/

# # Paket menejer yordamida tashqi paketlarni o'rnatish juda oson, buning uchun Windows terminalda (cmd) (yoki  Spyder konsolida, yoki  PyCharm konsolida va hokazo)pip install paket_nomi komandasidan foydalanasiz.


# googletrans
# pip install googletrans

# Ushbu modul yordamida Googlening tarjimonlik xizmatiga murojat qilib, istalgan matnni turli tillarga tarjima qilishimiz mumkin. Moduldan foydalanish uchun avvalo googletrans modulidan Translator klassini import qilamiz va bu klassdan yangi obyekt yaratamiz (tarjimon). Bevosita tarjimonlik xizmatiga murojat qilish uchun tarjimon obyekti ichidagi .translate() metodiga murojat qilamiz va parametr sifatida tarjima qilish kerak bo'lgan matnni uzatamiz. 
# matn_uz = "Python dunyodagi eng mashhur dasturlash tili"

from googletrans import Translator
tarjimon = Translator()
matn_uz = "Python dunyodagi eng mashhur dasturlash tili"
tarjima = tarjimon.translate(matn_uz,src="uz",dest="ru") # Agar ingliz tilidan boshqa tillarga tarjima qilmoqhchi bo'lsak,dest="" shu tilni qisqartmasni berib ketamiz
print(f"Tarjima: {tarjima.text}")
 # odatda python tarjima qilinishi kerak bo'lgan matnni avtomatik aniqlayti.Lekin matn tilini bildirmoqchi bo'lsaiz, src=" " orqali berib ketish mn.

# Requests
# pip install requests
#Bu paket yordamida Pythonda veb sahifalarga murojat qilishimiz (so'rov yuborishimiz) va ulardan qaytgan ma'lumotlar ustida turli amallar bajarishimiz mumkin. 
# Misol uchun quyida requests yordamida kun.uz sahifasini to'liqligicha toritb olamiz:

# import requests
# from pprint import pprint
# url = "https://kun.uz/uz/news/main"
# r = requests.get(url)
# pprint(r.text) # r.text orqali sahifadagi barcha matnni olamiz

#NOTE - API bu malum bir web xizmatga so'rov yuborish orqali undan foydalanish.
#Internetda restcountries.eu sahifasi mavjud. Bu sahifa orqali dunyodagi davlatlar haqida turli maʻlumotlarni olishingiz mumkin.
#  Sahifadan foydalanish qulay boʻlishi uchun esa, sahifa yaratuvchilari bir nechta tayyor API lar eʻlon qilishgan. Misol uchun Oʻzbekiston haqida maʻlumot olish uchun quyidagi manzilga soʻrov yuborasiz: https://restcountries.eu/rest/v2/name/Uzbekistan

# Internetda restcountries.eu sahifasi mavjud. Bu sahifa orqali dunyodagi davlatlar haqida turli maʻlumotlarni olishingiz mumkin. Sahifadan foydalanish qulay boʻlishi uchun esa, sahifa yaratuvchilari bir nechta tayyor API lar eʻlon qilishgan.
#  Misol uchun Oʻzbekiston haqida maʻlumot olish uchun quyidagi manzilga soʻrov yuborasiz: https://restcountries.eu/rest/v2/name/Uzbekistan÷
# import requests
# country = "Uzbekistan"
# url = f"'https://api.restcountries.com/countries/v5/codes.alpha_2/CA?pretty=1{country}"
# r = requests.get(url)
# r_json = r.json()[0]
# print(r_json['capital'])

# BeautifulSoup4
#pip install beautifulsoup4 


#BeautifulSoup juda kuchli modullardan biri bo'lib, bu modul yordamida turli veb sahifalardan istalgan ma'lumotlarni yig'ishtirib (scarpping) olish mumkin. Biror kishining instagram sahifasidagi barcha rasmlar deysizmi, Facebook guruhidagi barcha postlar va izohlar deysizmi, oldi-sotdi bozoridagi e'lonlar deysizmi, marhamat, bs4 moduli yordamida buni bemalol avtomatlashtirish mumkin. 

#Odatda bs4 moduli requests moduli bilan hamkorlikda ishlaydi. Keling, sodda misol kor'amiz. Avvalgi bo'limda, requests yordamida kun.uz sahifasining html kodini olgan edik. Endi esa bs4 yordamida html sahifadan oxirgi yangiliklarning mavzusini ajratib olamiz.

import requests
from bs4 import BeautifulSoup
url = "https://kun.uz/uz/news/main"
r  = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
news = soup.find_all(class_="news-title") # yangiliklar mavzusini ajratib olamiz.
print(news[0].text) # Birinchi yangiliklarni konsolga chiqaramiz.
