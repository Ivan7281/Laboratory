import random
n = int(input("n = "))
a = [[random.randint(0, 10) for j in range(n)]for i in range(n)]
print(*a, sep="\n")
print("Матриця: ")
max_a = []
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            a[i].sort()
print(*a, sep="\n")



