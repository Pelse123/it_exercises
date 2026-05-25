def sprawdz_czy_pusta_kolumna(tablica):
    licznik = 0
    for i in range(len(tablica[0])):
        flaga = True
        for j in range(len(tablica)):
            if tablica[j][i] != ".":
                flaga = False
        if flaga:
            licznik += 1
    return licznik


plik= open('szachy.txt', 'r')
zapis= open('zadanie1_1.txt', 'w')

tablica = []
plansze_z_pusta = 0
wiersz = []
maks_licznik = 0
for linia in plik:
    linia_planszy = linia.strip()
    if linia_planszy != "":
        wiersz.append(linia_planszy)
    else:
        tablica.append(wiersz)
        wiersz = []

if wiersz:
    tablica.append(wiersz)


for i in range(len(tablica)):
    licznik = sprawdz_czy_pusta_kolumna(tablica[i])
    if licznik>0:
        plansze_z_pusta += 1
    if licznik>maks_licznik:
        maks_licznik = licznik

zapis.write(str(plansze_z_pusta)+" "+str(maks_licznik)+"\n")

zapis.close()
plik.close()