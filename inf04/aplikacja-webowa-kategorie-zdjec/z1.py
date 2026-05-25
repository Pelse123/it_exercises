import random


class Operacje_na_tablicy():
    def __init__(self,liczba_elementow_tablicy:int):
        self.__liczba_elementow_tablicy = liczba_elementow_tablicy
        self.__tablica_liczb_calkowitych = [0]*self.__liczba_elementow_tablicy
        for i in range(len(self.__tablica_liczb_calkowitych)):
            self.__tablica_liczb_calkowitych[i] = random.randint(0,1000)

    def zwroc_elementy_tablicy(self):
        print("Elementy tablicy:")
        for i in range(len(self.__tablica_liczb_calkowitych)):
            print(i,":",self.__tablica_liczb_calkowitych[i])

    def znajdz_pierwsze_wystapienie(self,szukana):
        indeks = -1
        for i in range(len(self.__tablica_liczb_calkowitych)):
            if self.__tablica_liczb_calkowitych[i] == szukana:
                indeks = i
                break
        return indeks

    def wyswietl_wartosci_nieparzyste(self):
        print("Liczby nieparzyste:")
        ilosc = 0
        for i in range(len(self.__tablica_liczb_calkowitych)):
            if self.__tablica_liczb_calkowitych[i]%2!=0:
                ilosc+=1
                print(self.__tablica_liczb_calkowitych[i])
        return ilosc
    """
    **********************************************
    nazwa metody: srednia_arytmetyczna
    opis metody: metoda oblicza średnią arytmetyczną całej listy elementów
    parametry: self - jest referencją do aktualnej instancji klasy  i umozliwia dostęp do jej atrybutów i metod
    zwracany typ i opis: srednia arytmetyczna tablicy
    autor: 6969696966
    ***********************************************
    """
    def srednia_arytmetyczna(self):
        suma = 0
        for i in range(len(self.__tablica_liczb_calkowitych)):
            suma = suma + self.__tablica_liczb_calkowitych[i]
        srednia = suma / len(self.__tablica_liczb_calkowitych)
        return srednia

Obiekt_operacje = Operacje_na_tablicy(21)
Obiekt_operacje.zwroc_elementy_tablicy()
szukaj = Obiekt_operacje.znajdz_pierwsze_wystapienie(12)
if szukaj != -1:
    print(f"Znaleziono liczbę! Jej pierwsze wystąpienie: {szukaj} ")

print("Razem nieparzystych:",Obiekt_operacje.wyswietl_wartosci_nieparzyste())
print("Średnia wszystkich elementów: ",Obiekt_operacje.srednia_arytmetyczna())

