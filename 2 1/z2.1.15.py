slownik = {}
ilosc = int(input())

tablica_kluczy = []
for i in range(ilosc):
    tablica_kluczy.append(int(input()))

tablica_wartosci=[0]*len(tablica_kluczy)

for i in range(ilosc):
    ile = 0
    for j in range(ilosc):
        if tablica_kluczy[i]>tablica_kluczy[j]:
            ile += 1
    tablica_wartosci[i]= ile

slownik = {}
for i in range(ilosc):
    slownik[tablica_kluczy[i]] = tablica_wartosci[i]

for klucz in slownik:
    print(f"{klucz}: {slownik[klucz]}")
