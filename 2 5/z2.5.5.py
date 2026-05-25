def dodaj_polaczenie_grafu(macierz,wierzcholek1,wierzcholek2):
    macierz[wierzcholek1][wierzcholek2] = 1
    macierz[wierzcholek2][wierzcholek1] = 1
    return macierz

def zlicz_stopnie(macierz):
    stopnie = []
    for i in range(len(macierz)):
        suma = 0
        for j in range(len(macierz[i])):
            suma += macierz[i][j]
        stopnie.append(suma)
    return stopnie


ilosc_wierzcholkow = int(input())
graf = []
for i in range(ilosc_wierzcholkow):
    graf.append([0]*ilosc_wierzcholkow)
liczba_polaczen = int(input())
stopien = []
for i in range(liczba_polaczen):
    stopien = dodaj_polaczenie_grafu(graf, int(input()), int(input()))

stopien = zlicz_stopnie(stopien)
for i in range(len(stopien)):
    print(f"Stopień wierzchołka {i}: {stopien[i]}")

