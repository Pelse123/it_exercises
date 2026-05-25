def tworz_macierz(iloscwierszy,ilosckolumn,pierwszawartosc):
    macierz = []
    for i in range(iloscwierszy):
        wiersz = []
        for j in range(ilosckolumn):
            wiersz.append(pierwszawartosc)
            pierwszawartosc += 2
        macierz.append(wiersz)
    return macierz

def wyswietl_macierz(macierz):
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            print(macierz[i][j], end=" ")
        print()

iloscwierszy = int(input())
ilosckolumn = int(input())
pierwszawartosc = int(input())

wyswietl_macierz(tworz_macierz(iloscwierszy,ilosckolumn,pierwszawartosc))



