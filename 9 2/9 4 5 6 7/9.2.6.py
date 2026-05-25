def liczba_na_czynniki(liczba):
    tablica = []
    i = 2
    while liczba!=1:
        while liczba % i == 0:
            tablica.append(i)
            liczba = liczba // i
        i = i + 1

    return tablica

def stworz_unikalna(tablica):
    tablica_unikalna=[]
    for i in range (len(tablica)):
        if tablica[i] not in tablica_unikalna:
            tablica_unikalna.append(tablica[i])
    return tablica_unikalna

def policz_unikalna(tablica_unikalna,tablica):
    policz = [0]*len(tablica_unikalna)
    for i in range(len(tablica)):
        for j in range(len(tablica_unikalna)):
            if tablica_unikalna[j] == tablica[i]:
                policz[j] += 1
    return policz

plik= open('liczby.txt', 'r')
zapis= open('wyniki4.txt', 'w')

pierwszy_wiersz_str = plik.readline().strip(). split(" ")
drugi_wiersz_str = plik.readline().strip().split(" ")
pierwszy_wiersz=[]
drugi_wiersz=[]
for i in range(len(pierwszy_wiersz_str)):
    pierwszy_wiersz.append(int(pierwszy_wiersz_str[i]))
for i in range(len(drugi_wiersz_str)):
    drugi_wiersz.append(int(drugi_wiersz_str[i]))

pierwszy_wiersz_unikalne = stworz_unikalna(pierwszy_wiersz)
policz_wiersz_unikalne = policz_unikalna(pierwszy_wiersz_unikalne, pierwszy_wiersz)

for i in range(len(drugi_wiersz)):
    na_czynniki = liczba_na_czynniki(int(drugi_wiersz[i]))
    unikalna_czynnikow = stworz_unikalna(na_czynniki)
    policz_unikalne_czynniki = policz_unikalna(unikalna_czynnikow,na_czynniki)
    flaga = True
    for j in range(len(unikalna_czynnikow)):
        znaleziono =  False
        for k in range(len(pierwszy_wiersz_unikalne)):
            if unikalna_czynnikow[j]==pierwszy_wiersz_unikalne[k]:
                znaleziono = True
                if policz_unikalne_czynniki[j]>policz_wiersz_unikalne[k]:
                    flaga = False
        if znaleziono==False:
            flaga = False
    if flaga:
        zapis.write(str(drugi_wiersz[i]) + " ")

zapis.close()
plik.close()