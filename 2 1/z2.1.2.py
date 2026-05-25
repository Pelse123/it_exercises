ilosc_danych = int(input())
slownik = {}
for i in range(ilosc_danych):
    klucz = input()
    wartosc = input()
    slownik[klucz] = wartosc

odwrocony_slownik = {}
for klucz,wartosc in slownik.items():
    odwrocony_slownik[wartosc] = klucz

for klucz,wartosc in odwrocony_slownik.items():
    print(f"{klucz}: {wartosc} ")
