plik= open('napisy.txt', 'r')
zapis= open('wyniki4.txt', 'w')

zapis.write("b)\n")
haslo = ""
licznik = 1
licznik_pozycji = 0
for linia in plik:
    if licznik%20 == 0:
        haslo += linia.strip()[licznik_pozycji]
        licznik_pozycji += 1
    licznik += 1

zapis.write(haslo)


zapis.close()
plik.close()
