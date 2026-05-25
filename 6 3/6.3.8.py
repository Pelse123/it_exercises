plik = open("pogoda.txt", "r")
zapis = open("wyniki1.txt", "w")

tablica=[]
do_slownika = ["dzien","temperatura_maksymalna","temperatura_minimalna","opady"]
for linia in plik:
    tablica.append(dict(zip(do_slownika,linia.strip().split(","))))

maksymalna_temperatura = tablica[0]["temperatura_maksymalna"]
minimalna_temperatura = tablica[0]["temperatura_minimalna"]
maks_dzien = 0
mini_dzien = 0
for i in range(len(tablica)):
    for klucz in tablica[i]:
        wartosc = tablica[i][klucz]
        if klucz == "temperatura_maksymalna":
            if wartosc > maksymalna_temperatura:
                maksymalna_temperatura = wartosc
                maks_dzien = i

        if klucz == "temperatura_minimalna":
            if wartosc<minimalna_temperatura:
                minimalna_temperatura = wartosc
                mini_dzien = i

zapis.write(f'Dzień z najwyższą temperaturą: {tablica[maks_dzien]["dzien"]}\nDzień z najniższą temperaturą: {tablica[mini_dzien]["dzien"]}')

plik.close()
zapis.close()