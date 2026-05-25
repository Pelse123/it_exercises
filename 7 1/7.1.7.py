def suma_liczb(wiersz):
    suma = 0
    for i in range(len(wiersz)):
        temp = wiersz[i]
        while temp !=0:
            suma+=temp%10
            temp = temp//10
    return suma

plik = open("liczby.txt","r")
zapis = open("wyniki4.txt","w")

tablica = []
for liczba in plik:
    l1,l2,l3 = liczba.strip().split()
    wiersz = [int(l1),int(l2),int(l3)]
    tablica.append(wiersz)

suma_35_ilosc = 0
maksymalna_suma = 0

for i in range(len(tablica)):
    if suma_liczb(tablica[i]) == 35:
        suma_35_ilosc+=1
    if suma_liczb(tablica[i])>maksymalna_suma:
        maksymalna_suma = suma_liczb(tablica[i])
ilosc_maks = 0
for i in range(len(tablica)):
    if suma_liczb(tablica[i])==maksymalna_suma:
        ilosc_maks+=1

zapis.write("c)\n")

zapis.write(f"liczba wystąpień sumy cyfr równej 35: {suma_35_ilosc}\nnajwiększa suma cyfr w wierszu: {maksymalna_suma}\nliczba wierszy,w których wystąpiła największa suma cyfr w wierszu: {ilosc_maks}\n")


plik.close()
zapis.close()