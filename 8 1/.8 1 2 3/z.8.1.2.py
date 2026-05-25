def czy_palindrom(liczba):
    napis = str(liczba)
    odwrocony = ""
    for i in range(len(napis)-1, -1, -1):
        odwrocony += napis[i]
    if napis == odwrocony:
        return True
    else:
        i = 0
        nowy = odwrocony
        while odwrocony[i] == "0":
            nowy = nowy+"0"
            i += 1
        for i in range(len(nowy)//2):
            if nowy[i]!=nowy[len(nowy)-1-i]:
                return False
        return True
def zamien_na_binarna(liczba):
    binarna = ""
    while(liczba != 0):
        binarna = str(liczba%2) + binarna
        liczba = liczba // 2
    return int(binarna)


plik = open("dane.txt","r")
zapis = open("wyniki4_2.txt","w")

licznik = 0
for linia in plik:
    liczba = int(linia.strip())
    if czy_palindrom(zamien_na_binarna(liczba)):
        licznik += 1
zapis.write(str(licznik))

zapis.close()
plik.close()
