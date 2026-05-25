plik = open("pogoda.txt", "r")
zapis = open("wyniki1.txt","a")


tablica=[]
do_slownika = ["dzien","temperatura_maksymalna","temperatura_minimalna","opady"]

for linia in plik:
    tablica.append(dict(zip(do_slownika,linia.strip().split(","))))

tablica.sort(key=lambda x: x["temperatura_maksymalna"], reverse=True)

for i in range(len(tablica)):
    zapis.write(tablica[i]["dzien"]+","+tablica[i]["temperatura_maksymalna"]+","+tablica[i]["temperatura_minimalna"]+","+tablica[i]["opady"]+"\n")



zapis.close()
plik.close()
