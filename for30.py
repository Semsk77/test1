import math
N = int(input("Введите число N(>1):"))
A = int(input("Введите число A:"))
B = int(input("Введите число B:"))
if N > 1 and A < B:
    H = (B - A) / N
    print(f"Длина каждого отрезка H = {H}")
    for i in range(N + 1):
        x = A + i * H
        fx =1 - math.sin(x)
        print(f"F({x:.4f}) = {fx:.4f}")
else:
    print("N > 1 и A < B")
    #19.09.2026 00:38