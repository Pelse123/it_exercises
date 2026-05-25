def czy_pierwsza(liczba):
    if liczba<2:
        return False
    else:
        for i in range(2,int(liczba**(1/2))+1):
            if liczba%i==0:
                return False
    return True

def suma_kodow_ascii(zdanie):
    suma = 0
    for i in range(len(zdanie)):
        suma += ord(zdanie[i])
    return suma

plik = open("napis.txt","r")
zapis = open("zadanie5.txt","w")
licznik = 0
for linia in plik:
    napis = linia.strip()
    if czy_pierwsza(suma_kodow_ascii(napis)):
        licznik += 1

zapis.write("a)\n"+str(licznik) + "\n")

zapis.close()
plik.close()

