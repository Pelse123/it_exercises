def czy_liczba1_jest_wieksza(liczba1,liczba2):
    cyfra1 = int(liczba1)
    cyfra2 = int(liczba2)
    if cyfra1 > cyfra2:
        return True
    else:
        return False

def czy_ciag1_jest_wiekszy(ciag1,ciag2):
    n = 0
    if len(ciag1)<len(ciag2):
        n=len(ciag1)
    else:
        n=len(ciag2)
    for i in range(n):
        if ord(ciag1[i]) > ord(ciag2[i]):
            return True
        elif ord(ciag1[i]) < ord(ciag2[i]):
            return False
    return True

def suma_kodow_ascii(ciag):
    suma = 0
    for i in range(len(ciag)):
        suma += ord(ciag[i])
    return suma

def sprawdz_czy_wieksza(liczba1,liczba2,ciag1,ciag2):
    wieksza = []
    if czy_liczba1_jest_wieksza(liczba1,liczba2):
        wieksza = [liczba1,ciag1]
    elif czy_ciag1_jest_wiekszy(ciag1,ciag2):
        wieksza = [liczba1,ciag1]
    else:
        wieksza = [liczba2, ciag2]
    return wieksza

plik = open("dane.txt","r")
zapis = open("wyniki5.txt","w")

tablica = []
for linia in plik:
    wiersz = linia.strip().split()
    if int(wiersz[0])==suma_kodow_ascii(wiersz[1]):
        tablica.append(wiersz)

indeks_do_wypisania =0
najwieksza = []

for i in range(1,len(tablica)):
    liczba1 = tablica[i-1][0]
    ciag1 = tablica[i-1][1]
    liczba2 = tablica[i][0]
    ciag2 = tablica[i][1]
    wieksza = sprawdz_czy_wieksza(liczba1,liczba2,ciag1,ciag2)
    if len(najwieksza)==0:
        najwieksza = [liczba1,ciag1]
    najwieksza = sprawdz_czy_wieksza(najwieksza[0],wieksza[0],najwieksza[1],wieksza[1])


zapis.write(najwieksza[0]+" "+najwieksza[1])


zapis.close()
plik.close()