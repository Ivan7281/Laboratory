import random
n = int(input("Введіть кількість рядків матриці: "))
m = int(input("Введіть кількість стовпців матриці: "))
a = [[random.randint(-10, 10) for j in range(m)]for i in range(n)]
negativ_sum = 0
for i in range(n):
    for j in range(m):
        if i != 0 and j != 0 and a[i][j] < 0 and i % 2 == 0 and j % 2 == 0:
            negativ_sum += a[i][j]
print(*a, sep="\n")
print("Сума від’ємних елементів: {0}".format(negativ_sum))
