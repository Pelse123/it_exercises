def wyszukaj_binarnie_iteracyjnie(tablica):
    lewy = 0
    prawy = len(tablica)-1
    while lewy<prawy:
        index_srodka = (lewy+prawy)//2
        if index_srodka%2!=0:
            index_srodka-=1
        if tablica[index_srodka]==tablica[index_srodka+1]:
            lewy = index_srodka+2
        else:
            prawy = index_srodka

    return tablica[lewy]
n = int(input())
tab = []
for i in range(n):
    tab.append(int(input()))
print(wyszukaj_binarnie_iteracyjnie(tab))