#!/usr/bin/python3
# Написати консольну програму, яка б сортувала текст поданий їй 
# з файлу на стандартний вхід за алфавітом. Програма повинна 
# ігнорувати регістр при сортуванні. Перевірити роботу для 
# англійської, української та російської мов.

import sys
import re
c = ''
if len(sys.argv) == 1:
    c = sys.stdin.read()
else:
    c= open(sys.argv[1]).read()


ukrA = u"абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
rusA = u"абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
rus = {i[1]: i[0] for i in enumerate(rusA)}
ukr = {i[1]: i[0] for i in enumerate(ukrA)}
b = list(c)

if 'ы' in b or 'э' in b or 'ъ' in b or 'ё' in b:
     c = re.sub('[^' + rusA + ']', '', c)
     b = list(c)
     b.sort(key=lambda x: rus[x.lower()])
elif 'і' in b or 'о' in b or 'а' in b or  'м' in b or 'ї' in b or 'є' in b or 'ґ' in b:
     c = re.sub('[^' + ukrA + ']', '', c)
     b = list(c)
     b.sort(key=lambda x: ukr[x.lower()])
else:
    b.sort(key = lambda x: x.lower())

print(''.join(b))