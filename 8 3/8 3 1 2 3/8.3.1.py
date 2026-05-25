def licz_zera_i_jedynki(liczba):
    tablica=[0]*2
    for i in range(len(liczba)):
        tablica[int(liczba[i])]+=1
    if tablica[0]>tablica[1]:
        return True
    return False
plik= open('slowa.txt', 'r')
zapis= open('wynik4.txt', 'w')
licznik = 0
zapis.write("a)\n")
for liczba in plik:
    if licz_zera_i_jedynki(liczba.strip()):
        licznik+=1
zapis.write(str(licznik))
zapis.close()
plik.close()