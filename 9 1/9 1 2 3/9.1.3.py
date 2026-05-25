plik= open('slowa.txt', 'r')
zapis= open('wyniki4_1.txt', 'w')

tablica = []
wakacje = "wakacje"
for linia in plik:
    tablica.append(linia.strip())

tablica_mozliwych = []
for i in range(len(tablica)):
    k = 0
    for j in range(len(tablica[i])):
        if tablica[i][j] == wakacje[k%len(wakacje)]:
            k+=1
    ile_mozna_ulozyc = k//len(wakacje)
    ile_usunac = len(tablica[i])-(ile_mozna_ulozyc*len(wakacje))
    tablica_mozliwych.append(ile_usunac)

for i in range(len(tablica_mozliwych)):
    zapis.write(str(tablica_mozliwych[i]) + " ")

zapis.close()
plik.close()
