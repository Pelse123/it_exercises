plik = open("dane.txt","r")
zapis = open("wyniki6.txt","w")

licznik = 0
for linia in plik:
    cyfra = linia.strip()
    if cyfra[0] == cyfra[len(cyfra)-1]:
        licznik += 1

zapis.write("a) "+str(licznik))

plik.close()
zapis.close()