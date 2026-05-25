def sito_eratostenesa(n):
    tab = []
    for i in range(2,n+1):
        tab.append(i)
    for i in range(2,int(n**1/2)+1):
        for j in range(n-1):
            if tab[j]!=0 and tab[j]%i==0 and tab[j] != i:
                tab[j] = 0
    l_pierwsze =[]
    for i in range(len(tab)):
        if tab[i] != 0  :
            l_pierwsze.append(tab[i])
    return l_pierwsze

def blizniacze(tab):
    for i in range(1,len(tab)):
        if tab[i]-2 == tab[i-1]  :
            print(f"({tab[i-1]} {tab[i]})", end=" ")

n = int(input())
blizniacze(sito_eratostenesa(n))