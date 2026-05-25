def nwd(a,b):
    if b==0:
        return a
    else:
        return nwd(b,a%b)

plik = open("liczby.txt","r")
zapis = open("wyniki4.txt","w")

tablica = []
for liczba in plik:
    l1,l2,l3 = liczba.strip().split()
    wiersz = [int(l1),int(l2),int(l3)]
    tablica.append(wiersz)

zapis.write("b)\n")
suma = 0
for i in range(len(tablica)):
    suma = suma + nwd(nwd(tablica[i][0],tablica[i][1]),tablica[i][2])

zapis.write(str(suma)+"\n")



plik.close()
zapis.close()