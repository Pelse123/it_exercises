def czy_rosnaco_malejacy(cyfry,index_poczatku,index_konca):
    aktualny_index = index_poczatku
    licznik_rosnacych = 0
    licznik_malejacy = 0
    while   index_konca>=aktualny_index+1 and cyfry[aktualny_index] < cyfry[aktualny_index+1]:
        aktualny_index +=1
        licznik_rosnacych+=1

    if  index_konca>=aktualny_index+1  and cyfry[aktualny_index] == cyfry[aktualny_index+1]:
        aktualny_index +=1
        licznik_rosnacych+=1

    while index_konca>=aktualny_index+1 and cyfry[aktualny_index] > cyfry[aktualny_index+1]  :
        aktualny_index +=1
        licznik_malejacy+=1
    if licznik_rosnacych>0 and licznik_malejacy>0 and licznik_rosnacych+licznik_malejacy==5:
        return True
    return False


plik= open('pi.txt', 'r')
zapis= open('wyniki3.txt', 'w')

tablica = []
for linia in plik:
    tablica.append(int(linia.strip()))

licznik =0
for i in range(0,len(tablica)-5):
    if czy_rosnaco_malejacy(tablica,i,i+5):
        licznik+=1

zapis.write(str(licznik))



zapis.close()
plik.close()
