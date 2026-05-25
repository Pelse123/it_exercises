def wybor(tablica):
    dl = len(tablica)
    for i in range(dl):
        min = i
        for j in range(i+1, dl):
            if tablica[min] < tablica[j]:
               min = j
        tablica[i],tablica[min] = tablica[min], tablica[i]

liczba_miejsc = int(input())
tablica = [0]*liczba_miejsc
for i in range(liczba_miejsc):
    tablica[i] = int(input())
wybor(tablica)
for i in range(liczba_miejsc):
    print(tablica[i],end=" ")