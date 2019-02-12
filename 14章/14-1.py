# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 21:34:11 2019

@author: yuji_n
"""

class Square:
    squares = []    #クラス変数
    
    def __init__(self, l):
        self.length = l
        self.squares.append((self.length, self.length)) #呼び出されるたびにクラス変数に追加
        
squ1 = Square(3)
squ2 = Square(7)
print(Square.squares)