def tworz_macierz(ilosckolumn,iloscwierszy):
    macierz = []
    for i in range(iloscwierszy):
        wiersz = []
        for j in range(ilosckolumn):
            wiersz.append(int(input()))
        macierz.append(wiersz)
    return macierz

def znajdz_min_max(macierz):
    minimum = macierz[0][0]
    maksimum = 0
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] < minimum:
                minimum = macierz[i][j]
            if macierz[i][j] > maksimum:
                maksimum = macierz[i][j]
    print(f"Min: {minimum}")
    print(f"Max: {maksimum}")

iloscwierszy = int(input())
ilosckolumn = int(input())
macierz1 = tworz_macierz(ilosckolumn,iloscwierszy)
znajdz_min_max(macierz1)