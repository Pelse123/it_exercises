def licz_jedynki_i_zera(liczba):
    tablica=[0,0]
    for i in range(len(liczba)):
        tablica[int(liczba[i])]+=1
    return tablica

plik= open('anagram.txt', 'r')
zapis= open('wyniki3.txt', 'w')
zrownowazona = 0
niezrownowazona = 0
for linia in plik:
    tablica = licz_jedynki_i_zera(linia.strip())
    if tablica[0] == tablica[1]:
        zrownowazona+=1
    if tablica[0] - 1 == tablica[1] or tablica[1] - 1 == tablica[0]:
        niezrownowazona+=1
zapis.write(str(zrownowazona)+"\n")
zapis.write(str(niezrownowazona)+"\n")
zapis.close()
plik.close()