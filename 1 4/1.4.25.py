def suma_sasiadow(tab,n):
    nowa_tablica = []
    for i in range(n-1):
        nowa_tablica.append(tab[i]+tab[i+1])
    return nowa_tablica

n = int(input())
tablica = []

for i in range(n):
    tablica.append(int(input()))
tablica = suma_sasiadow(tablica,n)
for i in range(len(tablica)):
    print(tablica[i],end=" ")