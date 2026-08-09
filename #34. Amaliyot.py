#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 14:14:13 2026

@author: mirzo
"""
import json
#1.Ushbu o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini konsolga chiqaring:
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json = json.dumps(data,indent = 2)
print(data_json)
