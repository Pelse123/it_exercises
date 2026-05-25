def max_tablicy(tab):
    maks = 0
    for i in range(len(tab)):
        if tab[i] > maks:
            maks = tab[i]
    return maks

def min_tablicy(tab):
    mini = tab[0]
    for i in range(len(tab)):
        if tab[i] < mini:
            mini = tab[i]
    return mini

def roznica_min_max(tab):
    roznica = max_tablicy(tab) - min_tablicy(tab)
    return roznica


n = int(input())
tablica = []
for i in range(n):
    tablica.append(int(input()))
print(roznica_min_max(tablica))