def sito_erastotenesa(liczba):
    tablica=[False]*(liczba+1)
    for i in range(2,int(len(tablica)**0.5)+1):
        for j in range(i*i,len(tablica),i):
            tablica[j]=True

    tablica_liczb = []
    for i in range(2,len(tablica)):
        if tablica[i]== False and i%2!=0:
            tablica_liczb.append(i)

    return tablica_liczb


def czy_parzysta(liczba):
    if liczba%2 == 0:
        return True
    else:
        return False


plik = open("dane.txt","r")
zapis = open("wyniki5.txt","w")

tablica_liczb = []
zapis.write("1)\n")

for linia in plik:
    liczba = int(linia.strip().split()[0])
    if liczba>4 and czy_parzysta(liczba):
        tablica_liczb.append(int(liczba))

tablica_sum=[]
for i in range(len(tablica_liczb)):
    tablica_pierwszych = sito_erastotenesa(tablica_liczb[i])
    roznica = -1
    for j in range(len(tablica_pierwszych)):
        for k in range(len(tablica_pierwszych)):
            if tablica_pierwszych[j]+tablica_pierwszych[k]==tablica_liczb[i]:
                if roznica==-1:
                    roznica = abs(tablica_pierwszych[j]-tablica_pierwszych[k])
                    l1 = tablica_pierwszych[j]
                    l2 = tablica_pierwszych[k]
                if roznica>abs(tablica_pierwszych[j]-tablica_pierwszych[k]):
                    roznica = abs(tablica_pierwszych[j] - tablica_pierwszych[k])
                    l1 = tablica_pierwszych[j]
                    l2 = tablica_pierwszych[k]
    wypisz = sorted([l1,l2])
    zapis.write(str(tablica_liczb[i])+" "+str(wypisz[0])+" "+str(wypisz[1])+"\n")


zapis.close()
plik.close()