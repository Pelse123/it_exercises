def zwroc_przed_przecinkiem(liczba):
    if int(liczba) == 0:
        return "0"
    liczba = int(liczba)
    wynik = ""
    while liczba>0:
        wynik = str(liczba%2)+wynik
        liczba = liczba//2
    return wynik
def policz_ulamek_na_binarny(liczba,prezycja):
    poczatkowa = zwroc_przed_przecinkiem(liczba)
    liczba = liczba - int(liczba)
    wynik = ""
    while liczba>0 and len(wynik)<prezycja:
        liczba = liczba*2
        wynik = wynik + str(zwroc_przed_przecinkiem(liczba))
        liczba = liczba - int(zwroc_przed_przecinkiem(liczba))
    while len(wynik)<prezycja:
        wynik = wynik + "0"

    return poczatkowa + "." + wynik

liczba = float(input())
precyzja = int(input())
print(f"{policz_ulamek_na_binarny(liczba,precyzja)}")