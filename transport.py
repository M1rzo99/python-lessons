#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:59:35 2026

@author: mirzo
"""
from uuid import uuid4 # randaom ID yaratib beradi,xar safar.Har bir foydalanuvchiga
class Avto:
    """Avtomabil klassi"""
    def __init__(self,make,model,rang,yil,narx,km=0):
        """Avtomobilning xususiyatlari"""
        self.make= make
        self.model = model
        self.rang=rang
        self.yil=yil
        self.narx=narx
        self.__km = km # inkapsulyatsiya - xususiyatni hech kim ko'ra olmaydi va o'zgartira olmaydi,oddiy yo'l bilan
        self.__id = uuid4() # inkapsulyatsiya
        
    def get_km(self):
        return self.__km #inkapsulyatsiya - bu orqali ko'ra oaldi kmni 

    def get_id(self):
        return self.__id
    
#Bunday yopiq xususiyatlarni o'zgartirsh ham methodlar orqali amalga oshirilioshi kerak.Misol un mashinaning necha km yurganini o'zgartirish un klassimizga quyidagi methodni qo'shamiz:
    def add_km(self,km):
        """Mashinaning km siga yana km qo'shamiz"""
        if km>=0:
            self.__km +=km
        else:
            print("Mashinaning km sini kamaytirib bo'lmaydi!")