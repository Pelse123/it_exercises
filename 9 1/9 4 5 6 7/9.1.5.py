plik= open('instrukcje.txt', 'r')
zapis= open('wyniki4.txt', 'w')

tablica = []
for linia in plik:
    tablica.append(linia.strip().split()[0])

maks_instrukcja=0
maks_dlugosc=0
temp_dl=1
temp_ins=0
for i in range(1,len(tablica)):
    if tablica[i-1]==tablica[i]:
        temp_dl+=1
        temp_ins = tablica[i-1]
    else:
        if temp_dl>maks_dlugosc:
            maks_dlugosc=temp_dl
            maks_instrukcja=temp_ins
        temp_dl=1
zapis.write("b)\n")
zapis.write("rodzaj instrukcji: "+str(maks_instrukcja)+"\n")
zapis.write("dlugosc ciagu: "+str(maks_dlugosc)+"\n")

zapis.close()
plik.close()