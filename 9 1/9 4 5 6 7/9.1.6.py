plik= open('instrukcje.txt', 'r')
zapis= open('wyniki4.txt', 'w')

ilosc_alfabet = [0]*26
tablica = []

for linia in plik:
    literka = linia.strip().split()[1]
    if linia.strip().split()[0] == "DOPISZ":
        tablica.append(linia.strip().split()[1])

for i in range(len(tablica)):
    ilosc_alfabet[ord(tablica[i])-ord("A")]+=1
maks =0
maks_i = 0
for i in range(len(ilosc_alfabet)):
    if ilosc_alfabet[i] >maks:
        maks=ilosc_alfabet[i]
        maks_i=i
maks_i = chr(maks_i+ord('A'))
zapis.write("c)\n")
zapis.write("litera: "+maks_i+"\n")
zapis.write("ile razy dopisywana: "+str(maks)+"\n")


zapis.close()
plik.close()