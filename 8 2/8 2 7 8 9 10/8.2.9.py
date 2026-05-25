def czy_palindrom(napis):
    for i in range(len(napis)//2):
        if napis[i] != napis[len(napis)-i-1]:
            return False
    return True

plik= open('napisy.txt', 'r')
zapis= open('wyniki4.txt', 'w')

zapis.write("c)\n")
haslo = ""

for linia in plik:
    napis = linia.strip()
    przypadek1 = napis + napis[0]
    przypadek2 =napis[len(napis)-1] + napis
    if czy_palindrom(przypadek1):
        haslo += przypadek1[(len(przypadek1)-1)//2]
    elif czy_palindrom(przypadek2):
        haslo += przypadek2[(len(przypadek2)-1)//2]

zapis.write(haslo)

zapis.close()
plik.close()
