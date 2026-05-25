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

def odczytaj_odszyfrowany(macierz):
    for i in range(len(macierz)):
        for j in range(len(macierz)):
            if macierz[j][i] != "X":
                print(macierz[j][i],end="")



napis = input()
klucz = int(input())
odczytaj_odszyfrowany(kolumnowy(napis,klucz))