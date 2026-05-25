def szyfr_vigenere(klucz,slowo):
    wynik = ""
    licznik = 0
    for i in range(len(slowo)):
        if ord(slowo[i])>=ord("A") and ord(slowo[i])<=ord("Z"):
            liczba_klucza = ord(klucz[(licznik)%len(klucz)])-ord("A")
            liczba_slowa = ord(slowo[i])-ord("A")
            wynik += chr(((liczba_klucza+liczba_slowa)%26)+ord("A"))
            licznik += 1
        else:
            wynik += slowo[i]
    return wynik,licznik

plik= open('dokad.txt', 'r')
zapis= open('vigenere_wyniki.txt', 'w')

klucz = "LUBIMYCZYTAC"
linia = plik.readline().strip()
wynik = szyfr_vigenere(klucz,linia)
licznik = wynik[1]
licznik = licznik//len(klucz)
licznik+=1
zapis.write(str(licznik)+"\n")
zapis.write(wynik[0]+"\n")
zapis.close()
plik.close()
