plik = open("dane4.txt","r")
zapis = open("zadanie4.txt","w")

tablica = []
for linia in plik:
    cyfra = int(linia.strip())
    tablica.append(cyfra)

maks_roznica = 0
roznica = 0
mini_roznica = -1
for i in range(1,len(tablica)):
    roznica = abs(tablica[i]-tablica[i-1])
    if mini_roznica == -1:
        mini_roznica = roznica
    if roznica < mini_roznica:
        mini_roznica = roznica
    if roznica>maks_roznica:
        maks_roznica = roznica

zapis.write("a)\n")
zapis.write(f"Wartosc najwiekszej luki: {maks_roznica}\n")
zapis.write(f"Wartosc najmniejszej luki: {mini_roznica}\n")



zapis.close()
plik.close()