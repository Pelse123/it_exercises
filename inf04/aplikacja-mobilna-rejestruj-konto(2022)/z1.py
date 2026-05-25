"""/********************************************************
* nazwa funkcji: <__znajdz_maksymalna_wartosc>
* parametry wejściowe: i - poczatek pętli
* wartość zwracana: maks - indeks maksymalnej wartości
*
* nazwa funkcji: <sortowanie_przez_wybieranie>
* parametry wejściowe: self - tablica  przyjęta z konstruktora
* wartość zwracana: tablica - posortowana tablica
* autor: <numer PESEL zdającego>
* ****************************************************/"""
class sortowanie:
    def __init__(self,tablica):
        self.tablica = tablica

    def __znajdz_maksymalna_wartosc(self,i):
        maks = i
        for j in range(i+1,len(self.tablica)):
            if self.tablica[maks]<self.tablica[j]:
                maks = j
        return maks
    def sortowanie_przez_wybieranie(self):
        for i in range(len(self.tablica)):
            szukaj = self.__znajdz_maksymalna_wartosc(i)
            self.tablica[i],self.tablica[szukaj] = self.tablica[szukaj],self.tablica[i]
        return self.tablica


tab = [0]*10
print("Wypełnij tablice liczbami")
for i in range(10):
    tab[i] = int(input(F"Podaj liczbe w miejsce tablicy {i} :"))
sortowanie = sortowanie(tab)
print(sortowanie.sortowanie_przez_wybieranie())


