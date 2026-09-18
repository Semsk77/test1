pr = int(input("введите сумму за 1 кг конфет:"))
for i in range(1, 11):
    w = i / 10
    print(f"{w:.1f} кг стоит {pr * w:.2f}")
    #17.09.2026 23:34