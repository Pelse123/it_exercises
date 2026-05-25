
plik = open("napis.txt","r")
zapis = open("zadanie5.txt","w")

tablica = []
for linia in plik:
    linijka = linia.strip()
    tablica.append(linijka)

tablica_powtorzen = []
for i in range(len(tablica)):
    licznik = 0
    for j in range(len(tablica)):
        if tablica[j] == tablica[i]:
            licznik = licznik + 1
    if licznik>1 and tablica[i] not in tablica_powtorzen:
        tablica_powtorzen.append(tablica[i])

zapis.write("c)\n")
for i in range(len(tablica_powtorzen)):
    zapis.write(tablica_powtorzen[i]+"\n")

zapis.close()
plik.close()

