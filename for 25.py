import math

N = int(input("Введите число N:"))

if N > 0:
    t = 1
    f = 1
    for i in range(2, N + 1):
        f *= i
        t += 1 / f
else:
    print("0 == 0")
print(f"Приближённое значение e = {t}")
print(f"Точное значение math.e = {math.e}")
    #18.09.2026 19:02