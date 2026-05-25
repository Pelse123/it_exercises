def odwroc_tablice(tablica):
    odwrocona = []
    for i in range (len(tablica)-1,-1,-1):
        odwrocona.append(tablica[i])
    return odwrocona

ile = int(input())
tab = []
for i in range(ile):
    tab.append(int(input()))
print(odwroc_tablice(tab))