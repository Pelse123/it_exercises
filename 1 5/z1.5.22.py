def policz_wiersze(poczatek,koniec,skok):
    lista = []
    ilosc = 0
    for i in range(poczatek,koniec+1,skok):
        lista.append(i)
        ilosc += 1
    return ilosc

def macierz_prostokatna(policz_wiersze,poczatek,skok,koniec):
    macierz = []
    wartosc = poczatek
    for i in range(policz_wiersze//2+1):
        wiersz = []
        for j in range(2):
            if wartosc > koniec:
                break
            else:
                wiersz.append(wartosc)
                wartosc += skok
        macierz.append(wiersz)
    return macierz

def wypisz(macierz):
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            print(macierz[i][j],end=" ")
        print()

poczatek = int(input())
koniec = int(input())
skok = int(input())
ile_wierszy = policz_wiersze(poczatek,koniec,skok)

if ile_wierszy%2 !=0:
    lista = []
    for i in range(poczatek,koniec+1,skok):
        lista.append(i)
    for i in range(len(lista)):
        print(lista[i])
else:
    ile_wierszy = policz_wiersze(poczatek,koniec,skok)
    wypisz(macierz_prostokatna(ile_wierszy,poczatek,skok,koniec))
