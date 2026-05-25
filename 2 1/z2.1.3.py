napis = input()
tablica_napis = []
slowo = ""
for i in range(len(napis)):
    if(napis[i]!=" " ):
        slowo = slowo + napis[i]
    if(napis[i]==" " or i == len(napis)-1):
        tablica_napis.append(slowo)
        slowo=""

slownik = {}

for i in range(len(tablica_napis)):
    if tablica_napis[i] in slownik:
        slownik[tablica_napis[i]] = slownik[tablica_napis[i]]+1
    else:
        slownik[tablica_napis[i]] = 1

maks_wartosc = 0
maks_klucz =""

for klucz in slownik:
    wartosc = slownik[klucz]
    if wartosc > maks_wartosc:
        maks_wartosc = wartosc
        maks_klucz = klucz

print(f"{maks_klucz} {maks_wartosc} ")


