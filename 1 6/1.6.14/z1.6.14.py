def sprawdz_czy_liczba_pierwsza(liczba):
    if(liczba<2):
        return False
    for i in range(2,liczba):
        if(liczba%i==0):
            return False
    return True

ilosc_liczb_pierwszych = 0

plik = open("dane4.txt", "r")
zapis = open("wynik6.txt", "w")

for liczba in plik:
    if sprawdz_czy_liczba_pierwsza(int(liczba.strip())):
        ilosc_liczb_pierwszych = ilosc_liczb_pierwszych + 1

zapis.write("a)\n")
zapis.write(f"{ilosc_liczb_pierwszych}\n")

plik.close()
zapis.close()