N = int(input("Введите число N:"))
if N > 0:
    t = 0
    for i in range(1, N + 1):
        t += i ** (N - i + 1)
    print(f"Сумма = {t}")
else:
    print("N < 0")
    #19.09.2026 13:58