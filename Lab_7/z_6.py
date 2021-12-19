import random
n = int(input("Введіть кількість рядків матриці: "))
m = int(input("Введіть кількість стовпців матриці: "))
a = [[random.randint(0, 9) for j in range(m)]for i in range(n)]
max_a = a[0][0]
max_b = []
d = 0
for i in range(n):
    for j in range(m):
        if a[i][j] >= max_a:
            max_a = a[i][j]
            d = 0
            for row in a:
                for el in row:
                    if max_a == el:
                        d += 1
                        if d >= 2:
                            max_b = max_a
print(*a, sep="\n")
print("Максимальний елемент, який зустрічається більше одного разу:", max_b)

