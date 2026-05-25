def odszyfruj_vigenere(klucz,slowo):
    wynik = ""
    licznik = 0
    for i in range(len(slowo)):
        if ord(slowo[i])>=ord("A") and ord(slowo[i])<=ord("Z"):
            liczba_klucza = ord(klucz[(licznik)%len(klucz)])-ord("A")
            liczba_slowa = ord(slowo[i])-ord("A")
            wynik += chr(((liczba_slowa-liczba_klucza)%26)+ord("A"))
            licznik += 1
        else:
            wynik += slowo[i]
    return wynik,licznik

plik= open('szyfr.txt', 'r')
zapis= open('vigenere_wyniki.txt', 'w')


linia = plik.readline().strip()
klucz = plik.readline().strip()
wynik = odszyfruj_vigenere(klucz,linia)
zapis.write(wynik[0]+"\n")
zapis.close()
plik.close()
