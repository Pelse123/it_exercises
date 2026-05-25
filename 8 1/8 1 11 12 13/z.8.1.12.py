def wyszukaj_p(liczba):
    p = 1
    for i in range(len(liczba)):
        if int(liczba[i])>p:
            p = int(liczba[i])
    return p+1

def suma_liczb_liczby(liczba):
    suma = 0
    for i in range(len(liczba)):
        suma += int(liczba[i])
    return suma

plik= open('dane6.txt', 'r')
zapis= open('zadanie6_1.txt', 'w')
tablica = []

for linia in plik:
    tablica.append(linia.strip())
tablica_naj_sumy = [0]*9

for i in range(len(tablica)):
    suma_liczby = suma_liczb_liczby(tablica[i])
    aktualna_suma = suma_liczb_liczby(str(tablica_naj_sumy[wyszukaj_p(tablica[i])-2]))
    if aktualna_suma<suma_liczby:
        tablica_naj_sumy[wyszukaj_p(tablica[i]) - 2] = tablica[i]

for i in range(2,11):
    if int(tablica_naj_sumy[i-2])>0:
        zapis.write(f"{i} {tablica_naj_sumy[i-2]}\n")

zapis.close()
plik.close()