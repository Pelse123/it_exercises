def czy_parzysta_nieparzysta(slowo):
    if(len(slowo)%2==0):
        return True
    else:
        return False

plik = open("hasla.txt", "r")
zapis = open("wynik4a.txt", "w")

ilosc_parzystych = 0
ilosc_nieparzystych = 0
for line in plik:
    if czy_parzysta_nieparzysta(line.strip()):
        ilosc_parzystych += 1
    else:
        ilosc_nieparzystych += 1

zapis.write(f"Parzyste:{ilosc_parzystych}\nNieparzyste:{ilosc_nieparzystych}")
zapis.close()
plik.close()