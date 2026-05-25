def ilosc_cyfr(liczba):
    ilosc = 0
    while liczba > 0:
        ilosc += 1
        liczba = liczba//10
    return ilosc


plik = open("liczby_pary.txt","r")
zapis = open("wyniki.txt","w")

tablica=[]
for liczba in plik:
    tablica.append(liczba.strip().split(","))

ilosc = 0
for i in range(0,len(tablica)):
    l1 = int(tablica[i][0])
    l2 = int(tablica[i][1])
    if ilosc_cyfr(l1) == ilosc_cyfr(l2):
        ilosc += 1

zapis.write("b) "+str(ilosc))

plik.close()
zapis.close()
