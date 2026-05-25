import random

def sortowanie_babelkowe(tablica):
    n = len(tablica)
    flaga = True
    for i in range(n):
        for j in range(n-1-i):
            if tablica[j]>tablica[j+1]:
                flaga = False
                temp = tablica[j]
                tablica[j] = tablica[j+1]
                tablica[j+1] = temp
        if flaga:
             break

tab = [0]*100

for i in range(100):
    tab[i] = random.randint(1,100)
sortowanie_babelkowe(tab)
print("Posortowana tablica: ")
for i in range(100):
    if i!=99:
        print(tab[i],end=",")
    else:
        print(tab[i])
