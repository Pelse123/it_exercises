def NWD(a,b):
    if b<=0:
        return a
    return NWD(b,a%b)

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

licznik = 0
for i in range(len(tablica_int)):
    if NWD(tablica_int[i][0],tablica_int[i][1])==1:
        licznik += 1

zapis.write(str(licznik))

zapis.close()
plik.close()