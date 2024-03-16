#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 20:40:25 2022

@author: fatemehroohimaleki
"""


print ("----")
filled_dict={"one": 1, "two":2, "three":3 }

print(filled_dict)
k= filled_dict.keys()
v=filled_dict.values()

filled_dict["one"] = 100 #change valu
print(filled_dict)

print(k)
print(v)

filled_dict["four"] = 4 #adding
print(filled_dict)

filled_dict.pop("three")
print(filled_dict) # removing

for x in filled_dict:
    print(filled_dict[x])
