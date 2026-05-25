def czy_podobne(dzialka1,dzialka2):
    if len(dzialka1) != len(dzialka2):
        return False
    elif len(dzialka1[0]) != len(dzialka1[0]):
        return False
    for i in range(len(dzialka1)):
        for j in range(len(dzialka1[i])):
            if dzialka1[i][j] != dzialka2[len(dzialka2)-1-i][len(dzialka2[0])-1-j]:
                return False
    return True

plik = open("dzialki.txt","r")
zapis = open("wynik4.txt","w")

tablica = []
wiersz = []
for line in plik:
    linia = line.strip()
    if linia != "":
        wiersz.append(linia)
    else:
        tablica.append(wiersz)
        wiersz = []

flaga = True
for i in range(len(tablica)):
    if flaga != True:
        break
    for j in range(len(tablica)):
        if i!=j:
            if czy_podobne(tablica[i],tablica[j]):
                zapis.write(str(i+1)+" "+str(j+1))
                flaga = False


zapis.close()
plik.close()