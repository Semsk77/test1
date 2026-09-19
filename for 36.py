N = int(input("Введите число N:"))
K = int(input("Введите число K:"))
if N > 0 and K > 0:
    t = 0
    for i in range(1, N + 1):
        t += i ** K
    print(f"Сумма = {t}")
else:
    print("N < 0 и K < 0")
    #19.09.2026 13:54