#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 21:31:12 2022

@author: fatemehroohimaleki
"""

lst1 = []
lst2 = ["programming" , "english" , "mathematics" , 2018 , 3.14 ]
lst3 = [1,2,3,4,5,3,2,1]
lst4 = ["centennail" , "college"]
print(lst2[1])

print(lst3)

print(lst2[-2])

print("---")
motorcyles=["honda","yamaha", "suzuki"]
print(motorcyles)
#change th evalue of this first item
motorcyles[0]="ducati"
print(motorcyles)

motorcyles.append("BMW")
print(motorcyles)

#append( method makes it easy to build lists dynamically)
motorcyles= []
motorcyles.append("honda")
motorcyles.append("yamaha")
motorcyles.append("suzuki")

print("----1")
motorcyles=["honda","yamaha", "suzuki"]
motorcyles.insert(0,"ducati")
print(motorcyles)
print("----2")
print(len(motorcyles))
del motorcyles[3]
print(motorcyles)

print("----3")
print(motorcyles[:2])
print(motorcyles[2:])

print("----4")
### other function
number = [14, 13, 17, 55, 2]
number.sort()
print(number)
number.reverse()
print(number)
##remove all elements
number.clear()
print(number)
print("----5")

number= [14,13,17,55,2]
number1= [12,44]
number1=number.copy()
print(number1)
print("----6")

##remover the element at index 2
newlist= number.pop(2)
print("removed elements :", newlist)
print("updated list:", number)
number.insert(0,23)
print(number)

number.extend(number1)
print(number)

countNum= number.count(55)
print(countNum)


