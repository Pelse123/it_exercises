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

def sprawdz_4_czesci(n,tablica):
    czesc1 = []
    czesc2 = []
    czesc3 = []
    czesc4 = []
    k1 = 0
    k2 = 0
    for i in range(k1,n//2):
        for j in range(k2,n//2):
            czesc1.append(tablica[i][j])
    k1 = n//2
    k2 = 0
    for i in range(k1,n):
        for j in range(k2,n//2):
            czesc2.append(tablica[i][j])
    k1 = 0
    k2 = n//2
    for i in range(k1,n//2):
        for j in range(k2,n):
            czesc3.append(tablica[i][j])

    k1 = n//2
    k2 = n//2
    for i in range(k1,n):
        for j in range(k2,n):
            czesc4.append(tablica[i][j])
    if czesc1 == czesc2 == czesc3 == czesc4:
        return True
    else:
        return False



plik = open("dane_obrazki.txt", "r")
zapis = open("wyniki_obrazki.txt", "w")
tablica = wczytaj(plik)
pierwszy = True
licznik = 0
zap = []
for i in range(len(tablica)):
    if sprawdz_4_czesci(20,tablica[i]):
        licznik+=1
        if pierwszy:
            zap.append(tablica[i])
            pierwszy = False



zapis.write("Liczba obrazkow rekurencyjnych: "+str(licznik) + "\n")
zapis.write("Opis obrazka:\n")

for i in range(20):
    for j in range(20):
        zapis.write(str(zap[0][i][j]))
    zapis.write("\n")

zapis.close()
plik.close()