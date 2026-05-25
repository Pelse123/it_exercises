def usun_wartosc(slownik,ilosc):
    nowy_slownik = {}
    srednia = 0
    for klucz1 in slownik:
        wartosc1 = slownik[klucz1]
        srednia += wartosc1
    srednia = srednia / ilosc
    for klucz in slownik:
        wartosc = slownik[klucz]
        if wartosc>srednia:
            nowy_slownik[klucz] = wartosc
    return nowy_slownik

slownik={}
ilosc = int(input())

for i in range(ilosc):
    klucz = input()
    wartosc = int(input())
    slownik[klucz] = wartosc

nowy_slownik = usun_wartosc(slownik,ilosc)

for klucz in nowy_slownik:
    print(f"{klucz}: {nowy_slownik[klucz]}")