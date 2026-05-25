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
print(len(tablica))
def sprawdz_czy_się_zgadza_wiersz(tablica):
    ilosc_zle = 0
    for i in range(len(tablica)-1):
        bialy = 0
        czarny = 0
        for j in range(len(tablica[i])-1):
            if tablica[i][j]=="0":
                bialy+=1
            elif tablica[i][j]=="1":
                czarny+=1
        if czarny%2 == 0:
            if tablica[i][len(tablica[i])-1]!="0":
                ilosc_zle+=1
        else:
            if tablica[i][len(tablica[i])-1]=="0":
                ilosc_zle+=1
    return ilosc_zle

def sprawdz_czy_sie_zgadza_kolumna(tablica):
    ilosc_zle = 0
    for i in range(len(tablica[0])-1):
        bialy = 0
        czarny = 0
        for j in range(len(tablica)-1):
            if tablica[j][i]=="0":
                bialy+=1
            elif tablica[j][i]=="1":
                czarny+=1
        if czarny%2 == 0:
            if tablica[len(tablica[0])-1][i]!="0":
                ilosc_zle+=1
        else:
            if tablica[len(tablica[0])-1][i]=="0":
                ilosc_zle+=1
    return ilosc_zle
poprawne=0
niepoprawne=0
naprawialne = 0
maks_zle = 0
for i in range(len(tablica)):
    kolumny_zle = sprawdz_czy_sie_zgadza_kolumna(tablica[i])
    wiersze_zle = sprawdz_czy_się_zgadza_wiersz(tablica[i])
    zle = kolumny_zle+wiersze_zle
    if zle > maks_zle:
        maks_zle = zle
    if kolumny_zle==0 and wiersze_zle==0:
        poprawne+=1
    elif kolumny_zle>1 or wiersze_zle>1:
        niepoprawne+=1
    elif (kolumny_zle==1 or kolumny_zle==0) and (wiersze_zle==1 or wiersze_zle==0):
        naprawialne+=1

zapis.write(f"Liczba obrazkow poprawnych:{poprawne}\nLiczba obrazkow naprawialnych:{naprawialne}\nLiczba obrazkow nienaprawialnych:{niepoprawne}\nNajwieksza liczba blednych parzystosci:{maks_zle}\n")

zapis.close()
plik.close()