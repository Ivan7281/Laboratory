import random
""" Кількість чисел int - n """
n = int(input("n = "))
a = [random.randint(0, 999) for i in range(n)]
print(a)
b = sorted(a)
print(b)
