from functools import reduce
import random
"""
Дано текстовий файл, у якому міститься три одновимірних масиви по 10 елементів.
Визначити найбільший елемент кожного масиву.
"""
pum = 0
with open('f_1.txt') as file:
    line = file.readline()
    numbers = (map(lambda el: int(el), line.split(sep='[ ')))
    for i in numbers:
        pum += i
print(pum)
