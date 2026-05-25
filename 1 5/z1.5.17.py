def tworz_macierz(ilosc_wierszy):
    macierz = []
    for i in range(ilosc_wierszy):
        wiersz = []
        for j in range(ilosc_wierszy):
                wiersz.append(int(input()))
        macierz.append(wiersz)
    return macierz

def labirynt(macierz):
    aktualne_j = 0
    for i in range (len(macierz)):
        for j in range (aktualne_j,len(macierz[i])):
            if macierz[i][j] == 0:
                aktualne_j = j
                print(i,j)
            if macierz[i][j] == 1 :
                break

def wypisz(macierz):
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            print(macierz[i][j], end=" ")
        print()

ilosc_wierszy = int(input())
while ilosc_wierszy <= 2 or ilosc_wierszy > 100:
    ilosc_wierszy = int(input())

macierz = tworz_macierz(ilosc_wierszy)

wypisz(macierz)
labirynt(macierz)

