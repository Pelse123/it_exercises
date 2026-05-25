def usuwanie_wartosc(slownik):
    nowy_slownik = {}
    for i in slownik:
        klucz = i
        wartosc = slownik[klucz]
        if wartosc != "Delete":
            nowy_slownik[klucz] = wartosc
    return nowy_slownik

slownik={}
ilosc = int(input())

for i in range(ilosc):
    klucz = input()
    wartosc = input()
    slownik[klucz] = wartosc

slownik_usuniete = usuwanie_wartosc(slownik)

for i in slownik_usuniete:
    print(f"{i}: {slownik_usuniete[i]}")