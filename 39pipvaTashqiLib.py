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
tarjima = tarjimon.translate(matn_uz,dest="ru") # Agar ingliz tilidan boshqa tillarga tarjima qilmoqhchi bo'lsak,dest="" shu tilni qisqartmasni berib ketamiz
print(f"Tarjima: {tarjima.text}")

