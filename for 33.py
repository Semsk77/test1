N = int(input("Введите число N:"))

if N > 1:
    f1 = 1
    f2 = 1
    print(f1, f2, end=" ")
    for k in range(3, N + 1):
        f3 = f1 + f2
        print(f3, end=" ")
        f1, f2 = f2, f3
    print()
else:
    print("N < 1")
    #19.09.2026 13:35