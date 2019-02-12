# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 11:04:17 2019

@author: yuji_n
"""
import re

#複数文字との一致
#例：tで始まり、oかｗがあり、oで終わるものが引っ掛かる
string = "Two too."
m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)

#数字との一致
line = "123 hi 34 hello."
n = re.findall("\d", line, re.IGNORECASE)
print(n)

t = "__one__ __two__ __three__"

#貪欲な正規表現
found = re.findall("__.*__", t)
print(found)

#非貪欲な正規表現
found2 = re.findall("__.*?__", t)
print(found2)

#エスケープ
line2 = "I love $"
m2 = re.findall("\\$", line2, re.IGNORECASE)
print(m2)