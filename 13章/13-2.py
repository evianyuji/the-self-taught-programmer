# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 12:01:38 2019

@author: yuji_n
"""
import math

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.length = l
        
    def calculate_perimeter(self):
        return (self.width + self.length) * 2
    
    def change_size(self, l):
        self.length += l
    
class Square:
    def __init__(self, r):
        self.radius = r
        
    def calculate_perimeter(self):
        return self.radius ** 2 * math.pi
    
    def change_size(self, r):
        self.radius += r
    
rec = Rectangle(5, 10)
print(rec.calculate_perimeter())
rec.change_size(4)
print(rec.length)
rec.change_size(-1)
print(rec.length)

squ = Square(6)
print(squ.calculate_perimeter())
squ.change_size(4)
print(squ.radius)
squ.change_size(-2)
print(squ.radius)