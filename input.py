#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 20:37:03 2022

@author: fatemehroohimaleki
"""

price=float(input("enter the price of the itam more than 10"))
if price > 100:
    print("price is greater than 100")
elif price == 100:
    print("price is 100")
elif (price < 100) and (price > 10):
    print("price is less than 100 and more than 10")
else:
    print("invalid entry")
    