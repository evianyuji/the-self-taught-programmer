# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 10:56:14 2019

@author: yuji_n
"""

import re

zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!"""

#文章の先頭がIfで始まる　MULTILINE:複数行のテキストを復習業として扱う
m = re.findall("^If", zen, re.MULTILINE)
print(m)

#文章の末尾がidea.で終わる
n = re.findall("idea.$", zen, re.MULTILINE)
print(n)