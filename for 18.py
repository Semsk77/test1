A = float(input("Введите число A:"))
N = int(input("Введите число N:"))

if N > 0:
    total = 1.0
    power = 1.0
    sigh = -1
    for i in range(1, N + 1):
        power *= A
        total += power
        sigh = -sigh
        print(f" Значение выражения= {total}")
else:
    print("Ошибка: N должно быть больше 0")
    #18.09.2026 18:25