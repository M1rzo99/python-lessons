#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 18:30:33 2026

@author: mirzo
"""

#1.Amaliyot
#Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya
def eng_katta(a,b,c):
    katta = a
    
    if b> katta:
        katta=b
        
    if c> katta:
        katta=c
        
    return katta
print(eng_katta(10,8,7))

#2.Amaliyot
#Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya

def get_fam(mother,father,brother):
    return f"{mother},{father},{brother}".title()
print(get_fam("khamida", "maqsud", 'latif'))

#3.Amaliyot
#Berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya

def juftSon(sons):
    juftlar=[]
    for son in sons:
        if son %2 ==0:
            juftlar.append(son)
    return juftlar

sons=[1,2,3,4,5,5,6,7,8,9,10]
print(juftSon(sons))
    
    
    
    
    
    
    
    
    
    
        