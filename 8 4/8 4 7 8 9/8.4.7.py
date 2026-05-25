plik= open('identyfikator.txt', 'r')
zapis= open('wyniki4_1.txt', 'w')

maks_id = ""
maks_suma = 0
tablica_danych =[]
for linia in plik:
    suma = 0
    id = linia.strip()
    tablica_danych.append(id)
    for i in range(3,len(id)):
        suma += int(id[i])
    if suma > maks_suma:
        maks_suma = suma

tablica_najwiekszych_sum = []
for i in range(0,len(tablica_danych)):
    suma = 0
    for j in range(3,len(tablica_danych[i])):
        suma += int(tablica_danych[i][j])
    if suma == maks_suma:
        tablica_najwiekszych_sum.append(tablica_danych[i])

for i in range(len(tablica_najwiekszych_sum)):
    zapis.write(tablica_najwiekszych_sum[i]+"\n")

zapis.close()
plik.close()