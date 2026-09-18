A = float(input("Введите число A:"))
N = int(input("Введите число N:"))

if N > 0:
    power = 1.0
    for i in range(N):
        power *= A
        print(f"{A} степени {N} = {power}")
else:
    print("Ошибка: N должно быть больше 0")
    #18.09.2026 18:09