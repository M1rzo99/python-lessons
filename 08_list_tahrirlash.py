# -*- coding: utf-8 -*-
"""
2026/05/14

# 08 Ro'yhatlarni tahrirlash

Mirzo

"""
# ro'yhatimizni alifbo ketma-ketligida tartiblash un .sort() dan foydalanamiz
# Agar Katta harflar bn aralshib kiritsak, katta harflar birinchi keladi, a emas
cars = ['bmw','audi','kia','gt','damas','carniobal']
print(cars)

cars.sort()
print(cars)

# agar sortlashda teskari tartibda islatmoqchi bo'lsak, alifbodagi eng oxirgi harflarni nazarda tutayapman
# .sort(reverse=True ni kiritamiz
cars.sort(reverse=True)
print(cars)

# Asl ro'yhatni o'zgartirmasdan, undan nussxa olib ishlatsak bo'ladi. .sorted() orqali ishlaymiz

mehmonlar  = ['gziz','nodir','abbos','nurik','odil','bobur']
print(sorted(mehmonlar))
# Bu yerda ham teskari ihslatsak boi'ladi
print(sorted(mehmonlar,reverse=True))


ages = [54,51,30,27,24,21]
ages.reverse()
print(ages)


# Ro'yhatimizdagi Elementlar sonini aniqlash un len(element) functiondan foydalanamiz
print("Listimizda", len(ages), "ta element bor" )

# range(0,10) orqali malum sondan, boshqa malum son orasidagi sonlar ketma-ketliigin aniqlash mn
# list(range(0,10)) orqali esa oraliqni ro'yhat shaklida tashkillashtirib olamiz
sonlar = list(range(0,10))
print(sonlar) 
# natija: 1,2,3,4,5,6,7,8,9

juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
toq_sonlar = list(range(1,20,2)) # 1 dan 20 gacha 2 qadam bilan
print(juft_sonlar) # 0,2,4,6,8,10,12,14,16,18,20
print(toq_sonlar) # 0,1,3,5,7,9,11,13,15,17,19 
# Qancha qaadamligni o'zinizni ixtiyorimizga qarab berishimiz mumkin


# Sonlardan tashkil topgan ro'yhatda, eng katta,kichik son va Sonlarning Umumiy qiymatini ham topish mn

sonla = [1200,1300,11000,3400,23,1]

#kichik = min(sonla) # ro'yhatdagi eng kichik son
#katta = max(sonla) # ro'yhatdagi ebg katta son
#umumiy = sum(sonla) # ro'yhatdagi umumiy sonlarni yig'indisini topish

# Ro'yhatdan bizga kerakli natijani kesib olish
#sonlarr = sonla[1:3]
#print(sonlarr)

# agar boshlangich qiymat kiritmasak boshidan oxirigacha kesib oladi
#sonn = sonla[:2] # 2- elementgacha kesadi
#sonn = sonla[3:] # 3- elementdan ro'yhat oxirigacha kesadi

# Ro'yhatdan nusxa yasaymiz
sonla2 = sonla[:] # shu usul orqali nusxa olamiz
sonla2.append(2)
sonla2.append(3)
print("Umumiy",sonla2)

# pythonda tuple  - o'zgarmas qiymat hisoblanadi
# tuple - () degani.elemfent qo'shish,o'chirish,o'zgartirib bo'lmaydi
ism_fam = ("Mirzo","Shomuratov")
print(ism_fam[0])

# bizda o'zgarmas bor va uni o'zgarirmoqchi bo'lsak, oddiy listga o'tiramiz, o'zgariramiz va yana tuple() ga qaytarib qo'yamiz

greed = ("oyim","dadam","singlim","opam","ukam")
greed = list(greed)
greed.append("xolam")
greed[1] = "akam"
print(greed)
greed = tuple(greed)
print(greed)




















 