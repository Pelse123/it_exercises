plik = open("liczby_pary.txt","r")
zapis = open("wyniki.txt","w")

tablica=[]
for liczba in plik:
    tablica.append(liczba.strip().split(","))

maks_roznica = 0
zapisz_l1 = 0
zapisz_l2 = 0
for i in range(0,len(tablica)):
    l1 = int(tablica[i][0])
    l2 = int(tablica[i][1])
    roznica = l1 - l2
    if roznica > maks_roznica:
        zapisz_l1 = l1
        zapisz_l2 = l2
        maks_roznica = roznica

zapis.write(f"d)\nLiczby: {str(zapisz_l1)} i {str(zapisz_l2)}\nRoznica: {str(maks_roznica)}")

plik.close()
zapis.close()
