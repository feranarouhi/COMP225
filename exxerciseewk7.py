#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 20:55:32 2022

@author: fatemehroohimaleki
"""

favorite_languages = {'jen':'HTML', 'sarah':'c', 'edward':'ruby', 'phil':'C#' , 'lab key': 550}
print(favorite_languages)

favorite_languages['phil'] = "PYTHON"
print(favorite_languages)

favorite_languages["ferana"] = "Java"
print(favorite_languages)

favorite_languages.pop('jen')
print(favorite_languages)

print('-----')

for x in favorite_languages:
    print(favorite_languages)