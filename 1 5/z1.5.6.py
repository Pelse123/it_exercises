def utworzmacierz(ilosckolumn,iloscwierszy):
    macierz = []
    for i in range(iloscwierszy):
        wiersz = []
        for j in range(ilosckolumn):
            wiersz.append(int(input()))
        macierz.append(wiersz)
    return macierz

def sumykolumn(macierz):
    sumy = []
    for i in range(len(macierz[0])):
        sumakolumny = 0
        for j in range(len(macierz)):
            sumakolumny += macierz[j][i]
        sumy.append(sumakolumny)
    for i in range(len(sumy)):
        print(sumy[i])

iloscwierszy = int(input())
ilosckolumn = int(input())
macierz = utworzmacierz(ilosckolumn,iloscwierszy)
sumykolumn(macierz)