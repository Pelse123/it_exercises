def nwd_it(a,b):
    while b!=0:
        a,b = b,a%b
    return a

l = int(input())
tab = []
for i in range(l):
    tab.append(int(input()))
nwd = tab[0]
for i in range(1,l):
    nwd = nwd_it(nwd,tab[i])
print(nwd)
