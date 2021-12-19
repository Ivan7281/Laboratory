import random
a = [[random.randint(0, 10) for j in range(2)]for i in range(2)]
diagonal_1 = 1
diagonal_2 = 1
n = len(a)
for i in range(n):
    diagonal_1 *= a[i][i]
    diagonal_2 *= a[i][n - (i + 1)]
determinant = diagonal_1 - diagonal_2
print(*a, sep="\n")
print("Детермінант: {0}".format(determinant))
