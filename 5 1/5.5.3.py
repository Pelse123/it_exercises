
def ciag_fibbo(n):
    ciag = [0,1]
    for i in range(2,n):
        ciag.append(ciag[i-1] + ciag[i-2])
    return ciag
def sito_eratostenesa(ciag):
    tab = []
    n = ciag[len(ciag)-1]
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
def l_pierwsze_fibbo(ciag,l_pierwsze):
    for i in range(len(ciag)):
        for j in range(len(l_pierwsze)):
            if ciag[i] == l_pierwsze[j]:
                print(l_pierwsze[j],end=" ")

n = int(input())
l_pierwsze_fibbo(ciag_fibbo(n),sito_eratostenesa(ciag_fibbo(n)))