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

#