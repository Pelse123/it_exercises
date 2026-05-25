def dodaj_polaczenie_grafu(macierz,wierzcholek1,wierzcholek2):
    macierz[wierzcholek1][wierzcholek2] = 1
    return macierz

def szukaj_jedynki_w_grafie(macierz):
    tablica_relacji = []
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] == 1:
                tablica_relacji.append(f"{i} <-> {j}")
    return tablica_relacji

ilosc_wierzcholkow = int(input())
graf = []
for i in range(ilosc_wierzcholkow):
    graf.append([0]*ilosc_wierzcholkow)
liczba_polaczen = int(input())
for i in range(liczba_polaczen):
    graf = dodaj_polaczenie_grafu(graf, int(input()), int(input()))

print(graf)
wynik = szukaj_jedynki_w_grafie(graf)
for i in range(len(wynik)):
    print(wynik[i])