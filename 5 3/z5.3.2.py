def wyszukaj_binarnie_rekurencyjnie(tablica,szukana,lewy,prawy):
    while lewy<=prawy:
        index_srodka = (lewy+prawy)//2
        if tab[index_srodka]==szukana:
            return index_srodka
        if tab[index_srodka]<szukana:
            return wyszukaj_binarnie_rekurencyjnie(tab,szukana,index_srodka+1,prawy)
        else:
           return wyszukaj_binarnie_rekurencyjnie(tablica,szukana,lewy,index_srodka-1)
    return -1
n = int(input())
tab = []
for i in range(n):
    tab.append(int(input()))
k = int(input())
lewy = 0
prawy = len(tab) - 1
print(wyszukaj_binarnie_rekurencyjnie(tab,k,lewy,prawy))