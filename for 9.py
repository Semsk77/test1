A = int(input("введите число A:"))
B = int(input("введите число B:"))
if A < B:
    t = 0
    for i in range(A, B + 1):
        t += i ** 2
    print(f"Сумма чисел от {A} до {B} =", t)
else:
    print("Ошибка")
# 18.09.2026 14:41