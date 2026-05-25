

def utworzmacierz(iloscwierszy,ilosckolumn):
    macierz = []
    for i in range(iloscwierszy):
        wiersz = []
        for j in range(ilosckolumn):
                wiersz.append(int(input()))
        macierz.append(wiersz)
    return macierz

def dodaj_macierze(a,b):
    sumamacierzy=[]
    for i in range(len(a)):
        wiersz=[]
        for j in range(len(a[i])):
            wiersz.append(a[i][j]+b[i][j])
        sumamacierzy.append(wiersz)
    return wypisz(sumamacierzy)


def wypisz(macierz):
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            print(macierz[i][j], end=" ")
        print()

iloscwierszy = int(input())
ilosckolumn = int(input())
macierzA = utworzmacierz(iloscwierszy,ilosckolumn)
macierzB = utworzmacierz(iloscwierszy,ilosckolumn)
dodaj_macierze(macierzA,macierzB)
