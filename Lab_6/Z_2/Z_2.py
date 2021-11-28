z = float(input("z = "))
n = int(input("n = "))
x = float(input("x = "))
y = float(input("y = "))
ai = [x ** (i - 2) + x ** (i - 1) / 2 ** (i - 1) * y ** (i - 3) for i in range(4, n)]
a = [ai for ai in ai if ai > z]
print(a)
