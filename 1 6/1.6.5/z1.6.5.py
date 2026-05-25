def czy_liczba_parzysta(liczba):
    if liczba%2==0:
        return True
    return False

plik = open("cyfry.txt", "r")
zapis = open("zadanie4.txt", "w")
wynik = 0
for linia in plik:
    if czy_liczba_parzysta(int(linia.strip())):
        wynik = wynik + 1

zapis.write(f"a)\n{wynik}\n")

zapis.close()
plik.close()