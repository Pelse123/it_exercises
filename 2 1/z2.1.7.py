def polacz_slowniki(slownik,slownik2):
    nowy_slownik={}
    for i in slownik:
        klucz1 = i
        wartosc1 = slownik[klucz1]
        nowy_slownik[klucz1] = wartosc1
    for j in slownik2:
        klucz = j
        wartosc = slownik2[klucz]
        if klucz in nowy_slownik:
            nowy_slownik[klucz] = nowy_slownik[klucz]
        else:
            nowy_slownik[klucz] = wartosc
    return nowy_slownik

ilosc = int(input())
slownik = {}
for i in range(ilosc):
    klucz = (input())
    wartosc = (input())
    slownik[klucz] = wartosc

ilosc_2_slownika = int(input())
slownik2 = {}
for i in range(ilosc_2_slownika):
    klucz2 = (input())
    wartosc2 = (input())
    slownik2[klucz2] = wartosc2

print(polacz_slowniki(slownik,slownik2))
