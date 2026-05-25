def czy_konczy_na_A(slowo):
    if slowo[len(slowo)-1]=="A":
        return True
    return False


plik = open("slowa.txt","r")
zapis = open("wyniki6.txt","w")

licznik = 0

for linia in plik:
    slowo = (linia.strip()).split()
    for i in range(len(slowo)):
        if czy_konczy_na_A(slowo[i]):
            licznik = licznik + 1

zapis.write("a)\n")
zapis.write(str(licznik))

zapis.close()
plik.close()