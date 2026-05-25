def wstawianie(tab):
    n = len(tab)
    for i in range(1,len(tab)):
        klucz = tab[i]
        j = i
        while j>0 and klucz<tab[j-1]:
            tab[j] = tab[j-1]
            j-=1
        tab[j] = klucz

def wstawianie2(tab):
    n = len(tab)
    for i in range(1,len(tab)):
        k = tab[i]
        j = i-1
        while j>=0 and tab[j]>k:
            tab[j+1] = tab[j]
            j-=1
        tab[j+1] = k

tab = [8,6,67,2,5,9]
wstawianie2(tab)
print(tab)