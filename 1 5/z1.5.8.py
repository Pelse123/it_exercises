def tworz_macierz(ilosc_kolumn,ilosc_wierszy):
    macierz = []
    for i in range(ilosc_wierszy):
        wiersz = []
        for j in range(ilosc_kolumn):
            wiersz.append(int(input()))
        macierz.append(wiersz)
    return macierz

def znajdz_liczbe_pierwsza(liczba):
    if liczba<2:
        return False
    for i in range(2,liczba):
        if(liczba%i==0):
            return False
    return True

def iteruj(macierz):
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if(znajdz_liczbe_pierwsza(macierz[i][j])):
                print(macierz[i][j])

ilosc_wierszy = int(input())
ilosc_kolumn = int(input())
macierz = tworz_macierz(ilosc_kolumn,ilosc_wierszy)
iteruj(macierz)