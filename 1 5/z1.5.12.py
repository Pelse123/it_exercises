def utworzmacierz(iloscwierszy):
    macierz = []
    for i in range(iloscwierszy):
        wiersz = []
        for j in range(iloscwierszy):
            wiersz.append(int(input()))
        macierz.append(wiersz)
    return macierz

def kopiujmacierz(macierz):
    nowamacierz=[]
    for i in range(len(macierz)):
        wiersz = []
        for j in range(len(macierz[i])):
            wiersz.append(macierz[i][j])
        nowamacierz.append(wiersz)
    return nowamacierz

def odwrocmacierz(macierz,nowamacierz):
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            nowamacierz[j][len(macierz)-i-1] = macierz[i][j]
    return nowamacierz

def wypisz(macierz):
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            print(macierz[i][j], end=" ")
        print()

iloscwierszy = int(input())
macierz = utworzmacierz(iloscwierszy)
nowamacierz = kopiujmacierz(macierz)

macierz90 = odwrocmacierz(macierz,nowamacierz)
macierz180 =kopiujmacierz(macierz90)

macierz180 = odwrocmacierz(macierz90,macierz180)
macierz270 = kopiujmacierz(macierz180)

wypisz(odwrocmacierz(macierz180,macierz270))