def rozklad_na_czynniki(liczba):
    l_rozkladana = int(liczba)
    i = 2
    licznik_czynnikow = 0
    licznik_roznych_czynnikow = 0
    while l_rozkladana!=1:
        if l_rozkladana%i == 0:
            licznik_roznych_czynnikow += 1
        while l_rozkladana%i == 0:
            l_rozkladana = l_rozkladana // i
            licznik_czynnikow+=1
        i=i+1
    return [licznik_czynnikow, licznik_roznych_czynnikow]

plik= open('liczby.txt', 'r')
zapis= open('wyniki4.txt', 'w')
maks_czynnikow=0
liczba_maks_czynnikow=""
maks_roznych_czynnikow=0
liczba_maks_roznych_czynnikow=""
for linia in plik:
    liczba = linia.strip()
    if rozklad_na_czynniki(liczba)[0]>maks_czynnikow:
        maks_czynnikow=rozklad_na_czynniki(liczba)[0]
        liczba_maks_czynnikow = liczba

    if rozklad_na_czynniki(liczba)[1]>maks_roznych_czynnikow:
        maks_roznych_czynnikow=rozklad_na_czynniki(liczba)[1]
        liczba_maks_roznych_czynnikow = liczba

zapis.write("b)\n")
zapis.write(f"{liczba_maks_czynnikow}\n{maks_czynnikow}\n{liczba_maks_roznych_czynnikow}\n{maks_roznych_czynnikow}\n")

zapis.close()
plik.close()

