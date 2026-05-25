def zaszyfruj(A,B):
    tablica = []
    for i in range(0,26):
        tablica.append(i)
    for i in range(0,26):
        tablica[i] = ((tablica[i]*A)+B)%26
    return tablica

def zaszyfruj_slowo(klucz,tablica):
    wynik = ""
    for i in range(0, len(tablica)):
        literka = tablica[i]
        literka_na_numer = ord(literka) - ord("a")
        wynik += chr(klucz[literka_na_numer] + ord("a"))
    return wynik

plik= open('probka.txt', 'r')
zapis= open('wyniki.txt', 'w')

slownik = {}
for linia in plik:
    napisy = linia.strip().split(" ")
    slownik[napisy[0]] = napisy[1]


for klucz in slownik:
    wynik_wartosc = [0,0]
    wynik_klucz = [0,0]
    wartosc = slownik[klucz]
    zmieniona_wartosc =klucz
    zamieniony_klucz = wartosc
    flaga_wartosci = True
    flaga_klucza = True
    for i in range(27):
        for j in range(27):
            zmieniona_wartosc = zaszyfruj_slowo(zaszyfruj(i,j),klucz)
            zamieniony_klucz = zaszyfruj_slowo(zaszyfruj(i,j),wartosc)
            if zmieniona_wartosc == wartosc and flaga_wartosci:
                flaga_wartosci = False
                wynik_wartosc[0]=i
                wynik_wartosc[1]=j
            if zamieniony_klucz == klucz and flaga_klucza:
                flaga_klucza = False
                wynik_klucz[0]=i
                wynik_klucz[1]=j
            if flaga_klucza!=True and flaga_wartosci!=True :
                break
        if flaga_klucza!=True and flaga_wartosci!=True :
            zapis.write("("+str(wynik_wartosc[0]) + "," + str(wynik_wartosc[1])+")" + "("+str(wynik_klucz[0]) + "," + str(wynik_klucz[1])+")" +"\n")
            break

zapis.close()
plik.close()
