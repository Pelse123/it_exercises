"""
******************************************************
 nazwa klasy: Filmy
 pola: _tytul - przechowuje wartość string oraz tytul pobrany przez setter
 _liczba_wypozyczen - przechowuje wartość int ktora sie zwieksza wraz z wywolaniem funkcji zwieksz
 metody: setter - posiada argument tytul, metoda przypisuje wartosci argumentu tytul do pola _tytul
 getter_tytul - zwraca tytuł
 getter_liczba_wypozyczen - zwraca liczbe wypozyczen
 informacje: klasa filmy zawiera pola _tytul i _liczba_wypozyczen oraz 3 metody
 autor: 00000000000000000000
*****************************************************
"""
class Filmy():
    def __init__(self):
        self._tytul = ""
        self._liczba_wypozyczen = 0

    def setter(self,tytul):
        self._tytul = tytul

    def getter_tytul(self):
        return self._tytul

    def getter_liczba_wypozyczen(self):
        return self._liczba_wypozyczen

    def zwieksz(self):
        self._liczba_wypozyczen += 1

klasa = Filmy()
klasa.setter("star wars")
print(klasa.getter_tytul())
print(klasa.getter_liczba_wypozyczen())
klasa.zwieksz()
print(klasa.getter_liczba_wypozyczen())

