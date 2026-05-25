def wyznacz_pivot(tab, lewy_index, prawy_index):
    index_pivota = prawy_index
    index_granicy = lewy_index
    for i in range(lewy_index,prawy_index):
        if tab[i]<tab[index_pivota]:
            tab[i],tab[index_granicy] = tab[index_granicy],tab[i]
            index_granicy += 1
    tab[index_pivota],tab[index_granicy] = tab[index_granicy],tab[index_pivota]

    return index_granicy
def quick_sort(tab, lewy_index, prawy_index):
    if lewy_index < prawy_index:
        pivot = wyznacz_pivot(tab, lewy_index, prawy_index)
        quick_sort(tab, lewy_index, pivot-1)
        quick_sort(tab, pivot+1, prawy_index)

p= int(input())
n = int(input())
tab = []
for i in range(n):
    tab.append(int(input()))
lewy_index = 0
prawy_index = len(tab)-1
tab[p],tab[prawy_index] = tab[prawy_index],tab[p]
quick_sort(tab, lewy_index, prawy_index)
for i in range(len(tab)):
    print(tab[i],end=" ")