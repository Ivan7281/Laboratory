import math
x = float(input('x = '))
if x <= 0:
    print("НЕПРАВИЛЬНЕ ЗНАЧЕННЯ!")
ln = math.log(x)
n = 1
s = 2 + ((x - 1)/(x + 1)) + (1/3 * ((x - 1)/(x + 1)) ** 3)
epsilon = float(input("Задайте епсілон: "))
while True:
    if s > epsilon:
        if s == ln:
            print("{0} == {1}".format(s, ln))
            break
        else:
            print("{0} != {1}".format(s, ln))
            break
    s += (1 / ((2 * n) - 1)) * ((x - 1)/(x + 1)) ** ((2 * n) - 1)
    n += 1
print(ln)
print(s)
