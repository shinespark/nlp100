# -*- coding: UTF-8 -*-

str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
only_initial = [1, 5, 6, 7, 8, 9, 15, 16, 19]
periodic_table = {}

for i, word in enumerate(str.split()):
    num = i + 1
    if num in only_initial:
        periodic_table[word[:1]] = num
    else:
        periodic_table[word[:2]] = num

print(periodic_table)
print(sorted(periodic_table.items(), key=lambda x:x[1]))

