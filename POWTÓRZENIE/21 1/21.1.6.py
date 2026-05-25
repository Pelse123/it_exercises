def czy_wiecej_zer(liczba):
    slownik={"0":0,"1":0}
    for i in range(len(liczba)):
        slownik[liczba[i]]+=1
    if slownik["0"]>slownik["1"]:
        return True
    else:
        return False

plik = open("liczby.txt","r")
zapis = open("wynik4.txt","w")

licznik = 0

for linia in plik:
     if czy_wiecej_zer(linia.strip()):
         licznik += 1

zapis.write("1)\n"+str(licznik))


zapis.close()
plik.close()