plik= open('galerie.txt', 'r')
zapis= open('wynik4_1.txt', 'w')

tablica_miast = []
for linia in plik:
     galeria = (linia.strip()).split()
     tablica_miast.append(galeria)
for i in range(len(tablica_miast)):
    licznik = 0
    suma_miasta = 0
    for j in range(3,len(tablica_miast[i]),2):
        if tablica_miast[i][j-1] != "0" and tablica_miast[i][j] != "0":
            suma_miasta += int(tablica_miast[i][j-1])*int(tablica_miast[i][j])
            licznik += 1
    zapis.write(f"{tablica_miast[i][1]} {suma_miasta} {licznik}\n")






zapis.close()
plik.close()