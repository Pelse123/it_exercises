ilosc_danych = int(input())
slownik = {}
for i in range(ilosc_danych):
    klucz = input()
    wartosc = input()
    slownik[klucz] = wartosc

for klucz,wartosc in slownik.items():
    print(f"{wartosc} -> {klucz} ")
