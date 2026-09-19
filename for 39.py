A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A < B and A > 0:
    for i in range(A, B + 1):
        for _ in range(i):
            print(i, end=" ")
        print()
else:
    print("A < 0 или A < B")
    #19.09.2026 14:20