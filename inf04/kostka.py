import random
class gra():
    def __init__(self,ile_rzut):
        self.ile_rzut = ile_rzut

    def losowanie(self):
        tablica_kosci = []
        for i in range(self.ile_rzut):
            tablica_kosci.append(random.randint(1,6))
        for i in range(len(tablica_kosci)):
            print(f"Kostka {i + 1}: {tablica_kosci[i]}")
        return tablica_kosci

    def wynik(self,tablica_kosci):
        tablica_rzuconych = [0]*6 #kosci od 1 do 6
        for i in range(len(tablica_kosci)):
            tablica_rzuconych[tablica_kosci[i]-1] +=1
        wynik = 0
        for i in range(len(tablica_rzuconych)):
            if tablica_rzuconych[i] >1:
                wynik += tablica_rzuconych[i]*(i+1)
        print(f"Liczba uzyskanych punktów:{wynik}")
        return wynik

t = "t"
while t == "t":
    ile_rzut = 0
    while ile_rzut<3 or ile_rzut>10:
        ile_rzut = int(input("Ile kostek chcesz rzucić(3 - 10)\n"))

    kostki = gra(ile_rzut)
    wylosowana = kostki.losowanie()
    kostki.wynik(wylosowana)
    t = input("Jeszcze raz? (t/n)\n").strip().lower()





