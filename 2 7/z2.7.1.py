try:
    liczba = int(input("Podaj liczbę: "))
    if liczba < 0:
        raise ValueError("Podano ujemną liczbę")
    else:
        pierwiastek = liczba ** (1 / 2)
        print("Wynik pierwiastka", pierwiastek)
except ValueError as e:
    print(e)


