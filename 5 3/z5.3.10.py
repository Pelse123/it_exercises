def znajdz_najdluzszy_wspolny_podciag(x,y):
    ciag_x = y
    ciag_y = x
    dlugosc_x = len(ciag_x)
    dlugosc_y = len(ciag_y)
    macierz = []
    wynik=""
    for i in range(dlugosc_x+1):
        wiersz = []
        for j in range(dlugosc_y+1):
            wiersz.append(0)
        macierz.append(wiersz)

    for i in range(1,dlugosc_x+1):
        for j in range(1,dlugosc_y+1):
            if ciag_x[i-1]==ciag_y[j-1]:
                macierz[i][j] = macierz[i-1][j-1]+1
            else:
                if macierz[i][j-1]>macierz[i-1][j]:
                    macierz[i][j] = macierz[i][j-1]
                else:
                    macierz[i][j] = macierz[i-1][j]
    i = dlugosc_x
    j = dlugosc_y
    while i>0 and j>0:
        if ciag_x[i - 1] == ciag_y[j - 1]:
            wynik = ciag_x[i-1]+wynik
            i = i-1
            j = j-1
        else:
            if macierz[i][j - 1] > macierz[i - 1][j]:
                j = j-1
            else:
                i=i-1
    return wynik

napis1 = input()
napis2 = input()
print(znajdz_najdluzszy_wspolny_podciag(napis1,napis2))