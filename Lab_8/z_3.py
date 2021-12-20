"""
Визначити xn.
"""


def x_n(x):
    if x == 0:
        return 2
    elif x > 2:
        a = (7 * (x - 1) - (x - 2) * (x - 3))
        return a
    else:
        return 3


n = int(input("n = "))
print("x_n =", x_n(n))
print((7 * (4 - 1)) - (4 - 2) * (4 - 3))
