# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:45:33 2019

@author: yuji_n
"""
import math

class Circle:
    def __init__(self, r):
        self.radius = r
        
    def area(self):
        return self.radius * self.radius * math.pi
    
r = int(input("円の半径を入力してください："))
circle = Circle(r)
area = circle.area()
print(area)