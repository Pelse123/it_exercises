def minimalny_i_maksymalny_element(tablica):
    minimum = tablica[0]
    maksimum = tablica[0]
    for i in range(len(tablica)):
        if tablica[i] < minimum:
            minimum = tablica[i]
        if tablica[i] > maksimum:
            maksimum = tablica[i]
    return minimum, maksimum
def sortowanie_kubelkowe(tablica):
    mini, maksi = minimalny_i_maksymalny_element(tab)
    tymczasowa  = [0]*(maksi+1-mini)
    for i in range(len(tablica)):
        tymczasowa[tablica[i]-mini] = tymczasowa[tablica[i]-mini] + 1
    indeks = 0
    for i in range(len(tymczasowa)-1, -1, -1):
        for j in range(tymczasowa[i]):
            tablica[indeks] = i+mini
            indeks = indeks + 1
    return tablica

n = int(input())
tab = []
for i in range(n):
    tab.append(int(input()))
tab = sortowanie_kubelkowe(tab)
for i in range(len(tab)):
    print(tab[i],end=" ")