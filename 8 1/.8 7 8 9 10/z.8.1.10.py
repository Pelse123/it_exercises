#w%u == 0
#x%w == 0
#y%x == 0
#z%y == 0
plik= open('liczby.txt', 'r')
zapis= open('wyniki4.txt', 'w')
tablica = []
for linia in plik:
    tablica.append(int(linia.strip()))

licznik = 0
for i in range(0,len(tablica)):
    u = tablica[i]
    for j in range(0,len(tablica)):
        w = tablica[j]
        if w%u == 0 and w!=u:
            for k in range(0,len(tablica)):
                x = tablica[k]
                if x%w == 0 and w!=x:
                    for l in range(0,len(tablica)):
                        y = tablica[l]
                        if y % x == 0 and y != x:
                            for m in range(0, len(tablica)):
                                z = tablica[m]
                                if z % y == 0 and z != y:
                                    licznik += 1
zapis.write("d)\n")
zapis.write(f"{licznik}")

zapis.close()
plik.close()