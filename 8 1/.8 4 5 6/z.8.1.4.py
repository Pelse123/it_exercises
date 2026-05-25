plik = open("dane.txt","r")
zapis = open("wyniki.txt","w")

zapis.write("a)\n")

licznik = 0
for line in plik:
    liczba = int(line.strip())
    if liczba%7==0 and liczba%5!=0:
        licznik += 1
zapis.write(str(licznik)+"\n")

zapis.close()
plik.close()