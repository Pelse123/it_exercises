class Osoba():
    statyczne = 0
    def __init__(self,id=0,imie=""):
        self.__id = int(id)
        self.__imie = str(imie)
        Osoba.statyczne+=1

    def kopiujaca(self):
        return Osoba(self.__id,self.__imie)

    def wypisujaca(self,argument):
        if self.__imie != "":
            print(f"Cześć {argument} mam na imie {self.__imie}")
        else:
            print("Brak danych")

print(Osoba.statyczne)
ob1 = Osoba()
ob2 = Osoba(int(input()),input())
ob3 = Osoba.kopiujaca(ob2)
parametr = "Jan"
ob1.wypisujaca(parametr)
ob2.wypisujaca(parametr)
ob3.wypisujaca(parametr)
Osoba.wypisujaca(Osoba(3,"Kamil"),parametr)
print(Osoba.statyczne)