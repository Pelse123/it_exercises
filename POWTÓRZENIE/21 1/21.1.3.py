def znak_rzymski_na_arabski(znak):
    slownik_znakow = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    return slownik_znakow[znak]

def rzymski_na_arabski(rzymska):
    if rzymska.isdigit():
        return int(rzymska)
    else:
        wynik = 0

        for i in range(len(rzymska)):
            aktualna_arabska = znak_rzymski_na_arabski(rzymska[i])
            if i+1<len(rzymska):
                nastepna_arabska = znak_rzymski_na_arabski(rzymska[i+1])
                if aktualna_arabska<nastepna_arabska:
                    wynik = wynik - aktualna_arabska
                else:
                    wynik = wynik + aktualna_arabska
            else:
                wynik += aktualna_arabska

    return wynik

wielkosc_macierzy = int(input())
macierz = []

for i in range(wielkosc_macierzy):
    wiersz = []
    for j in range(wielkosc_macierzy):
        wiersz.append(input())
    macierz.append(wiersz)

suma = 0
for i in range(wielkosc_macierzy):
    if i != wielkosc_macierzy-1-i:
        suma = suma + rzymski_na_arabski(macierz[i][i])
        suma = suma + rzymski_na_arabski(macierz[i][wielkosc_macierzy-1-i])
    else:
        suma = suma + rzymski_na_arabski(macierz[i][i])


print(suma)







