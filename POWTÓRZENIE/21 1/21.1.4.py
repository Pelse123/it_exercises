def czy_pierwsza(liczba):
    if liczba<2:
        return False
    for i in range(2,int(liczba**0.5)+1):
        if liczba%i==0:
            return False
    return True

def wyswietl_macierz(macierz):
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            print(macierz[i][j],end=" ")
        print()

liczba_wierszy = int(input())
liczba_kolumn = int(input())
macierz =[]
for i in range(liczba_wierszy):
    wiersz = []
    for j in range(liczba_kolumn):
        liczba = int(input())
        if czy_pierwsza(liczba):
            wiersz.append(0)
        else:
            wiersz.append(liczba)
    macierz.append(wiersz)


odwrocona_macierz = []
for i in range(liczba_kolumn):
    wiersz =[]
    for j in range(liczba_wierszy-1,-1,-1):
        wiersz.append(macierz[j][i])
    odwrocona_macierz.append(wiersz)


wyswietl_macierz(odwrocona_macierz)
