def zamien_na_dziesietny(liczba,system):
    na_dziesietny = 0
    for i in range(len(liczba)-1,-1,-1):
        cyfra = int(liczba[i])
        potega = system**(len(liczba)-i-1)
        na_dziesietny = na_dziesietny + (cyfra * potega)
    return na_dziesietny

plik = open("dane.txt","r")
zapis = open("wyniki6.txt","w")

licznik = 0
for linia in plik:
    cyfra = linia.strip()
    zamiana_cyfry = str(zamien_na_dziesietny(cyfra,8))
    if zamiana_cyfry[0] == zamiana_cyfry[len(zamiana_cyfry)-1]:
        licznik += 1

zapis.write("b) "+str(licznik))

plik.close()
zapis.close()