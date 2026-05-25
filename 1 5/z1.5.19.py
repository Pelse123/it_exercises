def utworzmacierz(iloscwierszy,ilosckolumn):
    macierz = []
    for i in range(iloscwierszy):
        wiersz = []
        for j in range(ilosckolumn):
            wiersz.append(input())
        macierz.append(wiersz)
    return macierz


def transponowana(macierz):
    tmacierz = []
    for i in range(len(macierz[0])):
        wiersz = []
        for j in range(len(macierz)):
            wiersz.append(macierz[j][i])
        tmacierz.append(wiersz)
    return tmacierz

def czy_symetryczna(macierz,macierz2):
    tmacierz = []
    for i in range(len(macierz)):
        wiersz = []
        for j in range(len(macierz[i])):
            wiersz.append(macierz2[i][j])
        tmacierz.append(wiersz)

    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] != tmacierz[i][j]:
                return False
    return True

iloscwierszy = int(input())
ilosckolumn = int(input())
if iloscwierszy != ilosckolumn:
    print(False)
else:
    macierz = utworzmacierz(iloscwierszy,ilosckolumn)
    czy_prawda = czy_symetryczna(macierz,transponowana(macierz))
    print(czy_prawda)