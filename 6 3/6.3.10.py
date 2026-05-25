plik = open("pogoda.txt", "r")
zapis = open("wyniki1.txt", "w")

tablica=[]
do_slownika = ["dzien","temperatura_maksymalna","temperatura_minimalna","opady"]

tablica_srednich_dnia = []

for linia in plik:
    tablica.append(dict(zip(do_slownika,linia.strip().split(","))))

ilosc_dni = 0
ile_deszczu = 0
for i in range(len(tablica)):
    if float(tablica[i]["opady"]) > 0:
        ilosc_dni += 1
        ile_deszczu += float(tablica[i]["opady"])
zapis.write("Liczba dni deszczowych: " + str(ilosc_dni) + "\nIle deszczuspadło: "+str(ile_deszczu) + "\n")
zapis.close()
plik.close()