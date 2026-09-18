A = int(input("введите число A:"))
B = int(input("введите число B:"))
if A < B:
    n = 0
    for i in range(A, B + 1):
        print(i, end=" ")
        n = (B + 2) - A
    print(". Кол-во чисел=", n)
else:
    print("Ошибка")
# 17.09.2026 23:19