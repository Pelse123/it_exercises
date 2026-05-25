def czy_czarne(komorka):
    if ord(komorka) >= 97 and ord(komorka[0]) <= 122:
        return True
    return False

def czy_biale(komorka):
    if ord(komorka) >= 65 and ord(komorka[0]) <= 90:
        return True
    return False

def czy_wieza(komorka):
    return komorka == "w" or komorka == "W"

def czy_krol(komorka):
    return komorka == "k" or komorka == "K"

plik= open('szachy.txt', 'r')
zapis= open('zadanie1_2.txt', 'w')

tablica = []
wiersz = []
for linia in plik:
    linia_planszy = linia.strip()
    if linia_planszy != "":
        wiersz.append(linia_planszy)
    else:
        tablica.append(wiersz)
        wiersz = []

if wiersz:
    tablica.append(wiersz)


rownowaga = 0
mini_suma =-1


for i in range(len(tablica)):
    tablica_pionkow_bialych = [0, 0, 0, 0, 0, 0]
    tablica_pionkow_czarnych = [0, 0, 0, 0, 0, 0]
    for j in range(len(tablica[i])):
        for k in range(len(tablica[i][j])):
            if czy_czarne(tablica[i][j][k]):
                if tablica[i][j][k] == "p":
                    tablica_pionkow_czarnych[0]+=1
                if tablica[i][j][k] == "w":
                    tablica_pionkow_czarnych[1]+=1
                if tablica[i][j][k] == "s":
                    tablica_pionkow_czarnych[2]+=1
                if tablica[i][j][k] == "g":
                    tablica_pionkow_czarnych[3]+=1
                if tablica[i][j][k] == "h":
                    tablica_pionkow_czarnych[4]+=1
                if tablica[i][j][k] == "k":
                    tablica_pionkow_czarnych[5]+=1
            if czy_biale(tablica[i][j][k]):
                if tablica[i][j][k] == "P":
                    tablica_pionkow_bialych[0] += 1
                if tablica[i][j][k] == "W":
                    tablica_pionkow_bialych[1] += 1
                if tablica[i][j][k] == "S":
                    tablica_pionkow_bialych[2] += 1
                if tablica[i][j][k] == "G":
                    tablica_pionkow_bialych[3] += 1
                if tablica[i][j][k] == "H":
                    tablica_pionkow_bialych[4] += 1
                if tablica[i][j][k] == "K":
                    tablica_pionkow_bialych[5] += 1
    flaga = True
    for i in range(len(tablica_pionkow_czarnych)):
        if tablica_pionkow_czarnych[i] != tablica_pionkow_bialych[i]:
            flaga = False
    if flaga:
        rownowaga+=1
        if sum(tablica_pionkow_bialych)==sum(tablica_pionkow_czarnych):
            suma = sum(tablica_pionkow_bialych) + sum(tablica_pionkow_czarnych)
            if mini_suma == -1:
                mini_suma = suma
            if mini_suma > suma:
                mini_suma = suma

zapis.write(str(rownowaga)+" "+str(mini_suma)+"\n")

zapis.close()
plik.close()