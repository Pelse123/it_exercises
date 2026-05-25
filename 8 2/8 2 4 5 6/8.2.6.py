def czy_komplementarny(nukleotyd):
    for i in range(1,len(nukleotyd)):
        if nukleotyd[i-1] == "A" and (nukleotyd[i] != "T" and nukleotyd[i] != "A"):
            return False
        if nukleotyd[i-1] == "T" and (nukleotyd[i] != "T" and nukleotyd[i] != "A"):
            return False
        if nukleotyd[i-1] == "C" and (nukleotyd[i] != "G" and nukleotyd[i] != "C"):
            return False
        if nukleotyd[i-1] == "G" and (nukleotyd[i] != "C" and nukleotyd[i] != "G"):
            return False
    return True

plik = open("sekwencje.txt","r")
zapis = open("wyniki_alfa.txt","w")
zapis.write("3)\n")
for linia in plik:
    if czy_komplementarny(linia.strip()):
        zapis.write(linia.strip()+"\n")

zapis.close()
plik.close()
