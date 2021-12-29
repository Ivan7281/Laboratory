"""
Дано два вектори x, y є R**n . Знайти суму векторів.
"""
sum_vectors = 0
x = []
y = []
n = int(input("Кількість векторів: "))
for i in range(n):
    x.append(float(input("x = ")))
    y.append(float(input("y = ")))
    sum_vectors += x[i] + y[i]
print("Сума векторів: {0:.2f}".format(sum_vectors))
