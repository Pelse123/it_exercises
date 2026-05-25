def utworzmacierz(iloscwierszy,ilosckolumn):
    macierz = []
    for i in range(iloscwierszy):
        wiersz = []
        for j in range(ilosckolumn):
            wiersz.append(int(input()))
        macierz.append(wiersz)
    return macierz

def iloczyn(macierz1,macierz2,iw1,ik1,iw2,ik2):
    macierzwynikowa = []
    if ik1 == iw2:
        for i in range(iw1):
            wiersz = []
            for j in range(ik2):
                suma = 0
                for k in range(ik1):
                    suma = suma + macierz1[i][k]*macierz2[k][j]
                wiersz.append(suma)
            macierzwynikowa.append(wiersz)
        return macierzwynikowa
    else:
        return 0


def wypisz(macierz):
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            print(macierz[i][j],end=" ")
        print()

iloscwierszy1 = int(input())
ilosckolumn1 = int(input())
macierz1 = utworzmacierz(iloscwierszy1,ilosckolumn1)
iloscwierszy2 = int(input())
ilosckolumn2 = int(input())
macierz2 = utworzmacierz(iloscwierszy2,ilosckolumn2)
wypisz(iloczyn(macierz1,macierz2,iloscwierszy1,ilosckolumn1,iloscwierszy2,ilosckolumn2))
