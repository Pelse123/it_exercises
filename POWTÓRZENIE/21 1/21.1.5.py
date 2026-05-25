def wyswietl_macierz(macierz):
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            print(macierz[i][j],end=" ")
        print()

def czy_symetryczna(macierz):
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] != macierz[j][i]:
                return False
    return True

wielkosc = int(input())

macierz = []
for i in range(wielkosc):
    wiersz =[]
    for j in range(wielkosc):
        wiersz.append(int(input()))
    macierz.append(wiersz)

if czy_symetryczna(macierz):
    print("Symetryczna")
else:
    print("Niesymetryczna")