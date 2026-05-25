def max_tablicy(tablica):
    maks = 0
    for i in range(len(tablica)):
        if tablica[i] > maks:
            maks = tablica[i]
    return maks

ile = int(input())
tab = []
for i in range(ile):
    tab.append(int(input()))
print(max_tablicy(tab))
