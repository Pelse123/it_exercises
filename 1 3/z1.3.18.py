ile = int(input())
przesuniecie = int(input())
tablica = []
for i in range(ile):
    tablica.append(int(input()))

for i in range(przesuniecie):
    pierwszyelement = tablica[0]
    for j in range(len(tablica)-1):
        tablica[j]=tablica[j+1]
    tablica[ile-1]=pierwszyelement

for i in tablica:
    print(i,end=" ")

