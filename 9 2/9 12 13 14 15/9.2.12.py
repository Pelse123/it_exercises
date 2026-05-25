plik= open('dane_ulamki.txt', 'r')
zapis= open('wyniki_ulamki.txt', 'w')

tablica= []
for linia in plik:
       tablica.append(linia.strip().split())
tablica_int = []

minim = -1
licznik = 0
mianownik = 0
for i in range(len(tablica)):
    wiersz =[]
    for j in range(len(tablica[i])):
        wiersz.append(int(tablica[i][j]))
    tablica_int.append(wiersz)
for i in range(len(tablica_int)):
    ulamek = tablica_int[i][0]/tablica_int[i][1]
    if minim == -1:
        minim = ulamek
        licznik = tablica_int[i][0]
        mianownik = tablica_int[i][1]
    if ulamek < minim:
        minim = ulamek
        licznik = tablica_int[i][0]
        mianownik = tablica_int[i][1]
    elif ulamek == minim:
        if mianownik >  tablica_int[i][1]:
            licznik = tablica_int[i][0]
            mianownik = tablica_int[i][1]
            minim = ulamek

zapis.write(str(licznik) + " " + str(mianownik) + '\n')

zapis.close()
plik.close()