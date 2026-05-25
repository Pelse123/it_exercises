def funkcja_usuwajaca_spacje(slowo):
    nowe_slowo = ""
    for i in range(len(slowo)):
        if slowo[i] != " ":
            nowe_slowo += slowo[i]
    return nowe_slowo

ilosc_danych = int(input())
slownik = {}
for i in range(ilosc_danych):
    klucz = input()
    wartosc = input()
    slownik[klucz] = wartosc

nowy_slownik = {}
for klucz in slownik:
    klucz_bez_spacji = funkcja_usuwajaca_spacje(klucz)
    nowy_slownik[klucz_bez_spacji] = slownik[klucz]

for klucz,wartosc in nowy_slownik.items():
    print(f"{klucz}: {wartosc}")
