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

maks = 0
min = -1
for i in range(len(tablica)):
    for j in range(len(tablica[i])):
        if min == -1:
            min = tablica[i][j]
        if tablica[i][j] < min:
            min = tablica[i][j]
        if tablica[i][j] > maks:
            maks = tablica[i][j]

zapis.write(f"a)\nNajjasniejszy piksel:{maks}\nNajciemniejszy piksel:{min}\n")

zapis.close()
plik.close()