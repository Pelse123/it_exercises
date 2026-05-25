plik = open("odbiorcy.txt","r")
zapis = open("wyniki4.txt","w")

tablica = [-1]
tablica_stala = [-1]
for linia in plik:
    tablica.append(int(linia.strip()))
    tablica_stala.append(int(linia.strip()))
n = len(tablica)
runda = 1
szukana = 0
flaga = True

while(flaga):
    wynik_tablica = [-1] * n
    for i in range(1,len(tablica)):
        wynik_tablica[i]=tablica[tablica_stala[i]]
        if i == wynik_tablica[i]:
            szukana = i
            flaga = False
            break
    tablica = wynik_tablica
    runda += 1

zapis.write(str(runda) +" "+str(szukana)+"\n")

zapis.close()
plik.close()