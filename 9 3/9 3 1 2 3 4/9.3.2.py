def czy_palindrom(wiersz):
    for i in range(len(wiersz)//2):
        if wiersz[i]!=wiersz[len(wiersz)-i-1]:
            return False
    return True

plik = open("dane.txt","r")
zapis = open("wyniki6.txt","w")
tablica_str =[]
for linia in plik:
    wiersz = linia.strip().split()
    tablica_str.append(wiersz)

tablica = []
licznik =0
for i in range(len(tablica_str)):
    wiersz = []
    for j in range(len(tablica_str[i])):
        wiersz.append(int(tablica_str[i][j]))

    if czy_palindrom(wiersz) == False:
        licznik +=1

    tablica.append(wiersz)

zapis.write(f"{licznik}\n")



zapis.close()
plik.close()