plik= open('galerie.txt', 'r')
zapis= open('wynik4_1.txt', 'w')

tablica_miast = []
for linia in plik:
     galeria = (linia.strip()).split()
     tablica_miast.append(galeria)

maks_miasto_suma = 0
maks_miasto_nazwa = ""
min_miasto_suma = -1
min_miasto_nazwa = ""

for i in range(len(tablica_miast)):
    suma_miasta = 0
    for j in range(3,len(tablica_miast[i]),2):
        if tablica_miast[i][j-1] != "0" and tablica_miast[i][j] != "0":
            suma_miasta += int(tablica_miast[i][j-1])*int(tablica_miast[i][j])
    if min_miasto_suma == -1:
        min_miasto_suma = suma_miasta
    if min_miasto_suma > suma_miasta:
        min_miasto_suma = suma_miasta
        min_miasto_nazwa = tablica_miast[i][1]
    if maks_miasto_suma < suma_miasta:
        maks_miasto_suma = suma_miasta
        maks_miasto_nazwa = tablica_miast[i][1]

zapis.write(f"{maks_miasto_nazwa} {maks_miasto_suma}\n")
zapis.write(f"{min_miasto_nazwa} {min_miasto_suma}\n")

zapis.close()
plik.close()