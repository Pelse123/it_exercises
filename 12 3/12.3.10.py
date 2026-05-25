def najczesciej_powtarzajaca_sie(tablica):
    unikalna_tablica = list(set(tablica))
    licznik_elementow = [0]*len(unikalna_tablica)

    for i in range(len(unikalna_tablica)):
        for j in range(len(tablica)):
            if unikalna_tablica[i] == tablica[j]:
                licznik_elementow[i] += 1

    maks=0

    for i in range(len(licznik_elementow)):
        if licznik_elementow[i] > maks:
            maks = licznik_elementow[i]

    return maks


plik = open("odbiorcy.txt","r")
zapis = open("wyniki4.txt","w")

tablica = [-1]
tablica_stala = [-1]
for linia in plik:
    tablica.append(int(linia.strip()))
    tablica_stala.append(int(linia.strip()))
n = len(tablica)
runda = 1
flaga = True
rundy_do_sprawdzenia = [1,2,4,8]

while runda<=8:

    if runda in rundy_do_sprawdzenia:
        zapis.write(str(najczesciej_powtarzajaca_sie(tablica))+" ")

    wynik_tablica = [-1] * n

    for i in range(1,len(tablica)):
        wynik_tablica[i]=tablica[tablica_stala[i]]

    tablica = wynik_tablica

    runda += 1

zapis.write("\n")

zapis.close()
plik.close()