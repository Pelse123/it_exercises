
def wyszukaj_binarnie_iteracyjnie(tablica,szukana):
    lewy = 0
    prawy = len(tablica)-1
    while lewy<=prawy:

        index_srodka = (lewy+prawy)//2
        if tab[index_srodka]==szukana:
            return index_srodka
        elif tab[index_srodka]<szukana:
            lewy = index_srodka+1
        else:
            prawy = index_srodka-1

    if abs(tablica[lewy]-szukana)<abs(tablica[prawy]-szukana):
        return tablica[lewy]
    else:
        return tablica[prawy]

n = int(input())
tab = []
for i in range(n):
    tab.append(int(input()))
k = int(input())
print(wyszukaj_binarnie_iteracyjnie(tab,k))