def suma_cyfr(liczba):
    suma = 0
    while liczba>0:
        ostatnia_liczba = liczba%10
        suma += ostatnia_liczba
        liczba = liczba//10
    return suma

plik = open("liczby.txt", "r")
zapis = open("wynik5.txt", "w")
suma_liczb = 0
calkowita_suma = 0
tablica = []

for linia in plik:
    suma_liczb = suma_cyfr(int(linia.strip()))
    calkowita_suma += suma_liczb
    if suma_liczb > 30:
        tablica.append(linia.strip())

zapis.write(f"Całkowita suma: {calkowita_suma}\n")

for i in range(len(tablica)):
    zapis.write(f"{tablica[i]}\n")

plik.close()
zapis.close()
