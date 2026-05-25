def czy_pierwsza(l):
    if 2>l:
        return False
    else:
        for i in range(2,l):
            if l%i==0:
                return False
    return True
def wyszukaj_binarnie_iteracyjnie(tablica):
    lewy = 0
    prawy = len(tablica)-1
    wynik = -1
    while lewy<=prawy:
        index_srodka = (lewy+prawy)//2
        if czy_pierwsza(tablica[index_srodka]):
            wynik = tab[index_srodka]
            prawy = index_srodka - 1
        else:
            lewy = index_srodka + 1
    return wynik
n = int(input())
tab = []
for i in range(n):
    tab.append(int(input()))
print(wyszukaj_binarnie_iteracyjnie(tab))
