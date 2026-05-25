plik = open("sekwencje.txt","r")
zapis = open("wyniki_alfa.txt","w")
licznik = 1
kod_genetyczny = ""
for linia in plik:

    if licznik%20 == 0:
        piata_litera = linia.strip()[4]
        kod_genetyczny += piata_litera

    licznik = licznik + 1

zapis.write("1)\n")
zapis.write(kod_genetyczny)

zapis.close()
plik.close()
