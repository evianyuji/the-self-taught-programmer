# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:58:23 2019

@author: yuji_n
"""

class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h
        
    def area(self):
        return self.base * self.height / 2
    
try:
    b = int(input("底辺の長さを入力してください："))
except:
    print("整数値で入力してください")
    exit
try:
    h = int(input("高さを入力してください："))
except:
    print("整数値で入力してください")
    
triangle = Triangle(b, h)
print(triangle.area())