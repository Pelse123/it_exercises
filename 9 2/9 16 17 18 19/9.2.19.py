def czy_rosnaco_malejacy(cyfry,index_poczatku):
    aktualny_index = index_poczatku
    licznik_rosnacych = 0
    licznik_malejacy = 0
    while   len(cyfry)>=aktualny_index+1 and cyfry[aktualny_index] < cyfry[aktualny_index+1]:
        aktualny_index +=1
        licznik_rosnacych+=1

    if  len(cyfry)>=aktualny_index+1  and cyfry[aktualny_index] == cyfry[aktualny_index+1]:
        aktualny_index +=1
        licznik_rosnacych+=1

    while len(cyfry)>=aktualny_index+1 and cyfry[aktualny_index] > cyfry[aktualny_index+1]  :
        aktualny_index +=1
        licznik_malejacy+=1
    if licznik_rosnacych>0 and licznik_malejacy>0:
        return index_poczatku+licznik_rosnacych+licznik_malejacy
    return -1


plik= open('pi.txt', 'r')
zapis= open('wyniki3.txt', 'w')

tablica = []
for linia in plik:
    tablica.append(int(linia.strip()))

max_dlugosc = 0
max_i= 0
max_k = 0
for i in range(0,len(tablica)-4):
    indexPoczatku = i
    indexKonca = czy_rosnaco_malejacy(tablica,indexPoczatku)
    dl = indexKonca - indexPoczatku
    if max_dlugosc <dl:
        max_dlugosc = dl
        max_i = i
        max_k = indexKonca
zapis.write(str(max_i+1) +"\n")
for i in range(max_i,max_k+1):
    zapis.write(str(tablica[i]) + "")


zapis.close()
plik.close()
