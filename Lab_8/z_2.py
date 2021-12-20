"""
Використовуючи підпрограму для знаходження n-тового числа Фібоначчі.
Обчислити значення виразу s = f(3) + f(8) , де f(i) – i-тове число Фібоначчі.
"""


def fibonacci(n):
    number_1 = number_2 = 1
    for i in range(2, n):
        number_1, number_2 = number_2, number_1 + number_2
    return number_2


print("s =", (fibonacci(3) + fibonacci(8)))
