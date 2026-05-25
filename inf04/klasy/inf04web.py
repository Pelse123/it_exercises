class Osoba:
    static = 0

    def __init__(self, id=0, imie=""):
        self.__id = id
        self.__imie = imie
        Osoba.static += 1

    def kopiuj(self):
        return Osoba(self.__id, self.__imie)

    def wypisz(self,argument=""):
        if argument!="":
            print(f"Cześć {argument}, mam na imię {self.__imie}")
        else:
            print("Brak danych")
