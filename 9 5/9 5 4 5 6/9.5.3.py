def policz_wystapienia(linia):
    tablica=[0]*26
    for i in range(len(linia)):
        if ord(linia[i])>=ord("A") and ord(linia[i])<=ord("Z"):
            tablica[ord(linia[i])-ord("A")]+=1
    return tablica


plik= open('szyfr.txt', 'r')
zapis= open('vigenere_wyniki.txt', 'w')
linia = plik.readline().strip()
klucz = plik.readline().strip()
tablica_wystapien = policz_wystapienia(linia)
n = 0
k0 = 0
for i in range(len(tablica_wystapien)):
    k0 += tablica_wystapien[i]*(tablica_wystapien[i] - 1)
    n += tablica_wystapien[i]
    zapis.write(f"{chr(i+ord('A'))}:{tablica_wystapien[i]}\n")
k0 = k0/(n*(n-1))
d = (0.0285/(k0-0.0385))
zapis.write(f"szacunkowa dlugosc: {round(d,2)}\n")
zapis.write(f"dokladna dlugosc: {len(klucz)}\n")
zapis.close()
plik.close()