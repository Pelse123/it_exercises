def zamiana_na_rzymskie(wynik,liczba):
    for klucz in rzymskie:
        wartosc = rzymskie[klucz]
        while liczba >= wartosc:
            wynik += klucz
            liczba -= rzymskie[klucz]
    return wynik

rzymskie = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}
wynik = ""
liczba =int(input())

print(zamiana_na_rzymskie(wynik,liczba))
