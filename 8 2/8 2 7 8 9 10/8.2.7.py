#ascii 48-57 0-9
def ile_cyfr_w_napisie(napis):
    licznik = 0
    for i in range(len(napis)):
        if ord(napis[i])>=48 and ord(napis[i])<=57:
            licznik += 1
    return licznik

plik= open('napisy.txt', 'r')
zapis= open('wyniki4.txt', 'w')
ogolny_licznik = 0
for linia in plik:
    ogolny_licznik += ile_cyfr_w_napisie(linia.strip())

zapis.write("a)\n")
zapis.write(str(ogolny_licznik))

zapis.close()
plik.close()
