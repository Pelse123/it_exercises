def wyszukaj_binarnie_iteracyjnie(tablica):
    lewy = 0
    prawy = len(tablica)-1
    while lewy<prawy:
        index_srodka = (lewy+prawy)//2
        if tab[index_srodka]>tablica[prawy]:
            lewy = index_srodka+1
        else:
            prawy = index_srodka-1
    return tablica[lewy]
n = int(input())
tab = []
for i in range(n):
    tab.append(int(input()))
print(wyszukaj_binarnie_iteracyjnie(tab))