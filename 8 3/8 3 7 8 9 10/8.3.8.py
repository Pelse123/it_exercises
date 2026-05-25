def silnia(n):
    if n == 1 or n == 0:
        return 1
    return n*silnia(n-1)

def licz_jedynki_i_zera(liczba):
    tablica=[0,0]
    for i in range(len(liczba)):
        tablica[int(liczba[i])]+=1
    return tablica

def policz_ilosc(liczba):
    ilosc = licz_jedynki_i_zera(liczba)
    zera = ilosc[0]
    jedynki = ilosc[1]-1
    if jedynki < 0:
        return 0
    return (silnia(zera+jedynki))//(silnia(zera)*silnia(jedynki))

plik= open('anagram.txt', 'r')
zapis= open('wyniki3.txt', 'w')
maks_anagram = 0
tablica = []
zapis.write("b)\n")
for linia in plik:
    liczba = linia.strip()
    if len(liczba) == 8:
        tablica.append(liczba)
        if policz_ilosc(liczba)>maks_anagram:
            maks_anagram = policz_ilosc(liczba)
for i in range(len(tablica)):
    if policz_ilosc(tablica[i])==maks_anagram:
        zapis.write(f"{tablica[i]}\n")

zapis.close()
plik.close()