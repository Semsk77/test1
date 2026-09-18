import math
x = float(input("Введите число X:"))
N = int(input("Введите число N:"))

if N > 0:
    s = 1
    t = 1
    f = 1
    for i in range(2, N + 1):
        s *= x
        f *= i
        t += s / f
else:
    print("0 == 0")
print(f"Приближённое значение exp({x}) = {t}")
print(f"Точное значение math.exp({x}) = {math.exp(x)}")
    #18.09.2026 19:13