def czy_antypalindrom(liczba):
    for i in range(len(liczba) // 2):
        if liczba[i] == liczba[len(liczba) - i - 1]:
            return False
    return True
plik= open('dane6.txt', 'r')
zapis= open('zadanie6_3.txt', 'w')
licznik = 0
zapis.write("c)\n")
for linia in plik:
    l = linia.strip()
    if czy_antypalindrom(l):
        zapis.write(f"{l}\n")
        licznik += 1
zapis.write(f"{licznik}\n")

zapis.close()
plik.close()