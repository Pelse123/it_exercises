plik1 = open('dane2_3.txt', 'r')
zapis = open('zadanie2_3.txt', 'w')
tablica = []

for linia in plik1:
    tablica.append(linia.strip())


tablica_maksymalnej_glebokosci = []
for i in range(len(tablica)):
    glebokosc = 0
    maks_glebokosc = 0
    for j in range(len(tablica[i])):
        if tablica[i][j] == '[':
            glebokosc += 1
        elif tablica[i][j] == ']':
            glebokosc -= 1
        if glebokosc>maks_glebokosc:
            maks_glebokosc = glebokosc
    tablica_maksymalnej_glebokosci.append(maks_glebokosc)

for i in range(len(tablica_maksymalnej_glebokosci)):
    zapis.write(str(tablica_maksymalnej_glebokosci[i]) + '\n')


zapis.close()
plik1.close()