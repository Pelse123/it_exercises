plik= open('galerie.txt', 'r')
zapis= open('wynik4_1.txt', 'w')

tablica_miast = []
for linia in plik:
     galeria = (linia.strip()).split()
     miasto = galeria[0]
     tablica_miast.append(miasto)

slownik = {}
for i in range(len(tablica_miast)):
    if tablica_miast[i] not in slownik:
        slownik[tablica_miast[i]] = 0

for i in range(len(tablica_miast)):
    slownik[tablica_miast[i]] += 1

for klucz in slownik:
    wartosc = slownik[klucz]
    zapis.write(f"{klucz} {wartosc}\n")


zapis.close()
plik.close()