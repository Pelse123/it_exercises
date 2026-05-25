def czy_pierwsza(liczba):
    if(liczba < 2):
        return False
    else:
        for i in range(2,liczba):
            if(liczba % i == 0):
                return False
    return True

plik = open("liczby1.txt", "r")
zapis = open("wyniki1.txt", "w")

zapis.write("b)\n")
for linia in plik:
    if(czy_pierwsza(int(linia.strip()))):
        zapis.write(linia)

zapis.close()
plik.close()