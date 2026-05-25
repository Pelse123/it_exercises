slownik = {}
ilosc = int(input())

tablica_wartosci= []
for i in range(ilosc):
    tablica_wartosci.append(int(input()))

for i in range(ilosc):
    klucz = tablica_wartosci[i]
    if klucz in slownik:
        slownik[klucz].append(i)
    else:
        slownik[klucz] = [i]

for klucz in slownik:
    print(f"{klucz}: {slownik[klucz]}")