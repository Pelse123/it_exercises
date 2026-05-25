def czy_wszystkie_liczby_rozne(liczba):
    tablica = []
    for i in range(10):
        tablica.append(str(i))
    for i in range(65,71):
        tablica.append(chr(i))
    licznik_tablicy = [0]*len(tablica)

    for i in range(len(liczba)):
        for j in range(len(tablica)):
            if tablica[j] == liczba[i]:
                licznik_tablicy[j] +=1
                if licznik_tablicy[j]>1:
                    return False
    return True

czy_wszystkie_liczby_rozne("67")
plik = open("liczby_hex.txt","r")
zapis = open("wyniki_hex.txt","w")
licznik = 0
zapis.write("b)\n")
for linia in plik:
    cyfra = linia.strip()
    if czy_wszystkie_liczby_rozne(cyfra):
        zapis.write(cyfra+"\n")

zapis.close()
plik.close()