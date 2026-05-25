def podziel_na_kodony(sekwencja):
    ilosc_kodonow = len(sekwencja)//3
    tablica = [""]*ilosc_kodonow

    for i in range(0,len(sekwencja),3):
        tablica[i//3] = sekwencja[i]+sekwencja[i+1]+sekwencja[i+2]

    for i in range(len(tablica)-1):
        if tablica[i] == "TAA" or tablica[i] == "TAG" or tablica[i] == "TGA":
            return False

    if tablica[len(tablica)-1] != "TAA" and tablica[len(tablica)-1] != "TAG" and tablica[len(tablica)-1] != "TGA":
        return False
    return True



plik = open("dna_sekwencje.txt","r")
zapis = open("wyniki_dna.txt","w")
zapis.write("1)\n")
licznik = 0
dlugosc_najkrotszej = -1
for linia in plik:
    if podziel_na_kodony(linia.strip()) == False:
        licznik = licznik + 1
        if dlugosc_najkrotszej == -1:
            dlugosc_najkrotszej = len(linia.strip())
        if len(linia.strip())<dlugosc_najkrotszej:
            dlugosc_najkrotszej = len(linia.strip())
zapis.write(f"{licznik}\n{dlugosc_najkrotszej}\n")
zapis.close()
plik.close()


