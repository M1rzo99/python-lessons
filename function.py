# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Thu May 28 21:48:28 2026

# @author: mirzo
# """

# Funksiya ma'lum bir vazifani bajarishga mo'ljallangan kodlar yig'indisi. Biz shu paytgacha bir nechta tayyor funksiyalardan foydalanib keldik. Misol uchun print() funksiyasi konsolga matn chiqarish uchun, range() funksiyasi esa ma'lum oraliqdagi sonlarni yaratish uchun ishlatiladi.  
# Aslida har qanday funksiyaning ortida ham bir necha qatordan iborat kod bo'ladi, lekin biz funksiyaga murojat qilganda uning nomini yozamiz xolos. Funksiya ortidagi kod esa biz uchun yashirin bo'lib qolaveradi. Funksiyalarning qulayligi ham shunda. Dastur davomida ma'lum bir kodlarni qayta-qayta yozmaslik uchun biz ularni jamlab, bitta funksiya ichiga joylashimiz va dastur davomida bu kodlarga funksiya nomi orqali murojat qilishimiz mumkin. 
# Funksiyalar turlicha bo'ladi, ba'zi funksiyalar sizdan qiymat qabul qilib, konsolga biror ma'umot chiqaradi, ba'zilari esa sizdan qabul qilgan qiymat ustida turli amallar bajarib yangi qiymat qaytaradi. Foydalanuvchidan mutlaqo qiymat qabul qilmaydigan funksiyalar ham mavjud. 
# Ushbu mavzuda siz qanday qilib Pythonda yangi funksiya yaratish, unga murojat qilish, tekshirish va to'g'rilashni o'rganasiz. Shuningdek darsimiz yakunida dasturimizni bir nechta faullarga ajratishni va funksiylarani alohida, module deb ataluvchi fayllarga joylashni ham o'rganamiz.
# FUNKSIYA YARATAMIZ
# Keling oddiy, salom_ber deb nomlangan funksiya yaratamiz. Bu funksiya murojat qilganimizda konsolga "Assalom alaykum!" degan xabarni chiqarsin.

# Copy
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
# Kodni qatroma-qator tahlil qilaylik:
# Avvalo def operatori yordamida Pythonga funksiya yaratayotganimizni bildirdik. def dan so'ng esa funksiyamizga nom berdik va qavslarni ochib, yopdik. Bizning funksiyamiz foydalanuvchidan hech qanday qiymat qabul qilmaydi, shuning uchun ham qavs ichi bo'sh. Keyingi misollarda foydalanuvchidan qiymat qabul qiluvchi funksiyalarni ham ko'ramiz.
# def qatoridan keyin o'ngga surib yozilgan har qanday kod funksiyaning badani hisoblanadi. 2-qatorda biz uchta ketma-ket qo'shtirnoq ichida funksiya haqida ma'lumot berdik. Python mana shu ma'lumotni o'qib, dasturchi funksiya haqida bilmoqchi bo'lganda aynan shu matnni ko'rsatadi. 
# Oxirgi qatorimizda esa "Assalomu alaykum!" matnini konsolga chiqarishni buyurdik. Bizning sodda funksiyamizning asosiy vazifasi ham shu.
# Mana funksiya tayyor. Endi bu funksiyadan foydalanish uchun uni chaqiramiz. Buning uchun funksiya nomini yozamiz va qavslarni ochib, yopamiz (esingizda bo'lsa bizning funksiyamiz qiymat qabul qilmaydi, shuning uchun qavslar ichi bo'sh).

# Copy
# salom_ber()
# Natija: Assalomu alaykum!
# Funksiyaga nom berishda fe'l, ya'ni harakatni bildiruvchi so'zlar yoki jumlalardan foydalaning. Bu bilan siz o'zgaruvchi va funksiya o'rtasini farqlashingiz oson bo'ladi. Misol uchun, yuqorida biz funksiyamizni salom emas salom_ber deb nomladik.
# FUNKSIYAGA QIYMAT UZATISH
# Avvalgi sodda funksiyamiz foydalanivchidan hech qanday qiymat olmaydi va barchaga birday "Assalomu alaykum!" deb javob qiladi. Keling funksiyaga o'zgartirish kiritamiz, funksiya foydalanuvchi ismini qabul qilib, unga ismi bilan murojat qilsin. Buning uchun funksiya nomidan keyin, qavs ichida foydalanuvchi berishi kerak bo'lgan qiymatni ko'rsatamiz.

# Copy
# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# Mana endi fuknsiyamiz foydalanuvchidan ism degan qiymatni ham kutadi.

# Copy
# salom_ber('hasan')
# Natija: Assalomu alaykum, hurmatli Hasan!
# Agar funksiyaga murojat qilishda, unga qiymat bermasak xatolik vujudga keladi:

# Copy
# salom_ber()
# Natija: TypeError: salom_ber() missing 1 required positional argument: 'ism'
# DOCSTRING
# Avval aytganimizdek, funksiya yaratganda, funksiya qanday ishlashi haqida qisqacha ma'lumot berib ketish o'zimiz uchun ham, kelajakda bizni funksiyamizni ishlatadigan boshqa dasturchilar uchun ham juda foydali bo'ladi. Quyidagi funksiyaning 2-qatorda biz funksiya haqida ma'lumot berdik. Bu qator docstring deyiladi. Murakkab funksiyalar uchun docstringni bir necha qatorga bo'lib yozishingiz mumkin

# Copy
# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib, 
#         unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# Xo'sh, bu ma'lumot qachon va qayerda ko'rsatiladi? Dastur yozish jarayonida funksiya nomini yozishingiz bilan, docstring ko'rsatiladi:

# Docstring - funksiya haqida ma'lumot
# Docstringni konsolga chiqarish uchun print(funksiya_nomi.__doc__) deb ham yozishimiz mumkin:

# Copy
# print(salom_ber.__doc__)

# Docstring
# FUNKSIYAGA BIR NECHA BOR MUROJAT QILISH
# Funksiya yaratishning asl maqsadlaridan biri, biz unga qayta-qayta, yangi qiymatlar bilan murojat qilishimiz mumkin. 

# Copy
# salom_ber('hasan')
# salom_ber('olim')
# Natija:
# Assalomu alaykum, hurmatli Hasan! 
# Assalomu alaykum, hurmatli Olim!
# ARGUMENT VA PARAMETER
# Funksiya yaratishda, qavs ichida berilgan, funksiya to'g'ri ishlashi uchun uzatiladigan qiymat parameter deb ataladi. Yuqoridagi misolda ism bu salom_ber funksiyasining parametri. 
# Foydalanuvchi funksiyaga murojat qilishda funksiyaga uzatgan qiymat esa argument deb ataladi. salom_ber('hasan') kodida 'hasan' bu argument. 
# Ba'zi manbalarda yoki darslarda argument va parametr so'zlari almashtirib ishlatilishi ham kuzatiladi.
# FUNKSIYAGA BIR NECHTA ARGUMENT UZATISH
# Shunday funksiyalar bor, bir emas bir nechta parameter talab qilishi mumkin, foydalanuvchi esa o'z navbatida bir nechta argumentlar taqdim qilishi kerak. Funksiyaga argument uzatishning bir necha usuli bor, keling ular bilan birma bir tanishamiz.
# TO'G'RI TARTIBDA UZATISH
# Bu usulda, funksiya parametrlari qaysi tartibda yozilgan bo'lsa, argumentlar ham aynan shu ketma-ketlikda uzatilishi kerak. Keling bitta misol ko'ramiz. Quyidagi funksiya foydalanuvchining ismi va familiyasini parametr sifatida qabul qilib, ularni jamlab xabar chiqaradi.

# Copy
# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
# Yuqoridagi funksiya to'g'ri natija chiqarishi uchun argumentlarni ism va familiya ketma-ketligida kiritishimiz lozim.

# Copy
# toliq_ism('olim','hakimov')
# Natija: 
# Foydalanuvchi ismi: Olim 
# Foydalanuvchi familiyasi: Hakimov
# Agar argumentlarni noto'g'ri ketma-ketlikda bersak, natija ham biz kutganday chiqmaydi:

# Copy
# toliq_ism('hakimov','olim')
# Natija:
# Foydalanuvchi ismi: Hakimov 
# Foydalanuvchi familiyasi: Olim
# Ko'p xolatlarda esa, argumentlarni noto'g'ri tartibda uzatish xatolikka ham olib kelishi mumkin.

# Copy
# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2020-tugilgan_yil} yoshda")

# Copy
# yosh_hisobla('olim', 1997)
# Natija: Olim 23 yoshda

# Copy
# yosh_hisobla(1997, 'olim')
# Natija: AttributeError: 'int' object has no attribute 'title'
# KALIT SO'Z BILAN UZATISH
# Yuqoridagi kabi holatlarning oldini olish uchun argumentlarni parametr nomi bilan qo'shib uzatishimiz mumkin. Buning uchun funksiyaga o'zgartirish kiritish talab qilinmaydi.

# Copy
# yosh_hisobla(tugilgan_yil=1997, ism='olim')
# Natija: Olim 23 yoshda
# # 