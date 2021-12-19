import random
n = int(input("Введіть кількість рядків матриці: "))
m = int(input("Введіть кількість стовпців матриці: "))
a = [[random.randint(0, 5) for j in range(m)]for i in range(n)]
no_zero = 0
zero = 0
for i in range(n):
    if a[i] != [0]*m:
        row = a[i]
        zero = 0
        for el in row:
            if el != 0:
                zero += 1
                if zero == m:
                    no_zero += 1
print(*a, sep="\n")
print("Рядки, які не містять жодного нульового елемента:", no_zero)
