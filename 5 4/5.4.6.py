def szyfrowanie_plotkowe(tekst,klucz):
    szyfrogram = ""

    macierz = []
    for i in range(klucz):
        macierz.append([])
        for j in range(len(tekst)):
            macierz[i].append(" ")
    wDol = True
    licznik = 0
    for i in range(len(tekst)):
        macierz[licznik][i] = tekst[i]
        if wDol:
            licznik = licznik + 1
        else:
            licznik = licznik - 1

        if licznik == 0 or licznik == klucz-1:
            wDol = not wDol

    for i in range(klucz):
        for j in range(len(tekst)):
            if macierz[i][j]!=" ":
                szyfrogram = szyfrogram + macierz[i][j]
    return szyfrogram

tekst_jawny = input()
klucz = int(input())
print(szyfrowanie_plotkowe(tekst_jawny,klucz))