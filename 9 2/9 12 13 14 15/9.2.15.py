
plik= open('dane_ulamki.txt', 'r')
zapis= open('wyniki_ulamki.txt', 'w')

tablica= []
for linia in plik:
       tablica.append(linia.strip().split())
tablica_int = []

for i in range(len(tablica)):
    wiersz =[]
    for j in range(len(tablica[i])):
        wiersz.append(int(tablica[i][j]))
    tablica_int.append(wiersz)

b = (2**2)*(3**2)*(5**2)*(7**2)*13
suma = 0
for i in range(len(tablica_int)):
    suma += (tablica_int[i][0]*b)//tablica_int[i][1]

zapis.write(f"{suma}")


zapis.close()
plik.close()