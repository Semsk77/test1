import math
x = float(input("Введите число X:"))
N = int(input("Введите число N:"))

if N > 0:
    p = x
    t = 0
    f = 1
    s = 1
    for i in range(N + 1):
        if i > 0:
            p *= x * x
            f *= (2 * i) * (2 * i + 1)
        t += s * p / f
        s = -s
else:
    print("0 == 0")
print(f"Приближённое значение sin({x}) = {t}")
print(f"Точное значение math.sin({x}) = {math.sin(x)}")
    #18.09.2026 19:23