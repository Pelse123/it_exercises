def roznica(a,b):
    return abs(a-b)

plik = open("dane4.txt","r")
zapis = open("zadanie4.txt","w")

tablica = []
for linia in plik:
    cyfra = int(linia.strip())
    tablica.append(cyfra)

tablica_roznic = []
for i in range(1,len(tablica)):
    roznica_elementow = roznica(tablica[i-1],tablica[i])
    tablica_roznic.append(roznica_elementow)

tablica_niepowtarzalnych_roznic = []
for i in range(len(tablica_roznic)):
    if tablica_roznic[i] not in tablica_niepowtarzalnych_roznic:
        tablica_niepowtarzalnych_roznic.append(tablica_roznic[i])

policz_elementy = [0]*len(tablica_niepowtarzalnych_roznic)
for i in range(len(tablica_niepowtarzalnych_roznic)):
    for j in range(len(tablica_roznic)):
        if tablica_niepowtarzalnych_roznic[i]==tablica_roznic[j]:
            policz_elementy[i] += 1

maksymalny_element = 0
i_maks = 0
for i in range(len(policz_elementy)):
    if policz_elementy[i] > maksymalny_element:
        maksymalny_element = policz_elementy[i]
        i_maks = i

zapis.write("Krotnosc: "+str(maksymalny_element)+"\n")
zapis.write("Najczestsze luki:\n")
for i in range(len(tablica_niepowtarzalnych_roznic)):
    if policz_elementy[i] == maksymalny_element:
        zapis.write(str(tablica_niepowtarzalnych_roznic[i])+"\n")


zapis.close()
plik.close()