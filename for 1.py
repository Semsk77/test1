K = int(input("введите число:"))
N = int(input("сколько раз написать число:"))
if N < 0:
    print("Введите положительное число")
for i in range(N):
    print(K)