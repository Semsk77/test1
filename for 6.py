pr = int(input("введите сумму за 1 кг конфет:"))
for i in range(6, 11):
    w = i / 5
    print(f"{w:.1f} кг стоит {pr * w:.2f}")
    #17.09.2026 23:35