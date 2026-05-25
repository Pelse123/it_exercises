def czy_kontrastujacy(i,j,tablica):

    if i!=0 and j!=0 and i!=len(tablica)-1 and j!=len(tablica[i])-1:
        gora = tablica[i-1][j]
        dol = tablica[i+1][j]
        prawo = tablica[i][j+1]
        lewo = tablica[i][j-1]
        roznica_gora = abs(tablica[i][j]-gora)
        roznica_dol = abs(tablica[i][j]-dol)
        roznica_prawo = abs(tablica[i][j]-prawo)
        roznica_lewo = abs(tablica[i][j]-lewo)
        if roznica_lewo>128 or roznica_prawo>128 or roznica_dol>128 or roznica_gora>128:
            return False

    else:
        if i == 0:
            dol = tablica[i + 1][j]
            roznica_dol = abs(tablica[i][j] - dol)
            if j == 0:
                prawo = tablica[i][j + 1]
                roznica_prawo = abs(tablica[i][j] - prawo)
                if roznica_prawo > 128 or roznica_dol > 128:
                    return False
            elif j == len(tablica[i])-1:
                lewo = tablica[i][j-1]
                roznica_lewo = abs(tablica[i][j] - lewo)
                if roznica_lewo > 128 or roznica_dol > 128:
                    return False
            else:
                lewo = tablica[i][j - 1]
                roznica_lewo = abs(tablica[i][j] - lewo)
                prawo = tablica[i][j + 1]
                roznica_prawo = abs(tablica[i][j] - prawo)
                if  roznica_prawo > 128 or roznica_lewo > 128 or roznica_dol > 128:
                    return False
        elif i == len(tablica)-1:
            gora = tablica[i-1][j]
            roznica_gora = abs(tablica[i][j] - gora)
            if j == 0:
                prawo = tablica[i][j + 1]
                roznica_prawo = abs(tablica[i][j] - prawo)
                if roznica_prawo > 128 or roznica_gora > 128:
                    return False
            elif j == len(tablica[i]) - 1:
                lewo = tablica[i][j-1]
                roznica_lewo = abs(tablica[i][j] - lewo)
                if roznica_lewo > 128 or roznica_gora > 128:
                    return False
            else:
                lewo = tablica[i][j - 1]
                roznica_lewo = abs(tablica[i][j] - lewo)
                prawo = tablica[i][j + 1]
                roznica_prawo = abs(tablica[i][j] - prawo)
                if  roznica_prawo > 128 or roznica_lewo > 128 or roznica_gora > 128:
                    return False
        else:
            gora = tablica[i - 1][j]
            dol = tablica[i + 1][j]
            roznica_gora = abs(tablica[i][j] - gora)
            roznica_dol = abs(tablica[i][j] - dol)
            if j == 0:
                prawo = tablica[i][j + 1]
                roznica_prawo = abs(tablica[i][j] - prawo)
                if roznica_prawo > 128 or roznica_dol > 128 or roznica_gora>128:
                    return False
            elif j == len(tablica[i])-1:
                lewo = tablica[i][j-1]
                roznica_lewo = abs(tablica[i][j] - lewo)
                if roznica_lewo > 128 or roznica_dol > 128 or roznica_gora>128:
                    return False
            else:
                lewo = tablica[i][j - 1]
                roznica_lewo = abs(tablica[i][j] - lewo)
                prawo = tablica[i][j + 1]
                roznica_prawo = abs(tablica[i][j] - prawo)
                if  roznica_prawo > 128 or roznica_lewo > 128 or roznica_dol > 128 or roznica_gora>128:
                    return False
    return True

plik = open("dane.txt","r")
zapis = open("wyniki6.txt","w")
tablica_str =[]
for linia in plik:
    wiersz = linia.strip().split()
    tablica_str.append(wiersz)

tablica = []

for i in range(len(tablica_str)):
    wiersz = []
    for j in range(len(tablica_str[i])):
        wiersz.append(int(tablica_str[i][j]))
    tablica.append(wiersz)

licznik = 0
for i in range(len(tablica)):
    for j in range(len(tablica[i])):
        if czy_kontrastujacy(i,j,tablica)==False:
            licznik += 1

zapis.write(str(licznik)+"\n")

zapis.close()
plik.close()