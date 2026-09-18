N = int(input("сколько раз написать число:"))
if N > 0:
    t = 0.0
    for i in range(N, 2 * N + 1):
        t += i ** 2
    print("Сумма =", t)
else:
    print("Ошибка")
    #18.09.2026 15:50