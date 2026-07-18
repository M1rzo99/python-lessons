#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 20:14:33 2026

@author: mirzo
"""

# Amaliyot #30-dars
#1.Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])

class Talaba:
    def __init__(self,ism,fam,yosh,kasbi):
        self.ism=ism
        self.fam=fam
        self.yosh=yosh
        self.kasbi=kasbi
        self.fanlar=[]
        
    def fan_qosh(self,fan):
        return self.fanlar.append(fan)

    def get_info(self):
        info = f"{self.ism} {self.fam}, "
        info += f"{self.yosh} yoshda va {self.kasbi}. "
        info += f"Quyidagi fanlarni yoqtiradi: {', '.join(self.fanlar)}"
        return info
    
t1=Talaba("Mirzo", "SHomuratov", 27, "Student")

t1.fan_qosh("Python")
t1.fan_qosh("Java Script")
print(t1.get_info())