import random

class Kosc():
    statyczna = 0
    tablica = ["kosc0.png", "kosc1.png", "kosc2.png", "kosc3.png", "kosc4.png", "kosc5.png", "kosc6.png"]
    czy_dostepna:bool
    indetyfikator:int
    ile_oczek:int
    def __init__(self,wyrzucona_kosc = None):
        if wyrzucona_kosc is not None:
            if wyrzucona_kosc>=1 and wyrzucona_kosc<=6:
                self.wyrzucona_kosc=wyrzucona_kosc
            else:
                self.wyrzucona_kosc=0
        Kosc.czy_dostepna = True
        Kosc.indetyfikator = wyrzucona_kosc
        Kosc.ile_oczek = wyrzucona_kosc
        Kosc.statyczna +=1

    def metoda_rzutu(self):
        if self.czy_dostepna:
            losowa = random.randint(1,6)
            self.indetyfikator = losowa
            self.ile_oczek = losowa

    def blokuj_kosc(self):
        self.czy_dostepna = False

    def tekst_kosc(self):
        tab=["jeden","dwa","trzy","cztery","pięć","sześć"]
        return tab[self.indetyfikator-1]


obiekt1 = Kosc()
obiekt2 = Kosc(int(input()))
obiekt1.metoda_rzutu()
print(obiekt1.tekst_kosc(),obiekt1.ile_oczek,obiekt1.tablica[obiekt1.indetyfikator])
print(obiekt1.statyczna)
print(obiekt2.tekst_kosc(),obiekt2.ile_oczek,obiekt1.tablica[obiekt2.indetyfikator])
print(obiekt2.statyczna)




