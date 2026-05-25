plik = open("dane.txt","r")
zapis = open("wyniki6.txt","w")
tablica_str =[]
for linia in plik:
    wiersz = linia.strip().split()
    tablica_str.append(wiersz)

tablica = []
for i in range(len(tablica_str)):
    wiersz = []
    for j in range(len(tablica_str[i])):
        wiersz.append(int(tablica_str[i][j]))
    tablica.append(wiersz)

tablica_kolumnowa = []
for i in range(len(tablica[0])):
    wiersz = []
    for j in range(len(tablica)):
        wiersz.append(tablica[j][i])
    tablica_kolumnowa.append(wiersz)

max_licznik =0

for i in range(len(tablica_kolumnowa)):
    licznik = 1
    for j in range(1,len(tablica_kolumnowa[i])):
        if tablica_kolumnowa[i][j-1]==tablica_kolumnowa[i][j]:
            licznik = licznik + 1
        else:
            if licznik > max_licznik:
                max_licznik = licznik
            licznik = 1

    if licznik > max_licznik:
        max_licznik = licznik

zapis.write(str(max_licznik))

zapis.close()
plik.close()