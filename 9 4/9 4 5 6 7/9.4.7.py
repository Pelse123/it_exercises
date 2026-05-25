
def znajdz_wieze(plansza,literka):
    index = []
    for i in range(len(plansza)):
        for j in range(len(plansza[i])):
            if plansza[i][j] == literka :
                index.append([i, j])
    return index

def znajdz_krol(plansza,literka):
    for i in range(len(plansza)):
        for j in range(len(plansza[i])):
            if plansza[i][j] == literka:
                return [i, j]
    return -1

def czy_wieza_szachuje_krola(tablica,i_wiezy,j_wiezy,i_krola,j_krola):
    if i_wiezy == i_krola:
        if j_wiezy <j_krola:
            for j in range(j_wiezy+1,j_krola):
                if tablica[i_wiezy][j] != ".":
                    return False
            return True
        else:
            for j in range(j_krola+1,j_wiezy):
                if tablica[i_wiezy][j] != ".":
                    return False
            return True
    elif j_wiezy == j_krola:
        if i_wiezy < i_krola:
            for i in range(i_wiezy + 1, i_krola):
                if tablica[i][j_wiezy] != ".":
                    return False
            return True
        else:
            for i in range(i_krola + 1, i_wiezy):
                if tablica[i][j_wiezy] != ".":
                    return False
            return True
    return False


def podaj_czy_biala_szachuje_czarnego_krola(plansza):
    indexwiezy = znajdz_wieze(plansza,"W")
    indexkrol = znajdz_krol(plansza,"k")

    if len(indexwiezy)==1:
        wieza = indexwiezy[0]
        return czy_wieza_szachuje_krola(plansza,wieza[0],wieza[1],indexkrol[0],indexkrol[1])
    if len(indexwiezy)==2:
        wieza1 = indexwiezy[0]
        wieza2 = indexwiezy[1]
        czy_szach_w1 = czy_wieza_szachuje_krola(plansza,wieza1[0],wieza1[1],indexkrol[0],indexkrol[1])
        czy_szach_w2 = czy_wieza_szachuje_krola(plansza,wieza2[0],wieza2[1],indexkrol[0],indexkrol[1])
        if czy_szach_w1==True:
            return czy_szach_w1
        if czy_szach_w2==True:
            return czy_szach_w2
    return False

def podaj_czy_czarny_szachuje_bialego_krola(plansza):
    indexwiezy = znajdz_wieze(plansza,"w")
    indexkrol = znajdz_krol(plansza,"K")
    if len(indexwiezy)==1:
        wieza = indexwiezy[0]
        return czy_wieza_szachuje_krola(plansza,wieza[0],wieza[1],indexkrol[0],indexkrol[1])
    if len(indexwiezy)==2:
        wieza1 = indexwiezy[0]
        wieza2 = indexwiezy[1]
        czy_szach_w1 = czy_wieza_szachuje_krola(plansza,wieza1[0],wieza1[1],indexkrol[0],indexkrol[1])
        czy_szach_w2 = czy_wieza_szachuje_krola(plansza,wieza2[0],wieza2[1],indexkrol[0],indexkrol[1])
        if czy_szach_w1==True:
            return czy_szach_w1
        if czy_szach_w2==True:
            return czy_szach_w2
    return False

def policz(plansza):
    ile_razy_szach_czarny_krol =0
    ile_razy_szach_bialy_krol =0
    if podaj_czy_czarny_szachuje_bialego_krola(plansza):
        ile_razy_szach_bialy_krol += 1
    if podaj_czy_biala_szachuje_czarnego_krola(plansza):
        ile_razy_szach_czarny_krol += 1
    return ile_razy_szach_czarny_krol, ile_razy_szach_bialy_krol


plik= open('szachy.txt', 'r')
zapis= open('zadanie1_3.txt', 'w')

tablica = []
plansza = []
for linia in plik:
    linia_planszy = linia.strip()
    if linia_planszy != "":
        wiersz = list(linia_planszy)
        plansza.append(wiersz)
    else:
        if plansza:
            tablica.append(plansza)
        plansza = []

if plansza:
    tablica.append(plansza)
print(len(tablica))

bialy_suma= 0
czarny_suma = 0
for i in range(len(tablica)):
    bialy,czarny = policz(tablica[i])
    bialy_suma += bialy
    czarny_suma += czarny


zapis.write(str(bialy_suma)+" "+str(czarny_suma))


zapis.close()
plik.close()