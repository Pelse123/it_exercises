def sortowanie_przez_wstawianie(tablica):
    for i in range(1,len(tablica)):
        k = tablica[i]
        j = i
        while j>0 and tablica[j-1]>k:
            tablica[j] = tablica[j-1]
            j -= 1
        tablica[j] = k
    return tablica


plik = open("liczby.txt","r")
zapis = open("wyniki4.txt","w")

tablica = []
for liczba in plik:
    l1,l2,l3 = liczba.strip().split()
    wiersz = [int(l1),int(l2),int(l3)]
    tablica.append(wiersz)
ilosc = 0
for i in range(len(tablica)):
    if list(tablica[i]) == sortowanie_przez_wstawianie(list(tablica[i])):
        ilosc += 1

zapis.write("a) "+str(ilosc)+"\n")

plik.close()
zapis.close()