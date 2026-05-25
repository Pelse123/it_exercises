plik = open("liczby.txt","r")
zapis = open("wynik4.txt","w")
maksymalna = 0
minimalna = 0
tablica_liczb = []
for liczba_2 in plik:
    tablica_liczb.append(int(liczba_2,2))
zapis.write("3)\n")

for i in range(len(tablica_liczb)):
    if tablica_liczb[i] == max(tablica_liczb):
        maksymalna = i+1
    if tablica_liczb[i] == min(tablica_liczb):
        minimalna = i+1
    if maksymalna>0 and minimalna>0:
        break

zapis.write(f"Maksymalna:{maksymalna}\nMinimalna:{minimalna}\n")

zapis.close()
plik.close()