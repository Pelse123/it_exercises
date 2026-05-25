import statistics

plik = open("pogoda.txt", "r")
zapis = open("wyniki1.txt", "w")

tablica=[]
do_slownika = ["dzien","temperatura_maksymalna","temperatura_minimalna","opady"]

tablica_srednich_dnia = []

for linia in plik:
    tablica.append(dict(zip(do_slownika,linia.strip().split(","))))

for i in range(len(tablica)):
    tablica_srednich_dnia.append((float(tablica[i]["temperatura_maksymalna"])+float(tablica[i]["temperatura_minimalna"]))/2)

zapis.write(str(round(statistics.mean(tablica_srednich_dnia),2)))

zapis.close()
plik.close()