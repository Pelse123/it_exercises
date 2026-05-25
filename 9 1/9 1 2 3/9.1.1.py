plik= open('slowa.txt', 'r')
zapis= open('wyniki4_1.txt', 'w')

tablica = []
tablica_wk = []
for linia in plik:
    tablica.append(linia.strip())
    wiersz = [0,0]
    for i in range(len(linia.strip())):
        if linia.strip()[i] == "w":
            wiersz[0] += 1
        if linia.strip()[i] == "k":
            wiersz[1] += 1
    tablica_wk.append(wiersz)

for i in range(len(tablica)):
    if tablica_wk[i][0] == tablica_wk [i][1]:
        zapis.write(tablica[i]+"\n")


zapis.close()
plik.close()
