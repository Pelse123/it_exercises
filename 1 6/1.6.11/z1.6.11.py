plik = open("napisy.txt", "r")
zapis = open("zadanie4.txt", "w")

tablica = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
tablica_ilosci=[0]*16
dlugosc_napisu = 0

for linia in plik:
    dlugosc_napisu =len(linia.strip())
    for i in range(len(tablica)):
        if tablica[i] == dlugosc_napisu:
            tablica_ilosci[i] = tablica_ilosci[i] + 1
zapis.write("d)\n")
for wypisz in range(len(tablica)):
    zapis.write(f"{tablica[wypisz]} {tablica_ilosci[wypisz]}\n")

plik.close()
zapis.close()