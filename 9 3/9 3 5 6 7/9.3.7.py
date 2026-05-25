def sprawdz_kwadrat(rozmiar,tablica):
    for i in range(rozmiar):
        for j in range(rozmiar):
            if tablica[i][j]=="X":
                return -1
    return rozmiar

plik = open("dzialki.txt","r")
zapis = open("wynik4.txt","w")

wiersz = []
tablica = []

for line in plik:
    linia = line.strip()
    if linia != "":
        wiersz.append(linia)
    else:
        tablica.append(wiersz)
        wiersz = []


maks = 0
for i in range(len(tablica)):
    for j in range(len(tablica[i])):
        if sprawdz_kwadrat(j,tablica[i])>maks:
            maks = sprawdz_kwadrat(j,tablica[i])

dzialki = []
for i in range(len(tablica)):
    if sprawdz_kwadrat(maks,tablica[i])==maks:
        dzialki.append(i+1)

zapis.write("Numery dzialek: ")
for i in range(len(dzialki)):
    zapis.write(str(dzialki[i])+" ")
zapis.write("\nMaksymalny bok: "+str(maks))

zapis.close()
plik.close()