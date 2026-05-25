"""
************************************************
 klasa: Notatka
 opis: Klasa reprezentuje system notatki która wyświetla notatki
 pola: __licznik - (counter) liczy ilość wywołanych konstruktorów
__id - jest indetyfikatorem notatki który przyjmuje wartości licznika
_tytul - pole przyjmujące tytul notatki
_tresc - pole przyjmujące treść notatki
 autor: 00000000000000000000000
************************************************
"""
class Notatka():
    __licznik:int = 0
    def __init__(self,tytul:str,tresc:str):
        Notatka.__licznik += 1
        self.__id:int = Notatka.__licznik
        self._tytul = tytul
        self._tresc = tresc

    def wyswietl(self):
        print(f"Tytuł: {self._tytul}\nTreść:{self._tresc}")

    def diagnostyczna(self):
        print(f"{self._tytul};{self._tresc};{Notatka.__licznik};{self.__id}")

notatka1 = Notatka("Wynieść śmieci","Posegregowane śmieci są w pojemnikach")
notatka2 = Notatka("Zrobić zakupy","Ser,jajka,masło")

notatka1.wyswietl()
notatka1.diagnostyczna()
print()
notatka2.wyswietl()
notatka2.diagnostyczna()

