N = int(input("Введите число N:"))

if N > 0:
    f = 1
    for i in range(2, N + 1):
        f *= i
else:
    print("0 == 0")
print(f"{N}! = {f}")
    #18.09.2026 18:50