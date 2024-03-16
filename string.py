#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 20:37:38 2022

@author: fatemehroohimaleki
"""

print("This is a string message")
print("python's flexibillity is amazing")
print("the language 'python' is named after monty python, not the snake")

a='first line'\
    "second line" \
        "third line"
        
print("-------another way-------")

a= '''first line

second line
third line'''
print(a)


#using variables is strings
#f-strings are strng literals that have an
#f at the beginning and curly braces containing
#expressions that will be replace with their values.

print("-------another way-------")

college_name= "centennial"
campus_name= "progress"
full_detail=f"{college_name} {campus_name}"
print(full_detail)
print('college name is', college_name,", campus is",
      full_detail)