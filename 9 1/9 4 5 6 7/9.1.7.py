plik= open('instrukcje.txt', 'r')
zapis= open('wyniki4.txt', 'w')
tablica = []
for linia in plik:
    tablica.append(linia.strip().split())
napis =[]
zapis.write("d)\n")
for i in range(len(tablica)):
    instrukcja = tablica[i][0]
    litera = tablica[i][1]
    if instrukcja == "DOPISZ":
        napis.append(litera)
    if instrukcja == "ZMIEN":
        napis[len(napis) - 1] = litera
    if instrukcja == "USUN":
        napis.pop(len(napis) - int(litera))
    if instrukcja == "PRZESUN":
        for i in range(len(napis)):
            if napis[i] == litera:
                napis[i] = chr((ord(napis[i])-ord("A") + 1)%26 + ord("A"))
                break
wynik=""
for i in range(len(napis)):
    if napis[i] != "":
        wynik += napis[i]
zapis.write(str(wynik))
zapis.close()
plik.close()