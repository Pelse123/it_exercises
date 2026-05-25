def binarny_na_dziesietny(linia):
    wynik = 0
    for i in range(len(linia)):
        wynik += int(linia[i])*2**(len(linia)-i-1)
    return wynik

def dziesietny_na_binarny(linia):
    liczba = int(linia)
    wynik = ""
    while liczba > 0:
        wynik = str(liczba%2) + wynik
        liczba = liczba // 2
    return wynik

plik= open('anagram.txt', 'r')
zapis= open('wyniki3.txt', 'w')
najwieksza_roznica = -1
tablica = []
for linia in plik:
    tablica.append(linia.strip())

for i in range(1,len(tablica)):
    if najwieksza_roznica == -1:
        najwieksza_roznica = abs(binarny_na_dziesietny(tablica[i-1]) - binarny_na_dziesietny(tablica[i]))
    roznica = abs(binarny_na_dziesietny(tablica[i - 1]) - binarny_na_dziesietny(tablica[i]))
    if roznica > najwieksza_roznica:
        najwieksza_roznica = roznica

zapis.write("c)\n")
zapis.write(f"{dziesietny_na_binarny(najwieksza_roznica)}\n")

zapis.close()
plik.close()