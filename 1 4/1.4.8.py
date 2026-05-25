def czy_pierwsza(liczba):
    czyPierwsza = True
    if liczba <2:
        czyPierwsza = False
    else:
        for i in range(2,liczba):
            if liczba % i == 0:
                czyPierwsza = False
                break
    return czyPierwsza

liczba = int(input())
if czy_pierwsza(liczba):
    print("Podana liczba jest pierwsza")
else:
    print("Podana liczba nie jest pierwsza")