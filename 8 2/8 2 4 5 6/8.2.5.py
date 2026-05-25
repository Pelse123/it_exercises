plik = open("sekwencje.txt","r")
zapis = open("wyniki_alfa.txt","w")

maks_sekwencja_typow = 0
linia_z_max_dlugosciami = ""
for linia in plik:
        dlugosc_czterech_typow = len(set(linia.strip()))
        dlugosc_linii = len(linia.strip())
        if dlugosc_czterech_typow > maks_sekwencja_typow:
            maks_sekwencja_typow = dlugosc_czterech_typow
            linia_z_max_dlugosciami = linia.strip()
            break

zapis.write("2)\n")
zapis.write(linia_z_max_dlugosciami + " " + str(maks_sekwencja_typow))


zapis.close()
plik.close()
