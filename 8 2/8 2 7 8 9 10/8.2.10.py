def czy_cyfra(napis):
    cyfry = ""
    for i in range(len(napis)):
        if ord(napis[i])>=48 and ord(napis[i])<=57:
            cyfry += napis[i]
    if len(cyfry)%2 != 0:
        temp_cyfry = ""
        for i in range(len(cyfry)-1):
            temp_cyfry += cyfry[i]
        cyfry = temp_cyfry

    tablica_grup = []
    for i in range(1,len(cyfry),2):
        grupa = cyfry[i-1]+cyfry[i]
        tablica_grup.append(grupa)

    return tablica_grup

plik= open('napisy.txt', 'r')
zapis= open('wyniki4.txt', 'w')

zapis.write("c)\n")
haslo = ""
licznik_x = 0

for linia in plik:
    napis = linia.strip()
    aktualne_grupy = czy_cyfra(napis)

    if len(aktualne_grupy) != 0:
        aktualne_i = 0
        for i in range(len(aktualne_grupy)):
            if int(aktualne_grupy[i])>=65 and int(aktualne_grupy[i])<=90:
                if chr(int(aktualne_grupy[i])) == "X":
                    licznik_x += 1
                if chr(int(aktualne_grupy[i])) != "X":
                    licznik_x = 0
                if licznik_x == 3:
                    break
                haslo += chr(int(aktualne_grupy[i]))
                aktualne_i += 1

    if licznik_x == 3:
        haslo += chr(int(aktualne_grupy[aktualne_i-1]))
        break

zapis.write(haslo)

zapis.close()
plik.close()
