def czy_pierwsza(liczba):
    if(liczba<2):
        return False
    else:
        for i in range(2,liczba):
            if(liczba%i==0):
                return False
    return True

slownik_do = int(input())
slownik = {}
for i in range(slownik_do):
    klucz = i+1
    wartosc = czy_pierwsza(klucz)
    slownik[klucz] = wartosc

for i in slownik:
    print(f"{i}: {slownik[i]}")

