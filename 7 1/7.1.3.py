plik = open("liczby_pary.txt","r")
zapis = open("wyniki.txt","w")

tablica=[]
for liczba in plik:
    tablica.append(liczba.strip().split(","))

ilosc = 0
for i in range(0,len(tablica)):
    l1 = int(tablica[i][0])
    l2 = int(tablica[i][1])
    if l1**2 == l2:
        ilosc += 1

zapis.write("c) "+str(ilosc))

plik.close()
zapis.close()
