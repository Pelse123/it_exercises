
N=int(input())
d = 2
slownik = {}
licznik = 0
while N>=d:
    if N%d==0:
        licznik = licznik+1
        slownik[d]=licznik
        N=N//d
    else:
        d = d+1
        licznik = 0

for i in slownik:
    print(f"{i},{slownik[i]}")


"""N=int(input())
d = 2
tablica=[d]
licznik = 0
tablica_licznik = [licznik]
while N>=d:
    if N%d==0:
        licznik = licznik+1
        tablica_licznik[d-2]=licznik
        N=N//d
    else:
        d = d+1
        licznik = 0
        tablica_licznik.append(licznik)
        tablica.append(d)
print(tablica_licznik)
print(tablica)
print(dict(zip(tablica,tablica_licznik)))
for i in range(len(tablica)):
    if tablica_licznik[i]!=0:
        print(tablica[i],",", tablica_licznik[i])"""