plik= open('dane8.txt', 'r')
zapis= open('wyniki8.txt', 'w')

tablica =[]
for linia in plik:
    tablica.append(int(linia.strip()))

licznik=0
zapis.write("b)\n")
for i in range(len(tablica)):
    for j in range(len(tablica)):
        if j!=i:
            if tablica[i]>tablica[j] and i<j:
                licznik+=1
zapis.write(str(licznik))

zapis.close()
plik.close()