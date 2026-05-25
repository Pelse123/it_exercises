ile = int(input())
tablica = []
maks = 0
arytmetyczna = 0
for i in range(ile):
    tablica.append(int(input()))
mini = tablica[0]
for i in range(ile):
    if(tablica[i] < mini):
        mini = tablica[i]
    if(tablica[i] > maks):
        maks = tablica[i]
    arytmetyczna = arytmetyczna + tablica[i]
arytmetyczna = arytmetyczna / ile
print(f"Max: {maks}")
print(f"Min: {mini}")
print(f"Średnia: {arytmetyczna}")