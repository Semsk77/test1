A = float(input("Введите число A:"))
N = int(input("Введите число N:"))

if N > 0:
    total = 1.0
    power = 1.0
    for i in range(1, N + 1):
        power *= A
        total += power
        print(f" Сумма= {total}")
else:
    print("Ошибка: N должно быть больше 0")
    #18.09.2026 18:17