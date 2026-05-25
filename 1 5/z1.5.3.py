def utworzmacierzy(iloscwierszy,ilosckolumn):
    macierz = []
    for i in range(iloscwierszy):
        wiersz = []
        for j in range(ilosckolumn):
            wiersz.append(int(input()))
        macierz.append(wiersz)
    return macierz

def iloczyn7(macierz):
    iloczyn = 1
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j]%7 == 0:
                iloczyn = iloczyn *macierz[i][j]
    return iloczyn

iloscwierszy = int(input())
ilosckolumn = int(input())
macierz = utworzmacierzy(iloscwierszy,ilosckolumn)
print(iloczyn7(macierz))