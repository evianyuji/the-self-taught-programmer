# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 23:21:53 2019

@author: yuji_n
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

app.run(port=8000)