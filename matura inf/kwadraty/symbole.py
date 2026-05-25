def dodaj_do_macierzy(plik):
    macierz = []
    wiersz = []
    for line in plik:
        for i in line:
            if i != '\n':
                wiersz.append(i)
            else:
                macierz.append(wiersz)
                wiersz = []
    return(macierz)


def sprawdz(kombinacja):
    gwiazdka = [["*","*","*"],
                ["*","*","*"],
                ["*","*","*"]]

    kolko = [["o","o","o"],
             ["o","o","o"],
             ["o","o","o"]]

    plusik = [["+","+","+"],
              ["+","+","+"],
              ["+","+","+"]]
    if kombinacja == gwiazdka:
        return True
    elif kombinacja == plusik:
        return True
    elif kombinacja == kolko:
        return True
    else:
        return False
"""
[i-1][j-1] [i-1][j] [i-1][j+1]
[ i ][j-1] [ i ][j] [ i ][j+1]
[i+1][j-1] [i+1][j] [i+1][j+1]
"""

plik = open('symbole.txt','r')
macierz = dodaj_do_macierzy(plik)
print(macierz)
macierz_indeksow=[]
for i in range(1,len(macierz)-1):
    for j in range(1,len(macierz[i])-1):
        kombinacja = [
            [macierz[i-1][j-1],macierz[i-1][j],macierz[i-1][j+1]],
            [macierz[i][j-1],macierz[i][j],macierz[i][j+1]],
            [macierz[i+1][j-1],macierz[i+1][j],macierz[i+1][j+1]]]
        if sprawdz(kombinacja):
            macierz_indeksow.append([i+1,j+1])
            print(kombinacja)
print(len(macierz_indeksow),macierz_indeksow)




plik.close()