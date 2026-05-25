def babelkowe(tablica):
    dl = len(tablica)
    for i in range(dl):
        flaga = True
        for j in range(dl-1-i):
            if tablica[j] < tablica[j+1]:
                tablica[j], tablica[j+1] = tablica[j+1], tablica[j]
                flaga = False
        if flaga:
            break

liczba_miejsc = int(input())
tablica = [0]*liczba_miejsc
for i in range(liczba_miejsc):
    tablica[i] = int(input())
babelkowe(tablica)
for i in range(liczba_miejsc):
    print(tablica[i],end=" ")