# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 22:30:56 2019

@author: yuji_n
"""

class Hexagon:
    def __init__(self, l):
        self.length = l
        
    def caluculate_perimeter(self):
        return self.length * 6
    
hexagon = Hexagon(3)
print(hexagon.caluculate_perimeter())