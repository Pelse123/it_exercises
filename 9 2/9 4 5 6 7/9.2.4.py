plik= open('liczby.txt', 'r')
zapis= open('wyniki4.txt', 'w')

pierwszy_wiersz = plik.readline().strip(). split(" ")
drugi_wiersz = plik.readline().strip().split(" ")

licznik = 0
for i in range(len(pierwszy_wiersz)):
    for j in range(len(drugi_wiersz)):
        if int(drugi_wiersz[j])%int(pierwszy_wiersz[i])==0:
            licznik+=1
            break

zapis.write(str(licznik))


zapis.close()
plik.close()