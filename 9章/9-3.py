# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 23:58:27 2019

@author: yuji_n
"""
import os
import csv

list = [["Top Gun", "Risky Business","Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man On Fire", "Flight"]]

print(os.getcwd())

with open(r"C:\Users\yuji_n\Desktop\python\st2.csv", "w", newline='') as f:
    w = csv.writer(f, delimiter=",")
    for i in range(3):
        w.writerow(list[i])