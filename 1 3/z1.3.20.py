ile = int(input())

tablica = []
drugatablica = []
tablicatymczasowa=[]
for i in range(ile):
    tablica.append(int(input()))
for i in range(ile):
    drugatablica.append(int(input()))

czyjest = False
tablicatymczasowa = tablica

for i in range(ile-1):
    pierwszyelement = tablica[0]
    for j in range(len(tablica)-1):
        tablica[j]=tablica[j+1]
    tablica[ile-1]=pierwszyelement
    if(tablica==drugatablica):
        czyjest = True
        break
if(czyjest == False):
    tablica = tablicatymczasowa
    for i in range(ile-1):
        ostatnilement = tablica[ile - 1]
        for j in range(len(tablica) - 1):
            tablica[ile - 1 - j] = tablica[ile - 1 - j - 1]
        tablica[0] = ostatnilement
        if (tablica == drugatablica):
            czyjest = True
            break

if(czyjest == True):
    print("Druga tablica jest rotacją pierwszej tablicy.")
else:
    print("Druga tablica nie jest rotacją pierwszej tablicy.")




