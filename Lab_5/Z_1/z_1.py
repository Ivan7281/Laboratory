a = float(input('a = '))
n = int(input('n = '))
i = 1
s = 1
while i <= n:
    s *= a*(a + i)
    i += 1
else:
    s *= a + n - 1
print('s =', s)
