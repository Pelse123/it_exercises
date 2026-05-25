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

def zamien_na_tekst(macierz):
    napis = ""
    for i in range(len(macierz[0])):
        for j in range(len(macierz)):
            napis += macierz[j][i]
    return napis

szyfrogramy_plik = open("szyfrogramy.txt","r")
slowa_plik = open("slowa2.txt","r")
zapis = open("wyniki2.txt","w")

slowa_tablica=[]
for linia in slowa_plik:
    slowa_tablica.append(linia.strip())
szyfrowane_tablica=[]
for linia in szyfrogramy_plik:
    szyfrowane_tablica.append(linia.strip())

tablica_kluczy = []
for i in range(len(slowa_tablica)):
    if slowa_tablica[i] == szyfrowane_tablica[i]:
        tablica_kluczy.append(len(slowa_tablica[i]))
    else:
        for j in range(2,len(slowa_tablica[i])-1):
            if zamien_na_tekst(zamien_na_macierz(slowa_tablica[i],j)) == szyfrowane_tablica[i]:
                tablica_kluczy.append(j)

for i in range(len(tablica_kluczy)):
    zapis.write(str(tablica_kluczy[i])+"\n")

slowa_plik.close()
szyfrogramy_plik.close()
zapis.close()