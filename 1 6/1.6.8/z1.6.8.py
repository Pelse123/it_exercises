plik = open("napisy.txt", "r")
zapis = open("zadanie4.txt", "w")
aktualna_linia = ""
ilosc_parzystych = 0

for linia in plik:
    licznik = 0
    aktualna_linia = linia.strip()
    for i in range(len(aktualna_linia)):
        licznik = licznik + 1
    if licznik%2 == 0:
        ilosc_parzystych += 1

zapis.write(f"a)\n{ilosc_parzystych}")

zapis.close()
plik.close()