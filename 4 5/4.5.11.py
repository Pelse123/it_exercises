def kolumnowy(napis,klucz):
    macierz = []
    indeks = 0
    for i in range(klucz):
        wiersz = []
        for j in range(klucz):
            if indeks<len(napis):
                wiersz.append(napis[indeks])
                indeks += 1
            else:
                wiersz.append("X")
        macierz.append(wiersz)
    return macierz

def odczytaj(macierz):
    for i in range(len(macierz)):
        for j in range(len(macierz)):
            print(macierz[j][i],end="")

napis = input()
klucz = int(input())
odczytaj(kolumnowy(napis,klucz))