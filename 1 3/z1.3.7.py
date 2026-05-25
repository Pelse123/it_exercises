ile = int(input())
tablica = []
ilosczer = 0

for i in range(ile):
    dodaj = int(input())
    if(dodaj == 0):
        ilosczer = ilosczer + 1
    else:
        tablica.append(dodaj)

for i in range(ilosczer):
    tablica.append(0)

for i in range(len(tablica)):
    print(tablica[i])