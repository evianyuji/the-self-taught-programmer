# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 12:22:47 2019

@author: yuji_n
"""

class Horse:
    def __init__(self, n, j):
        self.name = n
        self.jockey = j
        
class Rider:
    def __init__(self, n):
        self.name = n
        
rid = Rider("Take Yutaka")
hor = Horse("Oguicape", rid)
print(hor.name)
print(hor.jockey.name)