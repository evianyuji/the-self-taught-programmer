# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 21:50:52 2019

@author: yuji_n
"""

import re

string = "The ghost that says boo haunts the loo"
m = re.findall(".oo", string)
print(m)