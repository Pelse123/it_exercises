def zwroc_przed_przecinkiem(liczba):
    wynik = 0
    liczba = str(int(liczba))
    for i in range(len(liczba)-1, -1, -1):
        wynik += int(liczba[len(liczba)-1-i])*2**i
    return wynik

def zwroc_za_przecinkiem(liczba):
    wynik = 0
    liczba = str(liczba)
    czy_przecinek = False
    iterator = 1
    for i in range(len(liczba)):
        if liczba[i] == ".":
            czy_przecinek = True
            continue
        if czy_przecinek:
            wynik = wynik + int(liczba[i])*(1/(2**iterator))
            iterator = iterator + 1

    return wynik


def policz_binarny_na_ulamek(liczba):
    poczatek = zwroc_przed_przecinkiem(liczba)
    za_przecinkiem = zwroc_za_przecinkiem(liczba)
    wynik = poczatek+za_przecinkiem
    return wynik


liczba = float(input())
print(policz_binarny_na_ulamek(liczba))
