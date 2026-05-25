def zamien_na_liczbe(znak):
    return ord(znak)-55

plik= open('identyfikator.txt', 'r')
zapis= open('wyniki4_1.txt', 'w')

tablica_wagi = [7,3,1]

tablica_numerow = []

tablica_id = []

for linia in plik:
    id = linia.strip()
    tablica_id.append(id)
    wiersz = []
    for i in range(len(id)):
        if i<3:
            wiersz.append(zamien_na_liczbe(id[i]))
        else:
            wiersz.append(int(id[i]))
    tablica_numerow.append(wiersz)

for i in range(len(tablica_numerow)):
    index = 0
    suma = 0
    for j in range(len(tablica_numerow[i])):
        if j!=3:
            suma = suma+tablica_numerow[i][j]*tablica_wagi[index%3]
            index = index + 1

    if suma%10!=tablica_numerow[i][3]:
        zapis.write(tablica_id[i]+"\n")

zapis.close()
plik.close()