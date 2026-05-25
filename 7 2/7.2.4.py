def zamien_na_liczbe(liczba):
    if ord(liczba)>=65 and ord(liczba)<=90:
        return ord(liczba)-55
    return int(liczba)

def zamien_na_dziesietny(liczba,system):
    na_dziesietny = 0
    for i in range(len(liczba)-1,-1,-1):
        cyfra = zamien_na_liczbe(liczba[i])
        potega = system**(len(liczba)-i-1)
        na_dziesietny = na_dziesietny + (cyfra * potega)
    return na_dziesietny

def czy_pierwsza(liczba):
    if liczba<2:
        return False
    else:
        for i in range(2,int(liczba**(0.5))+1):
            if liczba%i==0:
                return False
        return True

plik = open("liczby_hex.txt","r")
zapis = open("wyniki_hex.txt","w")
licznik = 0
for linia in plik:
    system_16 = linia.strip()
    dziesietny = zamien_na_dziesietny(system_16,16)
    if czy_pierwsza(dziesietny):
        licznik = licznik + 1

zapis.write("a)\n"+str(licznik))


zapis.close()
plik.close()