def sortowanie(tablica):
    for i in range(1,len(tablica)):
        klucz = tablica[i]
        j = i-1
        while j>=0 and tablica[j]<klucz:
            tablica[j+1] = tablica[j]
            j -= 1
        tablica[j+1]=klucz
    return tablica

plik= open('liczby.txt', 'r')
zapis= open('wyniki4.txt', 'w')
pierwszy_wiersz = plik.readline().strip().split(" ")
wiersz_int =[]
for i in range(len(pierwszy_wiersz)):
    wiersz_int.append(int(pierwszy_wiersz[i]))
posortowany = sortowanie(wiersz_int)
zapis.write(str(posortowany[102]))

zapis.close()
plik.close()