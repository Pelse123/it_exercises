def sprawdz_czy_slowo_jest(tablica_slow):
    slowo1 = tablica_slow[0]
    slowo2 = tablica_slow[1]
    if len(slowo1) > len(slowo2):
        return False
    else:
        j = 0
        i = 0
        while i != len(slowo2)-len(slowo1)+1:
            if slowo1[j] == slowo2[i+j]:
                j+=1
            else:
                j = 0
                i+=1
            if j == len(slowo1):
                return True

        return False


plik = open("slowa.txt","r")
zapis = open("wyniki6.txt","w")

zapis.write("b)\n")
licznik = 0
for linia in plik:
    slowa = (linia.strip()).split()
    if sprawdz_czy_slowo_jest(slowa):
        licznik = licznik + 1

zapis.write(f"{licznik}\n")

zapis.close()
plik.close()