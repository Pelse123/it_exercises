def najdluzszy_blok_zer(liczba):
    maks_licznik = 0
    licznik = 0
    for i in range(len(liczba)):
        if liczba[i]=="0":
            licznik += 1
        else:
            if licznik > maks_licznik:
                maks_licznik = licznik
            licznik = 0
        if licznik > maks_licznik:
            maks_licznik = licznik
    return maks_licznik

plik= open('slowa.txt', 'r')
zapis= open('wynik4.txt', 'w')

tablica = []
zapis.write("c)\n")
maks_blok = 0

for linia in plik:
    liczba = linia.strip()
    if najdluzszy_blok_zer(liczba)>maks_blok:
        maks_blok = najdluzszy_blok_zer(liczba)
    tablica.append(liczba)

zapis.write(f"Dlugosc najdluzszego bloku: {maks_blok}\n")
zapis.write("Slowa:\n")
for i in range(len(tablica)):
    if najdluzszy_blok_zer(tablica[i])==maks_blok:
        zapis.write(tablica[i]+"\n")

zapis.close()
plik.close()

