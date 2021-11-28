import math
x = float(input('x = '))
n = int(input('n = '))
ln = math.log(x)
i = 0
s = 0
for a in range(n):
    s += (1 / 2 * i - 1) * ((x - 1 / x + 1) ** (2 * i - 1))
    i += 1
else:
    s += 1
if ln == s:
    print('{0:.1f} = {1:.1f}'.format(ln, s))
else:
    print('{0:.1f} != {1:.1f}'.format(ln, s))