def wyszukaj_p(liczba):
    p = 1
    for i in range(len(liczba)):
        if int(liczba[i])>p:
            p = int(liczba[i])
    return p+1


plik= open('dane6.txt', 'r')
zapis= open('zadanie6_1.txt', 'w')
tablica = []
for linia in plik:
    tablica.append(linia.strip())

tablica_ilosci = [0]*9

for i in range(len(tablica)):
    indeks = wyszukaj_p(tablica[i])-2
    tablica_ilosci[indeks]+=1

for i in range(2,11):
    if tablica_ilosci[i-2]!=0:
        zapis.write(f"{i} {tablica_ilosci[i-2]}\n")

zapis.close()
plik.close()