def obliczanie_wartosci_funkcji(tab,x):
    wynik = tab[0]
    for i in range(1,len(tab)):
        wynik = x*wynik+tab[i]
    return wynik

def znajdz_miejsce_zerowe_iteracyjnie(a,b,e,tab):
    srodek = (a+b)/2
    if obliczanie_wartosci_funkcji(tab,a) == 0:
        return a
    elif obliczanie_wartosci_funkcji(tab,b) == 0:
        return b
    while abs(b-a)>e:
        if obliczanie_wartosci_funkcji(tab,srodek) == 0:
            return srodek
        if obliczanie_wartosci_funkcji(tab, a) * obliczanie_wartosci_funkcji(tab, srodek) < 0:
            b = srodek
        else:
            a = srodek
        srodek = (a + b) / 2
    return srodek

stopien = int(input())
wspolczynnik = stopien+1
tablica_wspolczynnikow=[]
for i in range(wspolczynnik):
    tablica_wspolczynnikow.append(int(input()))
a= float(input())
b= float(input())
e= float(input())
print(znajdz_miejsce_zerowe_iteracyjnie(a,b,e,tablica_wspolczynnikow))