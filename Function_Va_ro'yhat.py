# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Mon Jun  1 23:00:06 2026

# @author: mirzo
# """

# Funksiyaga ro'yhat uzatish

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

talabalar = ['ali','vali','hasan','husan']
baholar = bahola(talabalar)
print(baholar)

# Ro'yhatga o'zgartirish kiritish
# pop() - yordamida ro'yhatdan har bir elementni sug'urib ola bilamiz.
#Yuqoridagi funksiya unga uzatilgan ro'yxat ichidagi talabalarning ismini 
#.pop() yordamida sug'urib olgani uchun bizning asl ro'yxatimiz ham bo'shab qoldi. 
# E'tibor bering, funksiya tashqarisidagi va ichidagi ro'yxatlar ikki hil nomlangan bo'lsada (talabalar va ismlar), ikkalasi ham xotiradagi bitta ro'yxatga bog'langani sabab ulardan biriga o'zgartirish kiritilishi bilan, ikkinchisi ham o'zgaradi. 
