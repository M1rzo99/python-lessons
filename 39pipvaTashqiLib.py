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

# import requests
# from bs4 import BeautifulSoup
# url = "https://kun.uz/uz/news/main"
# r  = requests.get(url)
# soup = BeautifulSoup(r.text,"html.parser")
# news = soup.find_all(class_="news-title") # yangiliklar mavzusini ajratib olamiz.
# print(news[0].text) # Birinchi yangiliklarni konsolga chiqaramiz.


#  WorldCloud va Matplotib

#pip install wordcloud

#NOTE - pip install matplotlib

#ANCHOR - Wordcloud moduli yordamida katta matnlarda eng ko'p uchraydigan so'zlarni chiroyli qilib, so'zlar buluti chiqarish mumkin. 2020-yil yakunida, sariqdev sahifasida chop etilgan mashxur blogerlarning siluetlari ham aynan shu modul yordamida qilingan.


#NOTE - wordcloud moduli grafiklarni chizishga mo'ljallangan matplotlib moduli bilan hamkorlikda ishlaydi.

import requests

# from bs4 import BeautifulSoup
# from wordcloud import WordCloud 
# import matplotlib.pyplot as plt 


# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)

# soup = BeautifulSoup(r.text, 'html.parser')
# news = soup.find_all(class_="news-title")
# matn=""
# for n in news:
#     matn += n.text

# # kerakmas so'zlar
# stopwords = ["учун","бўйича","лекин","билан","ва","бор","ҳам","хил","йил"]
# # bulutni yaratamiz
# wordcloud = WordCloud(width = 1000, height = 1000, 
#                 background_color ='white', 
#                 stopwords = stopwords, 
#                 min_font_size = 20).generate(matn) 
  
# # plot the WordCloud image                        
# plt.figure(figsize = (8, 8), facecolor = None) 
# plt.imshow(wordcloud) 
# plt.axis("off") 
# plt.tight_layout(pad = 0) 
# plt.show() 


#pip install opencv-python

#openCV bu kompyuter yordamida rasm va video tasvirlar bilan ishlash uchun maxsus kutubxona. Bugungi kunda sun'iy intellekt yordamida tasvirlar bilan ishlaydigan dasturlarning deyarli barchasi openCV yordamida yaratiladi. 

#Bu dastur yordamida rasm va videolardagi turli obyektlarni "ko'rish", ajratib olish mumkin. Avtomobillar nomerini aniqlash, odamlarning yuzidan tanish, obyektlarni klassifikasiya qilish kabi dasturlarning kasari aynan openCV kutubxonasi yordamida ishlaydi

import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# copyright Tim Ruscia aka techwithtim
# code from https://github.com/techwithtim/OpenCV-Tutorials