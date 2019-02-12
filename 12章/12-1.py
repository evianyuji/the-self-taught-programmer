# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 20:38:44 2019

@author: yuji_n
"""
class Apple:
    def __init__(self, w, c, p):
        self.weight = w
        self.color = c
        self.produced = p
        self.mold = 0
        
apple = Apple(200, "red", "aomori")
print(apple.weight)
print(apple.color)
print(apple.produced)