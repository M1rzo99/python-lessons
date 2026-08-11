#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:19:42 2026

@author: mirzo
"""

#Yuqorida matn qaytaruvchi funksiyani tekshirishni ko'rdik. Keling endi sonlar bilan ishlashni ko'ramiz. Misol tariqasida yangi circle.py modulini yaratamiz va uning ichida doiraning yuzini ( 

#   ) va perimetrini ( 

# 2πr)  hisoblaydigan funksiyalar yozamiz:
    
def getArea(r,pi=3.14159):
    """Doiraning yuzini qaytaruvchi funksiya"""
    return pi*(r**2)

def getPerimetr(r,pi=3.14159):
    """Doiraning perimetrnini qaytaruvchi funksiya"""
    return 2*pi*r


#E'tibor bering, ikki funksiya ham, agar foydalanuvchi aniq qiymat bermasa, 
# π
# π ning qiymatini standart argument sifatida 3.14159 ga teng deb qabul qilayapti. Ushbu funksiyalarni tekshirish uchun alohida circle_test.py test dasturini yozamiz