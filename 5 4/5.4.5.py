def odszyfrowanie_plotkowe(szyfrogram,klucz):
    tekst = ""

    macierz = []
    for i in range(klucz):
        macierz.append([])
        for j in range(len(szyfrogram)):
            macierz[i].append(" ")
    wDol = True
    licznik = 0
    for i in range(len(szyfrogram)):
        macierz[licznik][i] = "X"
        if wDol:
            licznik = licznik + 1
        else:
            licznik = licznik - 1

        if licznik == 0 or licznik == klucz-1:
            wDol = not wDol

    licznik_slow = 0
    for i in range(klucz):
        for j in range(len(szyfrogram)):
            if macierz[i][j] == "X":
                macierz[i][j] = szyfrogram[licznik_slow]
                licznik_slow = licznik_slow + 1


    for i in range(len(szyfrogram)):
        for j in range(klucz):
            if macierz[j][i] != " ":
                tekst = tekst + macierz[j][i]

    return tekst

szyfrogram = input()
klucz = int(input())
print(odszyfrowanie_plotkowe(szyfrogram,klucz))