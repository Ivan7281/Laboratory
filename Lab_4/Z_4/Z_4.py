# Знайти значення z
import math
x = float(input("Введіть x: "))
n = float(input("Введіть n: "))
if n == 10:
    z = math.sin(x) ** n
elif n == 22:
    z = x ** n
elif n == 3:
    z = n ** x
else:
    z = 1
print("z = {0:.2f}".format(z))
