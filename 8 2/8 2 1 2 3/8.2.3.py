def zlicz_ilosc_slow(slowa):
    slowo1 = slowa[0]
    slowo2 = slowa[1]
    tablica_slowa1 =[0]*26
    tablica_slowa2 =[0]*26
    for i in range(len(slowo1)):
        tablica_slowa1[ord(slowo1[i])-65]+=1
    for i in range(len(slowo2)):
        tablica_slowa2[ord(slowo2[i])-65]+=1
    if tablica_slowa1 == tablica_slowa2:
        return True
    else:
        return False

plik = open("slowa.txt","r")
zapis = open("wyniki6.txt","w")
zapis.write("c)\n")
licznik = 0
tablica_slow = []
for linia in plik:
    slowo = (linia.strip()).split()
    if zlicz_ilosc_slow(slowo):
        licznik += 1
        tablica_slow.append(slowo)
zapis.write("Liczba par: "+str(licznik)+"\n")

for i in range (0,len(tablica_slow)):
    zapis.write(tablica_slow[i][0]+" "+tablica_slow[i][1]+"\n")


zapis.close()
plik.close()
