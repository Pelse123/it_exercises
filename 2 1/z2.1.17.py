def maks(tablica):
    maks = tablica[0]
    for i in range(len(tablica)):
        if maks<tablica[i]:
            maks = tablica[i]
    return maks

def czy_pierwsza(liczba):
    if liczba<2:
        return False
    else:
        for i in range(2,liczba):
            if liczba%i==0:
                return False
    return True

liczba = int(input())
tablica_wartosci = []

for i in range(liczba):
    tablica_wartosci.append(int(input()))
maksimum = maks(tablica_wartosci)
tablica_pierwszych = []

for i in range(maksimum+1):
    if czy_pierwsza(i):
        tablica_pierwszych.append(i)

slownik = {}

for i in range(len(tablica_pierwszych)):
    klucz = tablica_pierwszych[i]
    dzielniki = []
    for j in range(len(tablica_wartosci)):
        if tablica_wartosci[j]%klucz==0:
            dzielniki.append(tablica_wartosci[j])
    if len(dzielniki)>0:
        slownik[klucz] = dzielniki

for klucz in slownik:
    print(f"{klucz}: {slownik[klucz]}")