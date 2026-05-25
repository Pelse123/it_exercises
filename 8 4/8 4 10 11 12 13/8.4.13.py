plik= open('galerie.txt', 'r')
zapis= open('wynik4_1.txt', 'w')

tablica_miast = []
for linia in plik:
     galeria = (linia.strip()).split()
     tablica_miast.append(galeria)

najmniejszy_licznik = -1
najmniejszy_miasto = ""
najwiekszy_licznik = 0
najwiekszy_miasto = ""
for i in range(len(tablica_miast)):
    tablica_pow = []
    for j in range(3,len(tablica_miast[i]),2):
        if tablica_miast[i][j-1] != "0" and tablica_miast[i][j] != "0":
            powierzchnia = int(tablica_miast[i][j-1])*int(tablica_miast[i][j])
            tablica_pow.append(powierzchnia)
    unikalna = list(set(tablica_pow))
    if najmniejszy_licznik == -1:
        najmniejszy_licznik = len(unikalna)
    if len(unikalna) < najmniejszy_licznik:
        najmniejszy_licznik = len(unikalna)
        najmniejszy_miasto = tablica_miast[i][1]
    if najwiekszy_licznik < len(unikalna):
        najwiekszy_licznik = len(unikalna)
        najwiekszy_miasto = tablica_miast[i][1]

zapis.write(f"{najwiekszy_miasto} {najwiekszy_licznik}\n{najmniejszy_miasto} {najmniejszy_licznik}\n")

zapis.close()
plik.close()