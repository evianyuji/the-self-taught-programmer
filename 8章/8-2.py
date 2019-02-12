# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 14:08:43 2019

@author: yuji_n
"""

import cubed

val = input("数値を入力してください。3乗した値を返します：")
try:
    val = int(val)
    print(str(val) +"を3乗した値は、" + str(cubed.cube(val)) + "です。")
except:
    print("数値を入力してください")
    