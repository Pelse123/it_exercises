def zamiana_na_dziesietny(liczba):
    wynik = 0
    for i in range(len(liczba)):
        potega = 3**(len(liczba)-i-1)
        wynik = wynik + potega*int(liczba[i])
    return wynik

kolko = "0"
plusik = "1"
gwiazdka = "2"
plik = open("symbole_przyklad.txt")
tablica_linii = []

for i in plik:
    tablica_linii.append(i)
plik.close()
konwersja_na_trojkowy = []

for i in range(len(tablica_linii)):
    wynik = ""
    for j in range(len(tablica_linii[i])):
        if tablica_linii[i][j] == "o":
            wynik += kolko
        if tablica_linii[i][j] == "+":
            wynik += plusik
        if tablica_linii[i][j] == "*":
            wynik += gwiazdka
    konwersja_na_trojkowy.append(wynik)

suma = 0
for i in range(len(konwersja_na_trojkowy)):
    liczba = zamiana_na_dziesietny(konwersja_na_trojkowy[i])
    suma += liczba

print(suma)


