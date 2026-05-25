def licz_ile_zywych(tablica):
    licznik = 0
    for i in range(len(tablica)):
        for j in range(len(tablica[i])):
            if tablica[i][j]=="X":
                licznik += 1
    return licznik


def wypisz_gre(tablica):
    for i in range(len(tablica)):
        for j in range(len(tablica[i])):
            print(tablica[i][j], end="")
        print()


def ile_zywych(tablica):
    # [i-1][j-1] [i-1][j] [i-1][j+1]
    # [i][j-1]   [i][j]   [i][j+1]
    # [i+1][j-1] [i+1][j]  [i+1][j+1]
    # ilosc wierszy = 12
    # ilosc kolumn = 20
    # i%12
    # j%20

    wynik = []
    for i in range(len(tablica)):
        wiersz = []
        for j in range(len(tablica[i])):
            licznik = 0
            tablica_kombinacji = [
                [i - 1, j - 1], [i - 1, j], [i - 1, j + 1],
                [i, j - 1], [i, j], [i, j + 1],
                [i + 1, j - 1], [i + 1, j], [i + 1, j + 1]
            ]
            for k in range(len(tablica_kombinacji)):
                ki = tablica_kombinacji[k][0] % 12
                kj = tablica_kombinacji[k][1] % 20
                if ki == i and kj == j:
                    continue
                if tablica[ki][kj] == "X":
                    licznik += 1
            wiersz.append(licznik)
        wynik.append(wiersz)
    return wynik

def sprawdz_tablice(tablica1,tablica2):
    for i in range(len(tablica1)):
        for j in range(len(tablica1)):
            if tablica1[i][j]!=tablica2[i][j]:
                return False
    return True

def kolejne_pokolenie(tablica):
    zywi = ile_zywych(tablica)
    wynik = ile_zywych(tablica)
    for i in range(len(zywi)):
        for j in range(len(zywi[i])):
            if zywi[i][j] < 2:
                wynik[i][j] = "-"
            if zywi[i][j] == 2:
                if tablica[i][j] == "X":
                    wynik[i][j] = "X"
                else:
                    wynik[i][j] = "-"
            if zywi[i][j] == 3:
                wynik[i][j] = "X"
            if zywi[i][j] > 3:
                wynik[i][j] = "-"
    return wynik


plik = open('gra.txt', 'r')
zapis = open('wyniki_5.txt', 'w')
gra = []
wynik = []
for linia in plik:
    wiersz = []
    wiersz2 = []
    for i in range(len(linia.strip())):
        wiersz.append(linia[i])
        wiersz2.append(linia[i])
    wynik.append(wiersz)
    gra.append(wiersz2)
wynik = kolejne_pokolenie(wynik)
pokolenie = 2
for i in range(99):
    if sprawdz_tablice(gra, wynik):
        break
    gra = kolejne_pokolenie(gra)
    wynik = kolejne_pokolenie(wynik)
    pokolenie += 1

zapis.write(f"{pokolenie} pokolenie\n")
zapis.write(f"{licz_ile_zywych(gra)} zywych komorek")

zapis.close()
plik.close()