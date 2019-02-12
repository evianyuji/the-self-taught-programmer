# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 23:50:55 2019

@author: yuji_n
"""

str = input("あなたの名前は？：")

st = open(r"C:\Users\yuji_n\Desktop\python\st2.txt", "w", encoding="utf-8")
st.write(str)
st.close()