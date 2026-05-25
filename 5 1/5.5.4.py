def sito(n):
    n = n*2
    tab = []
    for i in range(2,n+1):
        tab.append(i)
    for i in range(2,int(n**1/2)+1):
        for j in range(n-1):
            if tab[j]!=0 and tab[j]%i==0 and tab[j]!=i:
                tab[j] = 0
    l_pierwsze = []
    for i in range(len(tab)):
        if tab[i]!=0:
            l_pierwsze.append(tab[i])
    return l_pierwsze

def sophie_germain(pierwsze):
    for i in range(len(pierwsze)):
        for j in range(i+1,len(pierwsze)):
            if 2*pierwsze[i]+1 == pierwsze[j]:
                print(pierwsze[i],end=" ")
n = int(input())
sophie_germain(sito(n))
        
