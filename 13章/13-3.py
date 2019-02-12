# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 12:01:38 2019

@author: yuji_n
"""
import math

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.length = l
    
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l
        
    def calculate_perimeter(self):
        return (self.width + self.length) * 2
    
    def change_size(self, l):
        self.length += l
    
class Square(Shape):
    def __init__(self, r):
        self.radius = r
        
    def calculate_perimeter(self):
        return self.radius ** 2 * math.pi
    
    def change_size(self, r):
        self.radius += r
    
rec = Rectangle(5, 10)
print(rec.calculate_perimeter())
rec.change_size(4)
print(rec.calculate_perimeter())
rec.change_size(-1)
print(rec.calculate_perimeter())

squ = Square(6)
print(squ.calculate_perimeter())
squ.change_size(4)
print(squ.calculate_perimeter())
squ.change_size(-2)
print(squ.calculate_perimeter())

rec.what_am_i()
squ.what_am_i()