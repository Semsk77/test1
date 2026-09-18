N = int(input("Введите число N: "))

if N > 0:
    product = 1.0
    for i in range(1, N + 1):
        product *= 1 + i / 10
    print(f"Произведение = {product}")
else:
    print("Ошибка: N должно быть больше 0")
    #18.09.2026 16:01