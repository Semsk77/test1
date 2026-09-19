import math
x = float(input("Введите число X:"))
N = int(input("Введите число N:"))
if N > 0 and abs(x) < 1:
    tt = x
    tr = x
    for k in range(1, N + 1):
        if k == 1:
            tr *= x / 2
        else:
            tr *= -(2 * k - 3) * x / (2*k)
        tt += tr
    print(f"Приближённое значение sqrt(1+{x}) = {tt}")
    print(f"Точное значение math.sqrt(1+{x}) = {math.sqrt(1 + x)}")
else:
    print("0 == 0")
    #19.09.2026 00:21