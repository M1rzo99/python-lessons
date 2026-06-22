#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:20:45 2026

@author: mirzo
"""

import Moduls # Moduls faylini chaqiramiz
avto1 = Moduls.avto_info("GYM", 'K5', "Oq", "avtomat", 2025,19000)
Moduls.info_print(avto1)

# MODULGA QISQA NOM BERISH
#Yuqoridagi usul bilan modulni chaqirib olishda fayl nomi uzun bo'lsa bu o'ziga yarasha noqulayliklar tug'dirishi mumkin. 
#Buning oldini olish uchun esa, modulni chaqirganda unga as operatori yordamida qisqa nom berishimiz, va modulga qisqa nom orqali murojat qilish mumkin. 
#Quyidagi misolda avto_info_mod ni qisqa qilib aim deb nomlab oldik, va 3-4-qatorlarda modulga murojat qilishda qisqa nomidan foydalandik.

import Moduls as aim # avto_info_mod ni qisqa nom aim bilan chaqiramiz

avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
aim.info_print(avto1)