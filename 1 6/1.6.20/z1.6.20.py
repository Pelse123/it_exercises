def usun_powtorzenia_w_tablicy(tablica):
    tablica_pomocnicza = []

    for i in range(len(tablica)):
        powtorzenie = False
        for j in range(len(tablica_pomocnicza)):
            if tablica[i] == tablica_pomocnicza[j]:
                powtorzenie = True
                break
        if powtorzenie==False:
            tablica_pomocnicza.append(tablica[i])

    return tablica_pomocnicza

plik = open("liczby1.txt", "r")
zapis = open("wyniki1.txt", "w")

tablica_wartosci = []
tablica_bez_powtorzen = []

for linia in plik:
    tablica_wartosci.append(int(linia.strip()))

tablica_bez_powtorzen = usun_powtorzenia_w_tablicy(tablica_wartosci)
tablica_bez_powtorzen.sort()

tablica_powtorzen = [0]*len(tablica_bez_powtorzen)
zapis.write("a)\n")

for i in range(len(tablica_bez_powtorzen)):
    for j in range(len(tablica_wartosci)):
        if(tablica_bez_powtorzen[i] == tablica_wartosci[j]):
            tablica_powtorzen[i] += 1

maks = 0
maks_i = 0
for i in range(len(tablica_powtorzen)):
    if(tablica_powtorzen[i] > maks):
        maks = tablica_powtorzen[i]
        maks_i = i

zapis.write(f"Liczba występująca najczęściej {tablica_bez_powtorzen[maks_i]} \n")

tablica_powtorzen = [0]*len(tablica_bez_powtorzen)

for i in range(len(tablica_bez_powtorzen)):
    for j in range(len(tablica_wartosci)):
        if(tablica_bez_powtorzen[i] == tablica_wartosci[j]):
            tablica_powtorzen[i] += 1
    zapis.write(f"{tablica_bez_powtorzen[i]} {tablica_powtorzen[i]}\n")

plik.close()
zapis.close()