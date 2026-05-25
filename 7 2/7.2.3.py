def spelnia_warunek_osemkowy(liczba):
    for i in range(1,len(liczba)):
        if int(liczba[i-1])>int(liczba[i]):
            return False
    return True

plik = open("dane.txt","r")
zapis = open("wyniki6.txt","w")

licznik = 0
tablica = []
for linia in plik:
    cyfra = linia.strip()
    if spelnia_warunek_osemkowy(cyfra):
        licznik += 1
        tablica.append(cyfra)

maks = 0
mini = int(tablica[0])
for i in range(len(tablica)):
    if int(tablica[i])<mini:
        mini = int(tablica[i])
    if int(tablica[i])>maks:
        maks = int(tablica[i])


zapis.write(f"c)\nLiczba liczb:{str(licznik)}\nNajwieksza:{str(maks)}\nNajmniejsza:{str(mini)}\n")

plik.close()
zapis.close()