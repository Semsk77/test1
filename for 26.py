import math
x = float(input("Введите число X:"))
N = int(input("Введите число N:"))

if N > 0 and abs(x) < 1:
    p = x
    t = 0
    s = 1
    for i in range(N + 1):
        if i > 0:
            p *= x * x
        t += s * p / (2 * i + 1)
        s = -s
else:
    print("0 == 0")
print(f"Приближённое значение arcth({x}) = {t}")
print(f"Точное значение math.arctg({x}) = {math.sin(x)}")
    #18.09.2026 19:25