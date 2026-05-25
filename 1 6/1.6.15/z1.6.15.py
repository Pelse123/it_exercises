def sprawdz_czy_liczba_pierwsza(liczba):
    if(liczba<2):
        return False
    for i in range(2,liczba):
        if(liczba%i==0):
            return False
    return True
plik = open("dane4.txt", "r")
zapis = open("wynik6.txt", "w")
najwieksza_liczba_pierwsza= 0
for liczba in plik:
    if sprawdz_czy_liczba_pierwsza(int(liczba.strip())):
        najmniejsza_liczba_pierwsza =  int(liczba.strip())
        break

for liczba in plik:
    if sprawdz_czy_liczba_pierwsza(int(liczba.strip())):
        if najwieksza_liczba_pierwsza<int(liczba.strip()):
            najwieksza_liczba_pierwsza = int(liczba.strip())
        if najmniejsza_liczba_pierwsza > int(liczba.strip()):
            najmniejsza_liczba_pierwsza = int(liczba.strip())

zapis.write("b)\n")
zapis.write(f"Najwieksza: {najwieksza_liczba_pierwsza}\n")
zapis.write(f"Najmniejsza: {najmniejsza_liczba_pierwsza}\n")

plik.close()
zapis.close()