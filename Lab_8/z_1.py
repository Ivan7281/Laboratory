"""
14.Обчислити значення виразу f(4) + 2 * f(a) - f(b)
де
"""


def fun(x):
    if x < 23:
        return 0
    elif x == 23:
        return 1
    else:
        return -1


a = float(input("a = "))
b = float(input("a = "))
print("Значення виразу:", (fun(4) + 2 * fun(a) - fun(b)))
