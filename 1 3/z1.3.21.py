ile = int(input())
przesuniecie = int(input())
tablica = []
drugatablica=[]
sumatablic = []
for i in range(ile):
    tablica.append(int(input()))
for i in range(ile):
    drugatablica.append(int(input()))

for i in range(przesuniecie):
    ostatnilement = tablica[ile-1]
    for j in range(len(tablica)-1):
        tablica[ile-1-j]=tablica[ile-1-j-1]
    tablica[0]=ostatnilement

for i in range(przesuniecie):
    pierwszyelement = drugatablica[0]
    for j in range(len(drugatablica)-1):
        drugatablica[j]=drugatablica[j+1]
    drugatablica[ile-1]=pierwszyelement

for i in range(ile):
    sumatablic.append(tablica[i]+drugatablica[i])

print(sumatablic)





