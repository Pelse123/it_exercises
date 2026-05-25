plik= open('liczby.txt', 'r')
zapis= open('wyniki4.txt', 'w')
licznik = 0
flaga = True
pierwsza_liczba=""
for linia in plik:
    liczba = linia.strip()
    if liczba[0]==liczba[len(liczba)-1]:
        if flaga:
            pierwsza_liczba+=liczba
            flaga=False
        licznik+=1

zapis.write(f"a)\n{licznik}\n{pierwsza_liczba}")

zapis.close()
plik.close()