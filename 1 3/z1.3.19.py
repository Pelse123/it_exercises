ile = int(input())
przesuniecie = int(input())
tablica = []
for i in range(ile):
    tablica.append(int(input()))

for i in range(przesuniecie):
    ostatnilement = tablica[ile-1]
    for j in range(len(tablica)-1):
        tablica[ile-1-j]=tablica[ile-1-j-1]
    tablica[0]=ostatnilement

for i in tablica:
    print(i,end=" ")

