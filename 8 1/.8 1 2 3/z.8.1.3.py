def wystepujace_cyfry(liczba):
    liczba = str(liczba)
    tablica =  []
    for i in range(len(liczba)):
        if int(liczba[i]) not in tablica:
            tablica.append(int(liczba[i]))
    return tablica

def sortuj_tablice(tablica):
    for i in range(1,len(tablica)):
        klucz = tablica[i]
        j = i
        while j>0 and tablica[j-1]>klucz:
            tablica[j] = tablica[j-1]
            j-=1
        tablica[j] = klucz
    return tablica

plik = open("dane.txt","r")
zapis = open("wyniki4_3.txt","w")
tablica_numerow = []
for linia in plik:
    tablica_numerow.append(int(linia.strip()))
licznik = 0
for i in range(len(tablica_numerow)):
    liczba1 = sortuj_tablice(wystepujace_cyfry(tablica_numerow[i]))
    for j in range(i+1,len(tablica_numerow)):
        if i != j:
            liczba2= sortuj_tablice(wystepujace_cyfry(tablica_numerow[j]))
            if liczba1==liczba2:
                licznik = licznik+1
zapis.write(str(licznik))
zapis.close()
plik.close()
