def zamien_na_2_cyfry(cyf1,cyf2):
    return (cyf1*10)+cyf2

plik= open('pi.txt', 'r')
zapis= open('wyniki3.txt', 'w')

tablica = []
for linia in plik:
    tablica.append(int(linia.strip()))


tablica_ilosc = [0]*100
for i in range(len(tablica)-1):
    numer = zamien_na_2_cyfry(tablica[i],tablica[i+1])
    tablica_ilosc[numer] += 1

mini=-1
maxi =0
minimalny_numer = ""
maksymalny_numer =""
for i in range(len(tablica_ilosc)):
    if mini==-1:
        mini=tablica_ilosc[i]
    if mini>tablica_ilosc[i]:
        mini=tablica_ilosc[i]
        minimalny_numer = str(i)
    if maxi<tablica_ilosc[i]:
        maxi=tablica_ilosc[i]
        maksymalny_numer = str(i)

for i in range(len(tablica_ilosc)):
    if tablica_ilosc[i]==mini:
        minimalny_numer = str(i)
        break

if len(maksymalny_numer)<2:
    maksymalny_numer = "0"+maksymalny_numer
if len(minimalny_numer)<2:
    minimalny_numer = "0"+minimalny_numer

zapis.write(f"{minimalny_numer} {mini}\n{maksymalny_numer} {maxi}")


zapis.close()
plik.close()
