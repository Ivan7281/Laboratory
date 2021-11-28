import random
""" 
Кількість чисел    n
Сума               s
Середнє арфметичне avg
"""
n = int(input("n = "))
a = {random.randint(0, 999) for i in range(n)}
s = sum(a)
avg = s / n
print("s = {0}, avg = {1:.2f}".format(s, avg))
