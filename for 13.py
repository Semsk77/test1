N = int(input("Введите число N: "))

if N > 0:
    total = 0.0
    sigh = 1
    for i in range(1, N + 1):
        total += sigh * (1 + i / 10)
        sigh = -sigh
    print(f"Значение выражения = {total}")
else:
    print("Ошибка: N должно быть больше 0")
    #18.09.2026 16:04