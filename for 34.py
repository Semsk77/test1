N = int(input("Введите число N:"))

if N > 1:
    A1 = 1
    A2 = 2
    print(A1, A2, end=" ")
    for k in range(3, N + 1):
        A3 = (A1 + 2 * A2) / 3
        print(A3, end=" ")
        A1, A2 = A2, A3
    print()
else:
    print("N < 1")
    #19.09.2026 13:38