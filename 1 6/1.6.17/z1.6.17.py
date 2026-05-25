def sprawdz_czy_wieksza(liczba,maks):
    if liczba>maks and liczba%2==0:
        maks=liczba
    return maks
plik = open("liczby.txt", "r")
zapis = open("wynik5.txt", "w")
maks = 0
for liczba in plik:
    maks = sprawdz_czy_wieksza(int(liczba.strip()),maks)
zapis.write(f"a)\n")
zapis.write(f"{maks}")
plik.close()
zapis.close()