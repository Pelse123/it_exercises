def binarny_na_dziesietny(linia):
    wynik = 0
    for i in range(len(linia)):
        wynik += int(linia[i])*2**(len(linia)-i-1)
    return wynik

def czy_jest_0(linia):
    for i in range(len(linia)):
        if linia[i] == "0":
            return False
    return True

def suma_cyfr(linia):
    suma = 0
    cyfry_bez_pow = list(set(linia))
    for i in range(len(cyfry_bez_pow)):
        suma += int(cyfry_bez_pow[i])
    return suma

plik= open('anagram.txt', 'r')
zapis= open('wyniki3.txt', 'w')

najwieksza_suma = 0
licznik_bez_0=0
liczba_sumy = ""
for linia in plik:
    if czy_jest_0(str(binarny_na_dziesietny(linia.strip()))):
        licznik_bez_0 += 1
    suma = suma_cyfr(str(binarny_na_dziesietny(linia.strip())))
    if suma > najwieksza_suma:
        najwieksza_suma = suma
        liczba_sumy = linia.strip()
zapis.write("d)\n"+str(licznik_bez_0)+"\n"+str(binarny_na_dziesietny(liczba_sumy))+"\n")
plik.close()
zapis.close()
plik.close()