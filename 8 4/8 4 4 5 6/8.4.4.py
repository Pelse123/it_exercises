plik= open('mecz.txt', 'r')
zapis= open('wyniki1.txt', 'w')

linia = plik.readline().strip()

licznik = 0
for i in range(1,len(linia)):
    if linia[i-1]!=linia[i]:
        licznik += 1

zapis.write("a)\n")
zapis.write(str(licznik))

zapis.close()
plik.close()