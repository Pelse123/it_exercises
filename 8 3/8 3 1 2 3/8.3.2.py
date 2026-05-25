def dwa_bloki(slowo):
    if slowo[0]=="1":
        return False
    else:
        slowo1 = ""
        slowo2 = ""
        i = 0
        while i<len(slowo) and slowo[i] == "0":
            slowo1 += slowo[i]
            i+=1
        for j in range(i,len(slowo)):
            slowo2 += slowo[j]
        if len(slowo1)==0 or len(slowo2)==0:
            return False
        for i in range(len(slowo2)):
            if slowo2[i] == "0":
                return False


    return True
plik= open('slowa.txt', 'r')
zapis= open('wynik4.txt', 'w')
licznik = 0
zapis.write("b)\n")
for linia in plik:
    liczba = linia.strip()
    if dwa_bloki(liczba):
        licznik += 1

zapis.write(str(licznik))
zapis.close()
plik.close()