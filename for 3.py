A = int(input("введите число A:"))
B = int(input("введите число B:"))
if A < B:
    n = 0
    for i in range(B - 1, A, - 1):
        print(i, end=" ")
        n += 1
    print(". Кол-во чисел=", n)
else:
    print("Ошибка")
# 17.09.2026 23:23