#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 17:06:52 2026

@author: abcd
"""

#1.  Bugun o'rgangan narsalaringizni matnga yozing va matnni Python yordamida oching
with open("amaliyot.txt") as file:
    info = file.read()
print(info)