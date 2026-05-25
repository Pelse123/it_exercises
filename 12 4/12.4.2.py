

plik = open("dane1_3.txt","r")
zapis = open("zadanie1_3.txt","w")

tablica = [False]
for linia in plik:
    tablica.append(int(linia.strip()))


maks_suma = 0
j_maks = 0
ostatni_element = 0
start=0
for i in range(1,len(tablica)):
    temp_suma = tablica[i]
    aktualne_j = i
    for j in range(i+1,len(tablica)):
        temp_suma += tablica[j]
        if temp_suma > maks_suma:
            ostatni_element = j
            maks_suma = temp_suma
            start = aktualne_j
        if temp_suma<0:
            break



zapis.write(str(start)+"\n"+str(ostatni_element)+"\n")

zapis.close()
plik.close()