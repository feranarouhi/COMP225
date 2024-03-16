#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:01:14 2022

@author: fatemehroohimaleki
"""
'''create a list of aligne software .insert the value , 
delete one item from the list . use slicing and display the list of
software's
'''

list=["red" , "purple", "blue"]
list.insert(1, "green")
print(list)

del list[0]
print(list)

print(list[1:])
print(list[:1])


'''start with the list by printing three course's name like comp100,comp120,comp213.
print a message sating trhat you are enrooled in the
the text of each message shoulkd be same , buyt each message should be personalized 
with the co