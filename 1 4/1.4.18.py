def usun_duplikaty(tablica):
    unikaty = []

    for i in range (len(tablica)):
        czy_unikaty = True
        for j in range (i):
            if tablica[i] == tablica[j]:
                czy_unikaty = False
                break
        if czy_unikaty:
            unikaty.append(tablica[i])
    return unikaty


ile = int(input())
tab = []
for i in range(ile):
    tab.append(int(input()))
print(usun_duplikaty(tab))