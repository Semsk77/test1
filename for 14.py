N = int(input("сколько раз написать число:"))
if N > 0:
    t = 0.0
    for i in range(1, N + 1):
        t += 2 * i - 1
    print(t)
else:
    print("Ошибка")