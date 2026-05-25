plik = open("odbiorcy.txt","r")
zapis = open("wyniki4.txt","w")
tablica = []
tablica_liczb = []
maks = -1
for linia in plik:
    liczba = int(linia.strip())
    tablica_liczb.append(liczba)
    if maks==-1:
        maks=liczba
    if liczba>maks:
        maks=liczba
n = maks
tablica=[0]*(n+1)
tablica_liczb[0]=False

for i in range(len(tablica_liczb)):
    tablica[tablica_liczb[i]] +=1
licznik = 0
for i in range(len(tablica)):
    if tablica[i]==0:
        licznik += 1
zapis.write(str(licznik)+"\n")
plik.close()
zapis.close()

