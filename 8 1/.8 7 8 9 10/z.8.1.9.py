#y%x == 0
#z%y == 0
plik= open('liczby.txt', 'r')
zapis= open('trojki.txt', 'w')
tablica = []
for linia in plik:
    tablica.append(int(linia.strip()))

tablica_trojek = []
for i in range(0,len(tablica)):
    x = tablica[i]
    for j in range(0,len(tablica)):
        y = tablica[j]
        if y%x == 0 and y!=x:
            for k in range(0,len(tablica)):
                z = tablica[k]
                if z%y == 0 and z!=y:
                    wiersz = [x,y,z]
                    tablica_trojek.append(wiersz)

for i in range(0,len(tablica_trojek)):
        zapis.write(f"{str(tablica_trojek[i][0])} {str(tablica_trojek[i][1])} {str(tablica_trojek[i][2])}\n")



zapis.close()
plik.close()