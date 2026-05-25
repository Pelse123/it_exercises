def licz_srednia(suma,licznik):
    return suma/licznik
plik= open('liczby.txt', 'r')
zapis= open('wyniki4.txt', 'w')

pierwszy_wiersz_str = plik.readline().strip(). split(" ")
pierwszy_wiersz = []
for i in range(len(pierwszy_wiersz_str)):
    pierwszy_wiersz.append(int(pierwszy_wiersz_str[i]))

maks_srednia = 0
maks_ilosc_elementow = 0
maks_i = 0

for i in range(len(pierwszy_wiersz)):
    licznik = 0
    suma = 0
    for j in range(i,len(pierwszy_wiersz)):
        licznik +=1
        suma = suma + pierwszy_wiersz[j]
        if licznik>=50:
            srednia = licz_srednia(suma,licznik)
            if srednia > maks_srednia:
                maks_srednia = srednia
                maks_ilosc_elementow = licznik
                maks_i =pierwszy_wiersz[i]

zapis.write(str(maks_srednia)+" "+str(maks_ilosc_elementow)+" "+str(maks_i))

zapis.close()
plik.close()