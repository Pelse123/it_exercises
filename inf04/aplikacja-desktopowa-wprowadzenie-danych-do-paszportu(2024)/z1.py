"""
**********************************************
nazwa funkcji: sprawdz_plec
opis funkcji: sprawdza płeć za pomocą peselu
parametry: pesel - wprowadzony pesel od użytkownika
zwracany typ i opis: zwraca znak 'K' w przypadku kiedy płcią jest kobieta w przeciwnym wypadku zwraca 'M' czyli mężczyzna
autor: <numer zdającego>
***********************************************
"""

def sprawdz_plec(pesel):
    pesel_string = str(pesel)
    numer_kontrolny = pesel_string[9]
    if int(numer_kontrolny)%2==0:
        return 'K'
    else:
        return 'M'

def suma_kontrolna(pesel):
    pesel_string = str(pesel)
    tablica_mnozen = [1,3,7,9]
    S=0
    for i in range(len(pesel_string)-1):
        liczba = int(pesel_string[i])
        aktualna_waga = tablica_mnozen[i%len(tablica_mnozen)]
        S += liczba*aktualna_waga
    M = S%10
    if M==0:
        R = 0
    else:
        R = 10-M
    if str(R)==pesel_string[len(pesel_string)-1]:
        return True
    else:
        return False




pesel = input("Wprowadź pesel: ")
if sprawdz_plec(pesel) == 'K':
    print("Kobieta")
else:
    print("Mężczyzna")
if suma_kontrolna(pesel):
    print("Pesel prawidłowy")
else:
    print("Pesel nieprawidłowy")

