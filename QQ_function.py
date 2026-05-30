# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sat May 30 22:20:57 2026

# @author: mirzo
# """

# Avvalgi darsimizda yaratgan barcha funksiyalarimiz konsolga ma'lumot chiqarayotgan edi. Aslida, aksar holatlarda bu g'ayritabiiy. Sababi, dasturchi sifatida biz konsolga chiqqan ma'lumotdan unumli foydalana olmaymiz. Konsoldagi qiymatni o'zgaruvchiga yuklab, undan kelajakda foydalanib ham bo'lmaydi. Mana shunday holatlarda, funksiyadan unumli foydalanish uchun undan biror qiymatni qaytarish maqsadga muvofiq bo'ladi.
# FUNKSIYADAN ODDIY QIYMAT QAYTARISH
# Keling ism va familiya degan parametrlarni olib, toliq_ism qaytaradigan sodda funksiya yasaymiz.

# Copy
# def toliq_ism_yasa(ism, familiya):
#     """Toliq isma qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz
# Yuqoridagi funksiyamizga ahamiyat bersangiz, uning badanida endi print() funksiyasi yo'q. Buning o'rniga, funksiyamiz return operatori yordamida toliq_ism degan o'zgaruvchining qiymatini qaytaradi.
# Endi funksiyadan to'g'ri foydalanish uchun u qaytargan qiymatni biror o'zgaruvchiga yuklashimiz kerak:

# Copy
# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov')
# Yuqoridagi kodlarni bajarganimizda konsolga hech narsa chiqmaydi. talaba1 va talaba2 o'zgaruvchilarining qiymatini ko'rish uchun esa print() funksiyasidan foydalanamiz.

# Copy
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# Natija: Darsga kelmagan talabalar: Olim Hakimov va Hakim Olimov
# Demak, qiymat qaytaradigan funksiyaning afzalligi shundaki, biz bu qiymatlardan keyin ham bemalol foydalanishimiz mumkin.
# Funksiya ichidagi o'zgaruvchilar mahalliy yoki ichki o'zgaruvchilar deyiladi (local variables). Ichki o'zgaruvchilar faqatgina funksiya ichida mavjud bo'ladi, ularga tashqaridan murojat qilib bo'lmaydi. Shuning uchun ham funksiya o'zgaruvchi emas qiymat qaytaradi.
# IXTIYORIY ARGUMENTLAR
# Avvalgi darsizmida funksiyalarga standart parametr berishni ko'rgan edik. Huddi shu usul bilan, ba'zi argumentlarni ixtiyoriy qilishimiz mumkin. Ya'ni funksiya ishlashi uchun bu agrumentarni kiritish majburiy emas, ixtiyoriy bo'ladi.
# Keling avvalgi funksiyamizni o'zgartiramiz va unga yana bitta otasiningismi degan paramter qo'shamiz, lekin bu parametr ixtiyoriy bo'ladi. Buning uchun funksiya yaratishda otasining_ismi='' deb yozib ketamiz. 

# Copy
# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# Yuqoridagi funksiyani tahlil qiladigan bo'lsak, 3-qatorda biz otasiningismi parametri bo'sh yoki yo'qligini tekshiramiz. Pythonda if dan so'ng bo'sh bo'lmagan matn (string) yozsak, bu shart True qaytaradi. Demak, bu ixtiyoriy parametr kiritilgani yoki yo'qligiga qarab, funksiyamiz turlicha qiymat qaytaradi.

# Copy
# talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
# talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# Natija: Darsga kelmagan talabalar: Olim Hakimov va Hakim Abrorovich Olimov
# FUNKSIYADAN LUG'AT QAYTARAMIZ
# Funksiyadan sodda qiymat emas, ro'yxat, lu'gat va boshqa ma'lumot turlarini ham qaytarishimiz mumkin.  Quyidagi funksiya ham mashina haqidagi ma'lumotlarni jamlab, ularni lug'at ko'rinishida qaytaradi:

# Copy
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
# E'tibor bering, narhi nomli parametrga None standart qiymatini berib ketdik. None Pythonda mavjud emas ma'nosini beradi, va if yordamida tekshirganda False mantiqiy qiymatini qaytardi. 
# Quyidagi kodni tahlil qilishni sizga vazifa sifatida qoldiramiz:

# Copy
# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

# Natija
# FUNKSIYADAN RO'YXAT QAYTARAMIZ
# Biz avvalroq range() funksiyasi bilan tanishgan edik. Bu funksiya 2 ta son qabul qilib, shu ikki son orali'g'idagi sonlarni qaytaradi. Keling biz oraliq() degan yangi funksiya yaratamiz. range() dan farqli ravishda, funksiyamiz 2 son oralig'idagi sonlarni ro'yxat ko'rinishida qaytarsin.

# Copy
# def oraliq(min,max):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# Funksiyani tekshiramiz:

# Copy
# print(oraliq(0,10))
# print(oraliq(10,21))

# Natija
# Yuqoridagi funksiyaga uchinchi, qadam deb nomlangan ixtiyoriy parameterni qo'sha olasizmi?

# Copy
# print(oraliq(0,21,2)) # 0 dan 21 gacha 2 qadam bilan
# Natija: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# FUNKSIYALARNI TSIKLDA ISHLATISH
# Funksiyalarni takrorlash uchun tsikldan foydalanishimiz mumkin. Quyidagi misolda biz while yordamida avvalroq yaratgan avto_info funksiyamizni bir necha bor chaqiramiz va salondagi avtolar ro'yxatini shakllantiramiz. Bunda, ro'yxatning har bir elementi avto_info funksiyasidan qaytgan lug'at bo'ladi.

# Copy
# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
# Yuqoridagi funksiyani Pythonda bajarib kor'ing. Ro'yxatga bir necha qiymatlar qo'shing. Natijalarni konsolga chiroyli qilib chiqaring:

# Kutilgan natija
