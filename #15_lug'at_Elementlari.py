#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:00:37 2026

@author: mirzo
"""

# Lug'atlar bilan ishlash
talaba_0 = {
    "ism":"Mirzo",
    "familiya":"Shomuratov",
    "yosh":27,
    "fakultet":"Computer Science",
    "holat":"Gradueted"
    }

#1. items() metofini  ishlatamiz.
# items() - elementlar degan manoni bildiradi. Va bizni o'zgaruvchimizda bor elementlarni ko'rsatadi\
# for sikli orqali esa kalit sozni  va qiymatni chiroyli tartibta tartiblashimiz mumkin.
print(talaba_0.items())
for kalit,qiymat in talaba_0.items():
    print(f"Kalit: {kalit}")
    print(f"qiymat: {qiymat}\n")
    
