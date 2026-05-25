plik = open("dane1_4.txt","r")
zapis = open("zadanie1_4.txt","w")

tablica = [False]
for linia in plik:
    tablica.append(int(linia.strip()))


aktualna_suma = 0
max_suma = -1000000
index_start = 1
tmp_index = 1
index_end = 0
for i in range(1,len(tablica)):
    aktualna_suma += tablica[i]
    if max_suma < aktualna_suma:
        max_suma = aktualna_suma
        index_end = i
        index_start = tmp_index
    if aktualna_suma < 0:
        aktualna_suma = 0
        tmp_index = i+1


zapis.write(str(index_start)+"\n"+str(index_end)+"\n")


zapis.close()
plik.close()