# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 00:07:36 2019

@author: yuji_n
"""

import os
import csv

list = [["トップガン", "リスキー　ビジネス","マイノリティリポート"], ["タイタニック", "レヴェナント", "インセプション"], ["トレーニングデイ", "マン　オン　ファイア", "フライト"]]

print(os.getcwd())

with open(r"C:\Users\yuji_n\Desktop\python\st3.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    for i in range(3):
        w.writerow(list[i])