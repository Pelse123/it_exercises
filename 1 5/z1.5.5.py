def utworzmacierz(ilosckolumn,iloscwierszy):
    macierz = []
    for i in range(iloscwierszy):
        wiersz = []
        for j in range(ilosckolumn):
            wiersz.append(int(input()))
        macierz.append(wiersz)
    return macierz

def sumywierszy(macierz):
    sumy = []
    for i in range(len(macierz)):
        sumawiersza = 0
        for j in range(len(macierz[i])):
            sumawiersza += macierz[i][j]
        sumy.append(sumawiersza)
    for i in range(len(sumy)):
        print(sumy[i])


iloscwierszy = int(input())
ilosckolumn = int(input())
macierz = utworzmacierz(ilosckolumn,iloscwierszy)
sumywierszy(macierz)
