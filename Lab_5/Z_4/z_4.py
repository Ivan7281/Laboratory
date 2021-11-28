"""
Визначити x10
"""
x = 1
i = 1
for a in range(10):
    xi = x + 2 * i
    print('x{0} = {1}'.format(i, xi))
    i += 1
    x = xi
