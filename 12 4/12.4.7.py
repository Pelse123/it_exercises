plik1 = open('dane4.txt', 'r')
zapis = open('zadanie4_3.txt', 'w')

x = [False]
for linia in plik1:
    x.append(int(linia.strip()))


maksymalne_i=0
maks_licznik = 0
for i in range(1,len(x)):
    licznik = 0
    for j in range(1,len(x)):
        if x[i]>x[j]:
            if i>j:
                licznik+=1
                if maks_licznik<licznik:
                    maks_licznik = licznik
                    maksymalne_i = i

zapis.write(str(maksymalne_i))

zapis.close()
plik1.close()