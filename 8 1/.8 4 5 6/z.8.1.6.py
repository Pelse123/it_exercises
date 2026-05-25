def czy_pierwsza(liczba):
    if liczba<2:
        return False
    else:
        for i in range(2,int(liczba**0.5)+1):
            if liczba%i==0:
                return False
    return True
plik = open("dane.txt","r")
zapis = open("wyniki.txt","w")

tablica = []
zapis.write("c)\n")
for linia in plik:
    tablica.append(int(linia.strip()))

dl_ciagu = 1
start = 0
suma_roznic = 0
max_dl_ciagu = 0
max_start=0
max_suma_roznic = 0
for i in range(1,len(tablica)):
    if tablica[i-1]<tablica[i] and czy_pierwsza(tablica[i]-tablica[i-1]):
        dl_ciagu += 1
        suma_roznic += tablica[i]-tablica[i-1]
    else:
        start = i-dl_ciagu-1
        if max_dl_ciagu < dl_ciagu:
            max_dl_ciagu = dl_ciagu
            max_start = start
            max_suma_roznic = suma_roznic
        dl_ciagu = 0
        suma_roznic = 0

zapis.write(str(tablica[max_start])+"\n")
zapis.write(str(max_dl_ciagu)+"\n")
zapis.write(str(max_suma_roznic)+"\n")


zapis.close()
plik.close()