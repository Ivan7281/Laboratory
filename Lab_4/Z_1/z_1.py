"""
Сума                float - s
Добуток             float - prod
Середнє арифметичне float - avg
Середнє геометричне float - geom
"""
a = float(input('Введіть перше число: '))
b = float(input('Введіть друге число: '))
s = a + b
prod = a * b
avg = (a + b) / 2
geom = (a * b) ** (1/2)
print('Сума = {0:.2f}, Добуток = {1:.2f}, Середнє арифметичне = {2:.2f}, '
      'Середнє геометричне = {3:.2f}'.format(s, prod, avg, geom))
