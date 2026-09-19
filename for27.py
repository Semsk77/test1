import math
x = float(input("Введите число X:"))
N = int(input("Введите число N:"))
if N > 0 and abs(x) < 1:
    total = x
    term = x
    for i in range(1, N + 1):
        if i > 0:
            term *= (2 * i - 1) * x * x / ((2 * i) * (2 * i + 1))
            total += term
    print(f"Приближённое значение arcsin({x}) = {total}")
    print(f"Точное значение math.asin({x}) = {math.asin(x)}")
else:
    print("0 == 0")
    #18.09.2026 23:03