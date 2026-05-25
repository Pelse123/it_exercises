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


plik = open("plansza.txt","r")
zapis = open("wyniki4.txt","w")

plansza =[]
for linia in plik:
    wiersz = []
    for i in range(len(linia.strip())):
        if linia[i].strip()!= "":
            wiersz.append(int(linia[i].strip()))
    plansza.append(wiersz)

zapis.write(str(sprawdz_pola_jednomasztowce(plansza)))

zapis.close()
plik.close()