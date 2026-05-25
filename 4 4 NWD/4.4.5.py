def nwd_it(a,b):
    while b!=0:
        a,b = b,a%b
    return a

def NWW(a,b):
    return a*b//nwd_it(a,b)


l = int(input())
tab = []
for i in range(l):
    tab.append(int(input()))

wynik = tab[0]
for i in range(1,l):
    wynik = NWW(wynik,tab[i])
print(wynik)