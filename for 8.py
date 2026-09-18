A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A < B:
    product = 1
    for i in range(A, B + 1):
        product *= i
    print(f"Произведение чисел от {A} до {B} = {product}")
else:
    print("Ошибка: должно быть A < B")
# 18.09.2026 14:39