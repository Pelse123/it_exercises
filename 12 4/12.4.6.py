plik1 = open('dane2_4.txt', 'r')
zapis = open('zadanie2_4.txt', 'w')

tablica = []
for line in plik1:
    tablica.append(line.strip())
for i in range(len(tablica)):
    ilosc_nawiasow = [0]*2
    for j in range(len(tablica[i])):
        if tablica[i][j]=="[":
            ilosc_nawiasow[0] +=1
        elif tablica[i][j]=="]":
            ilosc_nawiasow[1] +=1
    if ilosc_nawiasow[0]==ilosc_nawiasow[1]:
        zapis.write("tak\n")
    else:
        zapis.write("nie\n")



zapis.close()
plik1.close()