def wczytaj(plik):
    tablica = []
    wiersz = []
    for line in plik:
        linia = line.strip()
        if linia != "":
            wiersz.append(linia)
        else:
            tablica.append(wiersz)
            wiersz = []
    tablica.append(wiersz)
    return tablica
plik = open("dane_obrazki.txt", "r")
zapis = open("wyniki_obrazki.txt", "w")
tablica = wczytaj(plik)


licznik =0
maks =0
for i in range(len(tablica)):
    bialy = 0
    czarny = 0
    for j in range(len(tablica[i])-1):
        for k in range(len(tablica[i][j])-1):
            if tablica[i][j][k] == "0":
                bialy = bialy + 1
            if tablica[i][j][k] == "1":
                czarny = czarny + 1

    if czarny > bialy:
        licznik = licznik + 1
        if maks <= czarny:
            maks = czarny

zapis.write(f"Liczba rewersow: {licznik}\nNajwieksza liczba czarnych pikseli:{maks}\n")

zapis.close()
plik.close()