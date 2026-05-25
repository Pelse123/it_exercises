ile = int(input())
tablica = []
for i in range(ile):
    tablica.append(int(input()))

for i in range(ile,0,-1):
    print(tablica[i-1])
