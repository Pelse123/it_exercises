def sprawdz_klucze(slownik,slownik2):
    for i in slownik:
        for j in slownik2:
            if i == j:
                print(f"{i}")

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

sprawdz_klucze(slownik,slownik2)