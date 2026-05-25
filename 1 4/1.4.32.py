def suma_lista(tab,n):
    if n == 0:
        return tab[0]
    return suma_lista(tab,n-1) + tab[n]

tablica = []
n = int(input())
for i in range(n):
    tablica.append(int(input()))
print(suma_lista(tablica,n-1))