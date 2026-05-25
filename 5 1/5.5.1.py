def sito_eratostenesa(n):
    tab = []
    for i in range(2,n+1):
        tab.append(i)
    for i in range(2,int(n**1/2)+1):
        for j in range(n-1):
            if tab[j]!=0 and tab[j]%i==0 and tab[j] != i:
                tab[j] = 0
    for i in range(len(tab)):
        if tab[i] != 0  :
            print(tab[i], end=" ")

n = int(input())
sito_eratostenesa(n)