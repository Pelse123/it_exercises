def zaszyfruj(A,B):
    tablica = []
    for i in range(0,26):
        tablica.append(i)
    for i in range(0,26):
        tablica[i] = ((tablica[i]*A)+B)%26
    return tablica

plik= open('tekst.txt', 'r')
zapis= open('wyniki.txt', 'w')

tablica = plik.readline().strip().split(" ")
klucz = zaszyfruj(5,2)

for i in range(len(tablica)):
    if len(tablica[i]) >= 10:
        wynik = ""
        for j in range(0,len(tablica[i])):
            literka = tablica[i][j]
            literka_na_numer = ord(literka)-ord("a")
            wynik+=chr(klucz[literka_na_numer]+ord("a"))
        zapis.write(wynik+"\n")


zapis.close()
plik.close()
