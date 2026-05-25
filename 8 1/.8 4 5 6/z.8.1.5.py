def czy_pierwsza(liczba):
    if liczba<2:
        return False
    else:
        for i in range(2,int(liczba**0.5)+1):
            if liczba%i==0:
                return False
    return True


plik = open("dane.txt","r")
zapis = open("wyniki.txt","w")

zapis.write("b)\n")
for linia in plik:
    suma_liczb = 0
    liczba = linia.strip()
    for i in liczba:
        suma_liczb += int(i)**2
    if czy_pierwsza(suma_liczb):
        zapis.write(str(liczba)+" ")

zapis.close()
plik.close()