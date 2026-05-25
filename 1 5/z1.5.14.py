def utworzmacierz(iloscwierszy):
    macierz = []
    liczba = 1
    for i in range(iloscwierszy):
        wiersz = []
        for j in range(iloscwierszy):
            if(i==j):
                wiersz.append((j+1)**2)
            else:
                wiersz.append(0)
        macierz.append(wiersz)
    return macierz


def wypisz(macierz):
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            print(macierz[i][j], end=" ")
        print()

iloscwierszy = int(input())
macierz = utworzmacierz(iloscwierszy)
wypisz(macierz)
