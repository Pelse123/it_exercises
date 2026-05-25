def sprawdz_czy_ciag_rosnacy(slowo):
    tablica=[]
    for i in range(len(slowo)):
        tablica.append(int(slowo[i]))
    for i in range(1,len(tablica)):
        if(tablica[i]<=tablica[i-1]):
            return False
    return True

plik = open("cyfry.txt", "r")
zapis = open("zadanie4.txt", "w")

zapis.write("c)\n")
for liczba in plik:
    if sprawdz_czy_ciag_rosnacy(liczba.strip()):
        zapis.write(liczba)

plik.close()
zapis.close()