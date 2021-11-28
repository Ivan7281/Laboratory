n = int(input('n = '))
d = 0
while n > 0:
    n //= 10
    d += 1
print(d)
