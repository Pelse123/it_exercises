plik= open('tekst.txt', 'r')
zapis= open('wyniki.txt', 'w')

tablica = plik.readline().strip().split(" ")

for i in range(len(tablica)):
    if tablica[i][len(tablica[i]) - 1] == 'd' and tablica[i][0] == 'd':
        zapis.write(tablica[i] + '\n')

zapis.close()
plik.close()
