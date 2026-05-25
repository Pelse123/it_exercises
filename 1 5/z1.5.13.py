def utworzmacierz(iloscwierszy,ilosckolumn):
    macierz = []
    for i in range(iloscwierszy):
        wiersz = []
        for j in range(ilosckolumn):
            wiersz.append(input())
        macierz.append(wiersz)
    return macierz

def wypisz(macierz):
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            print(macierz[i][j], end=" ")
        print()
"""
def transponowana(macierz):
    tmacierz = []
    for i in range(len(macierz[0])):
        wiersz = []
        for j in range(len(macierz)):
            wiersz.append(macierz[j][i])
        tmacierz.append(wiersz)
    return tmacierz
"""
def transponowana(macierz,iloscwierszy,ilosckolumn):
    tmacierz = []
    for i in range(ilosckolumn):
        wiersz = []
        for j in range(iloscwierszy):
            wiersz.append(macierz[j][i])
        tmacierz.append(wiersz)
    return tmacierz
iloscwierszy = int(input())
ilosckolumn = int(input())
macierz = utworzmacierz(iloscwierszy,ilosckolumn)
wypisz(transponowana(macierz,iloscwierszy,ilosckolumn))