def wstawianie(tablica):
    dl = len(tablica)
    for i in range(1,dl):
        klucz = tablica[i]
        j = i-1
        while klucz<tablica[j] and j>=0:
            tablica[j+1] = tablica[j]
            j-=1
        tablica[j+1] = klucz

liczba_miejsc = int(input())
tablica = [0]*liczba_miejsc
for i in range(liczba_miejsc):
    tablica[i] = int(input())
wstawianie(tablica)
for i in range(liczba_miejsc):
    print(tablica[i],end=" ")