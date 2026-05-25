plik = open('dane8.txt', 'r')
zapis = open('wyniki8.txt', 'w')

tablica = []
for linia in plik:
    tablica.append(int(linia.strip()))

max_elementow = 0
licznik = 1
for i in range(1, len(tablica)):
    if tablica[i - 1] < tablica[i]:
        licznik += 1
    else:
        if licznik > max_elementow:
            max_elementow = licznik
        licznik = 1

if licznik > max_elementow:
    max_elementow = licznik

zapis.write(str(max_elementow))

zapis.close()
plik.close()