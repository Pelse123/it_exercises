def czy_pierwsza(liczba):
    if liczba<2:
        return False
    else:
        for i in range(2,int(liczba**0.5)+1):
            if liczba%i==0:
                return False
    return True

plik = open("dane.txt","r")
zapis = open("wyniki4_1.txt","w")
tablica =[]
for line in plik:
    tablica.append(int(line.strip()))

tablica_pierwszych = []
for i in range(len(tablica)):
    if czy_pierwsza(tablica[i]):
        tablica_pierwszych.append(tablica[i])
mini = tablica_pierwszych[0]
maksi = tablica_pierwszych[0]
for i in range(len(tablica_pierwszych)):
    if tablica_pierwszych[i]<mini:
        mini = tablica_pierwszych[i]
    if tablica_pierwszych[i]>maksi:
        maksi = tablica_pierwszych[i]

zapis.write(f"Liczba liczb pierwszych: {len(tablica_pierwszych)}\n")
zapis.write(f"Najwieksza liczba: {maksi}\n")
zapis.write(f"Najmniejsza liczba: {mini}\n")

zapis.close()
plik.close()