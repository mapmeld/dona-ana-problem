# script-p3.py
# run in Python3

import json

fdata = open('counties.csv', 'r').read().split(',')

print(fdata)

fout = open('county-out-3.csv', 'w')
fout.write(json.dumps(fdata, ensure_ascii=False))

in_code_string = "Doña Ana"
print(in_code_string)

tree_kanji = u"\u6728"
print(tree_kanji)

émoji = "😭"
print(émoji)
# 😭  = "emoji good"
