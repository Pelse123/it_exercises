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


m_dlugosc = 0
dlugosc= 1
ostatni_indeks = 0
for i in range(1,len(tablica_roznic)):
    if tablica_roznic[i-1]==tablica_roznic[i]:
        dlugosc+=1
        if dlugosc>m_dlugosc:
            m_dlugosc=dlugosc
            ostatni_indeks=i
    else:
        dlugosc=1

zapis.write("b)\n")
zapis.write("Dlugosc: "+str(m_dlugosc+1)+"\n")
zapis.write("Pierwsza wartosc: "+str(tablica[ostatni_indeks-m_dlugosc+1])+"\n")
zapis.write("Ostatnia wartosc: "+str(tablica[ostatni_indeks+1])+"\n")

zapis.close()
plik.close()