"""
Побудувати матрицю А, елементи якої задаються формулою
Побудувати одновимірний масив (переписати матрицю в одновимірний масив).
"""
def fac(x):
    if x == 0:
        return 1
    return fac(x-1) * x


def addi(x):
    if x == 0:
        return 1
    return addi(x-1) + x


n = int(input("Введіть кількість рядків матриці: "))
m = int(input("Введіть кількість стовпців матриці: "))
a = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if (i * j) % 2 == 0:
            a[i][j] = fac(j)
        else: a[i][j] = addi(i)
b = []
for i in range(len(a)):
    b += a[i]
print("Матриця:")
print(*a, sep="\n")
print(b)

