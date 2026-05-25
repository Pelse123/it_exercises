ile = int(input())
tablica = []
najwieksza = 0
indeksnajwiekszej = 0

for i in range(ile):
    tablica.append(int(input()))

for i in range(ile):
    czypierwsza = True
    if(tablica[i]<2):
        czypierwsza = False
    else:
        for j in range(2,tablica[i]):
            if (tablica[i] % j == 0):
                czypierwsza = False
                break
    if(czypierwsza == True):
        if (tablica[i] > najwieksza):
            najwieksza = tablica[i]
            indeksnajwiekszej = i

if(najwieksza>0):
    print(tablica[indeksnajwiekszej])
else:
    print("brak")


