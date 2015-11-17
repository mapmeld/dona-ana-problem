# script-p2.py
# -*- coding: utf-8 -*-
# run in Python2

import json

fdata = open('counties.csv', 'r').read().split(',')

print(fdata)

fout = open('county-out.csv', 'w')
fout.write(json.dumps(fdata, ensure_ascii=False))

in_code_string = u"Doña Ana"
print(in_code_string)

tree_kanji = u"\u6728"
print(tree_kanji)

emoji = "😭"
print(emoji)
