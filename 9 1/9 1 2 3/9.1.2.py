def minimum(tablica):
    mini = -1
    for i in range(len(tablica)):
        if mini == -1:
            mini = tablica[i]
        if tablica[i] < mini:
            mini = tablica[i]
    return mini

plik= open('slowa.txt', 'r')
zapis= open('wyniki4_1.txt', 'w')

tablica = []
tablica_wakacje = []
for linia in plik:
    tablica.append(linia.strip())
    wiersz = [0,0,0,0,0,0]
    for i in range(len(linia.strip())):
        if linia.strip()[i] == "w":
            wiersz[0] += 1
        if linia.strip()[i] == "a":
            wiersz[1] += 1
        if linia.strip()[i] == "k":
            wiersz[2] += 1
        if linia.strip()[i] == "c":
            wiersz[3] += 1
        if linia.strip()[i] == "j":
            wiersz[4] += 1
        if linia.strip()[i] == "e":
            wiersz[5] += 1
    wiersz[1]=wiersz[1]//2
    tablica_wakacje.append(wiersz)

for i in range(len(tablica_wakacje)):
    zapis.write(str(minimum(tablica_wakacje[i]))+" ")

zapis.close()
plik.close()
