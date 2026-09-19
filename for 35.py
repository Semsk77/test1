N = int(input("Введите число N(> 2):"))

if N > 2:
    A1 = 1
    A2 = 2
    A3 = 3
    print(A1, A2, A3, end=" ")
    for k in range(4, N + 1):
        A4 = A3 + A2 - 2 * A1
        print(A4, end=" ")
        A1, A2, A3 = A2, A3, A4
    print()
else:
    print("N < 2")
    #19.09.2026 13:41