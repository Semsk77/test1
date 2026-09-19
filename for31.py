N = int(input("Введите число N(>1):"))

if N > 0:
    A = 2.0
    for k in range(1, N + 1):
        A = 2 + 1 / A
        print(f"A_{k} = {A}")
else:
    print("N < 0")
    #19.09.2026 00:50