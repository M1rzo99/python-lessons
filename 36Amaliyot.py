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
