def odwroc_pary(tab):
    temp = 0
    for i in range(0,len(tab)-1,2):
        temp = tab[i+1]
        tab[i+1] = tab[i]
        tab[i] = temp
    if (len(tab) % 2 != 0):
        temp = tab[0]
        tab[0] = tab[len(tab)-1]
        tab[len(tab)-1] = temp
    return tab


n = int(input())
tablica = []
for i in range(n):
    tablica.append(int(input()))
tablica = odwroc_pary(tablica)
for i in range(n):
    print(tablica[i],end=" ")