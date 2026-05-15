#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:22:54 2026

@author: mirzo
"""

# for tsiki pastdagui ko'rinishda bo'ladi. 
#print esa obzasdan yoziladi.
mehmonlar = ["Ali","Vali", "BEkzod","Jumali"]
for mehmon in mehmonlar: 
    #print("Salom",mehmon)
    #print("Hayr",mehmon)
    

    print(f"Hurmatli {mehmon}, sizni To'y bazmimizga taklif qilamiz")
    print("Hurmat bn Sultonovlar oilasi\n")
    
#sonlarda for tsiklini ihslatish
sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")
    
    
snlar = list(range(1,11))
for sn in snlar:
    print(f"{sn} ning kubi {sn**3} ga teng")
    
    
#   
snolar = list(range(1,11))
snolar_kv = []
for sno in snolar:
    snolar_kv.append(sno**2)
print(snolar)
print(snolar_kv)


# 
#dostlar = []
#print("5 ta eng yaqin do'stingizni kiriting")
#for n in range(5):
 #   dostlar.append(input(f"{n+1} - do'stingizni ismini kiriting:"))
#print(dostlar)




#Amaliyot 1
oila = ("Dadam","Onam","Opam","Singlim", "Ukam", "Men")
for oilam in oila:
    print(f"Biz Oilada 6 kishimiz:{oilam}")
print("Function", len(oila)," marata takrorlandi")

#Amaliyot
toq_sonlar = list(range(10,100,2))
for tr_son in toq_sonlar:
    print(f" {tr_son} ning kubi:  {tr_son**3}\n")

# Amaliyot 3
#ev_kino = []
#print("Pastga 5ta sevimli kinoingizni kiriting ")
#for k in range(5):
 #   sev_kino.append(input(f" {k+1} sevimli kino nomini kiriting: "))
#print(sev_kino)

# Amaliyot 4
inat = []
tyu = int(input("nechta kishi bn suhbatlashdingiz? ")) # bu yerda int yozmasak inputga keladigan sonlar string shaklida keladi.int orqali raqamga o'zgartiramiz
for t in range(tyu):
    inat.append((input(f"{t+1} - Ularning ismlarini kiriting:")))

print(inat)






























    