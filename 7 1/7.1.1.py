def czy_pierwsza(liczba):
    if liczba<2:
        return False
    else:
        for i in range(2,int(liczba**(0.5))+1):
            if liczba%i==0:
                return False
    return True


plik = open("liczby_pary.txt","r")
zapis = open("wyniki.txt","w")

tablica=[]
for liczba in plik:
    tablica.append(liczba.strip().split(","))

licznik = 0
for i in range(0,len(tablica)):
    l1 = int(tablica[i][0])
    l2 = int(tablica[i][1])
    suma = l1+l2
    if czy_pierwsza(suma):
        licznik+=1

zapis.write("a) "+str(licznik))

plik.close()
zapis.close()
