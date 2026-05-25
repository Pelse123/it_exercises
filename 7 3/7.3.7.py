def zamien_na_macierz(slowo,klucz):
    if len(slowo)%klucz!=0:
        petla = int(len(slowo)/klucz)+1
    else:
        petla = len(slowo)//klucz
    macierz = []
    index = 0
    for i in range(petla):
        wiersz = []
        for j in range(klucz):
            if index != len(slowo):
                wiersz.append(slowo[index])
                index=index+1
            else:
                wiersz.append("")
        macierz.append(wiersz)
    return macierz


slowa_plik = open("slowa1.txt","r")
klucze_plik = open("klucze1.txt","r")
zapis = open("wyniki1.txt","w")
slowa_tablica=[]

for linia in slowa_plik:
    slowa_tablica.append(linia.strip())
klucze_tablica=[]
for linia in klucze_plik:
    klucze_tablica.append(linia.strip())

for i in range(len(slowa_tablica)):
    macierz = zamien_na_macierz(slowa_tablica[i],int(klucze_tablica[i]))
    for j in range(len(macierz[0])):
        for k in range(len(macierz)):
            zapis.write(macierz[k][j])
    zapis.write("\n")

slowa_plik.close()
klucze_plik.close()
zapis.close()