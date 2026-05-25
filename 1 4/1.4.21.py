def srednia_tablicy(tablica):
    srednia = 0
    for i in range(len(tablica)):
        srednia += tablica[i]
    return srednia/len(tablica)
ile = int(input())
tab = []
for i in range(ile):
    tab.append(int(input()))
print(srednia_tablicy(tab))