plik = open("dzialki.txt","r")
zapis = open("wynik4.txt","w")

ilosc = 0
inne = 0
gwiazdki = 0
for line in plik:
    linia = line.strip()
    if linia != "":
        for i in range(len(linia)):
            if linia[i] == "*":
                gwiazdki += 1
            else:
                inne += 1
    else:
        wszystkie = inne+gwiazdki
        roznica = gwiazdki/wszystkie
        if roznica>=0.7:
            ilosc += 1
        inne = 0
        gwiazdki = 0

zapis.write(str(ilosc))




zapis.close()
plik.close()