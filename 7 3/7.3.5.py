def czy_kolejne_wieksze(napis):
    for i in range(1,len(napis)):
        if ord(napis[i]) <= ord(napis[i-1]):
            return False
    return True

plik = open("napis.txt","r")
zapis = open("zadanie5.txt","w")

zapis.write("b)\n")
for linia in plik:
    linijka = linia.strip()
    if czy_kolejne_wieksze(linijka):
        zapis.write(linijka+"\n")


zapis.close()
plik.close()

