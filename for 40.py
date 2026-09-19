A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A < B:
    c = 1
    for i in range(A, B + 1):
        for _ in range(c):
            print(i, end=" ")
        c += 1
    print()
else:
    print("A > B")
    #19.09.2026 14:20