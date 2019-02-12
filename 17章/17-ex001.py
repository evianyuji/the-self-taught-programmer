# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 10:33:52 2019

@author: yuji_n
"""

import re #標準ライブラリの正規表現モジュール

l = "Beautiful is better than ugly."
matches = re.findall("Beautiful", l)

print(matches)

#大文字小文字の違いを無視する
matches2 = re.findall("beautiful", l, re.IGNORECASE)

print(matches2)