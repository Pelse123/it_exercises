plik = open("../1.6.13/slowa.txt", "r")
zapis = open("wynik5.txt", "w")
ilosc_wystapien = [0]*12

for line in plik:
    dlugosc_slowa = len(line.strip())
    for i in range(len(ilosc_wystapien)):
        if(dlugosc_slowa-1==i):
            ilosc_wystapien[i] = ilosc_wystapien[i]+1

zapis.write("a)\n")
for i in range(len(ilosc_wystapien)):
    zapis.write(f"{i+1} {ilosc_wystapien[i]}\n")
plik.close()
zapis.close()