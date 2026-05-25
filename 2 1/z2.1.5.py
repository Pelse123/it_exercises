def szukaj_najwieksza_wartosc(slownik):
    maks = 0
    for klucz in slownik:
        wartosc = slownik[klucz]
        if wartosc > maks:
            maks = wartosc
    return maks

ilosc = int(input())
slownik = {}
for i in range(ilosc):
    klucz = (input())
    wartosc = int(input())
    slownik[klucz] = wartosc

print(szukaj_najwieksza_wartosc(slownik))