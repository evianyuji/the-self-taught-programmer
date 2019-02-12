# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 22:37:31 2019

@author: yuji_n
"""

class Person:
    def __init__(self, h, w):
        self.height = h
        self.weight = w
        
class Dog:
    def __init__(self, n, o):
        self.name = n
        self.owner = o
        
def instanceCheck(a, b):
    return a is b

per = Person(190, 80)
same_per = per
print(instanceCheck(per, same_per))
print(instanceCheck(Person(175, 65), Dog("poti", "ryoma")))
