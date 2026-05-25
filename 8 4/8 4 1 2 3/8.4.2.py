def liczby_wystepujace_wiecej(ciag):
    unikalne =[]
    for i in range(len(ciag)):
        if ciag[i] not in unikalne:
         unikalne.append(ciag[i])
    ilosc = [0]*len(unikalne)
    for i in range(len(ciag)):
        for j in range(len(unikalne)):
            if unikalne[j] == ciag[i]:
                ilosc[j] += 1
    wiecej_niz_1=[]
    for i in range(len(unikalne)):
        if ilosc[i] > 1:
            wiecej_niz_1.append(unikalne[i])

    wynik = ""
    for i in range(len(ciag)):
        if ciag[i] in wiecej_niz_1:
            wynik += ciag[i]
        else:
            wynik += " "
    return wynik

def wyznacz_ciag(ciag):
    usun_niewystepujace_wiecej = liczby_wystepujace_wiecej(ciag)
    maks_dl = 0
    koniec = 0
    dl = 0
    for i in range(len(usun_niewystepujace_wiecej)):

        if usun_niewystepujace_wiecej[i] != " ":
            dl +=1
            if maks_dl <= dl:
                maks_dl = dl
                koniec = i
        else:
            dl = 0
    start = koniec-maks_dl+1
    wynik = ""
    for i in range(start,koniec+1):
        wynik+=usun_niewystepujace_wiecej[i]
    return wynik


plik = open("dane.txt","r")
zapis = open("wyniki5.txt","w")

tablica_ciagow = []
for linia in plik:
    ciag =linia.strip().split()[1]
    tablica_ciagow.append(ciag)

for i in range(len(tablica_ciagow)):
    wynik = wyznacz_ciag(tablica_ciagow[i])
    if len(wynik)!=0:
        zapis.write(wynik+" "+str(len(wynik))+"\n")

zapis.close()
plik.close()