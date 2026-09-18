import math
x = float(input("Введите число X:"))
N = int(input("Введите число N:"))

if N > 0:
    p = 1
    t = 1
    f = 1
    s = 1
    for i in range(N + 1):
        if i > 0:
            p *= x * x
            f *= (2 * i - 1) * (2 * i)
        t += s * p / f
        s = -s
else:
    print("0 == 0")
print(f"Приближённое значение cos({x}) = {t}")
print(f"Точное значение math.cos({x}) = {math.sin(x)}")
    #18.09.2026 19:25