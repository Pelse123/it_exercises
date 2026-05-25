def sprawdz_czy_liczba_pierwsza(liczba):
    if(liczba<2):
        return False
    for i in range(2,liczba):
        if(liczba%i==0):
            return False
    return True

plik = open("dane4.txt", "r")
zapis = open("wynik6.txt", "w")
tablica_pierwszych = []
for liczba in plik:
    if sprawdz_czy_liczba_pierwsza(int(liczba.strip())):
        tablica_pierwszych.append(int(liczba.strip()))
liczba_par = 0
zapis.write("c)\n")
for i in range(1, len(tablica_pierwszych)):
    if (tablica_pierwszych[i] == tablica_pierwszych[i - 1] - 2 or tablica_pierwszych[i] - 2 == tablica_pierwszych[i - 1]):
        liczba_par += 1
        zapis.write(f"{tablica_pierwszych[i-1]} {tablica_pierwszych[i]}\n")
zapis.write(f"Liczba par: {liczba_par}\n")
plik.close()
zapis.close()