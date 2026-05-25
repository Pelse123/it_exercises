def sprawdz_pola_jednomasztowce(plansza):
    """
    [i-1][j-1]  [i-1][j]  [i-1][j+1]
    [i][j-1]     [i][j]     [i][j+1]
    [i+1][j-1]  [i+1][j]  [i+1][j+1]
    """
    licznik = 0
    for i in range(len(plansza)):
        for j in range(len(plansza[i])):
            if plansza[i][j] == 1:
                continue
            tablica = [
                [i - 1,j - 1], [i - 1,j], [i - 1,j + 1],
                [i,j - 1],      [i,j],        [i,j + 1],
                [i + 1,j - 1], [i + 1,j], [i + 1,j + 1]
            ]
            flaga = True
            for k in range(len(tablica)):
                ki = tablica[k][0]
                kj = tablica[k][1]
                if (ki<0 or kj<0):
                    continue
                if (ki>= len(plansza) or kj>= len(plansza[i])):
                    continue
                if ki==i and kj==j:
                    continue
                if plansza[ki][kj]==1:
                    flaga = False
            if flaga:
                licznik += 1
    return licznik

def sprawdz_czy_jednomasztowiec(i,j,plansza):
    tablica = [
        [i - 1, j - 1], [i - 1, j], [i - 1, j + 1],
        [i, j - 1], [i, j], [i, j + 1],
        [i + 1, j - 1], [i + 1, j], [i + 1, j + 1]
    ]
    for k in range(len(tablica)):
        ki = tablica[k][0]
        kj = tablica[k][1]
        if (ki < 0 or kj < 0):
            continue
        if (ki >= len(plansza) or kj >= len(plansza[i])):
            continue
        if ki == i and kj == j:
            continue
        if plansza[ki][kj] == 1:
            return False
    return True


def symetrycznie(plansza):
    licznik = 0
    for i in range(len(plansza)):
        for j in range(len(plansza[i])):
            if  plansza[i][j] == 1  and sprawdz_czy_jednomasztowiec(i,j,plansza) and plansza[i][j] == plansza[j][i] and i!=j:
                licznik += 1
    return licznik//2

def czy_dwumasztowiec(i,j,plansza):
    if plansza[i][j] == 1:
        if sprawdz_czy_jednomasztowiec(i,j,plansza)==False:
            return True
        else:
            return False
    else:
        return False

def ile_na_przekatnych(plansza):
    jednomasztowce = 0
    dwumasztowce = 0
    dodane=[]
    for i in range(len(plansza)):
        if plansza[i][i]==1 and i!=len(plansza[0])-1-i:
            if i not in dodane:
                dodane.append(i)
                if sprawdz_czy_jednomasztowiec(i,i,plansza):
                    jednomasztowce += 1
                else:
                    dwumasztowce += 1
    for i in range(len(plansza)):
        if plansza[i][len(plansza[0])-1-i]==1 and i!=len(plansza[0])-1-i:
            if (len(plansza[0])-1-i) not in dodane:
                dodane.append(len(plansza[0])-1-i)
                if sprawdz_czy_jednomasztowiec(i,len(plansza[0])-1-i,plansza):
                    jednomasztowce += 1
                else:
                    dwumasztowce += 1
    return jednomasztowce,dwumasztowce


plik = open("plansza.txt","r")
zapis = open("wyniki4.txt","w")

plansza =[]
for linia in plik:
    wiersz = []
    for i in range(len(linia.strip())):
        if linia[i].strip()!= "":
            wiersz.append(int(linia[i].strip()))
    plansza.append(wiersz)


zapis.write(str(ile_na_przekatnych(plansza)[0])+"\n" +str(ile_na_przekatnych(plansza)[1])+"\n")

zapis.close()
plik.close()