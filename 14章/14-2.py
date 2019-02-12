# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 21:42:07 2019

@author: yuji_n
"""

class Square:
    def __init__(self, l):
        self.length = l
        
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.length, self.length, self.length, self.length)
    
print(Square(29))